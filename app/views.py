from django.shortcuts import render
from .models import PdfDocument
from django.http import JsonResponse
from transformers import BartForConditionalGeneration, BartTokenizer
import pdfplumber

model_name = "facebook/bart-large-cnn"
model = BartForConditionalGeneration.from_pretrained(model_name)
tokenizer = BartTokenizer.from_pretrained(model_name)

def extract_text_from_pdf(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

def summarize_pdf(request):
    if request.method == 'POST':
        pdf_file = request.FILES.get('pdf_file')
        if pdf_file:
            # Save the uploaded PDF file
            pdf_document = PdfDocument(file=pdf_file)
            pdf_document.save()

            # Extract text from the PDF
            text = extract_text_from_pdf(pdf_file)

            # Generate a summary using the Seq2Seq model
            inputs = tokenizer(text, return_tensors="pt", max_length=1024, truncation=True)
            summary_ids = model.generate(inputs["input_ids"], max_length=200, min_length=150, length_penalty=2.0, num_beams=4, early_stopping=True)
            summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

            sentences = summary.split(". ")
            points = "\n".join([f"• {sentence}" for sentence in sentences])

            return render(request, 'uploads.html', {'summary': points})

    return render(request, 'uploads.html')

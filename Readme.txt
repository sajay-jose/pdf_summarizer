Django project for building a PDF summarizer using a pre-trained sequence-to-sequence model called BartForConditionalGeneration from the transformers library. 
The goal of the project is to extract text from PDF documents and generate concise summaries of the content using a pre-trained model.


Navigate to Your Project Directory:
cd path/to/your/project

Create Virtual Environment:
python -m venv venv

Activate Virtual Environment:
venv\Scripts\activate

Install Required Packages:
pip install transformers pdfplumber django

Install PyTorch:
PyTorch library required for using BartForConditionalGeneration from the transformers library.

pip install torch==1.8.0+cpu torchvision==0.9.0+cpu torchaudio==0.8.0 -f https://download.pytorch.org/whl/cpu/torch_stable.html

python manage.py makemigrations
python manage.py migrate
python manage.py runserver



Libraries Used:
transformers: Used for working with pre-trained natural language processing models, including the BartForConditionalGeneration model.
pdfplumber: Used for extracting text content from PDF documents.
gradio: Initially used for creating a simple web-based interface for interacting with the summarization function.

Functionality:
Users can upload PDF files through a web interface.
The code extracts text content from the uploaded PDF using pdfplumber.
It then utilizes the BartForConditionalGeneration model and tokenizer from transformers to generate a summary of the text.
The generated summary is processed to present it in bullet-point format.

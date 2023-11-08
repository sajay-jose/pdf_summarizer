from django.db import models

class PdfDocument(models.Model):
    file = models.FileField(upload_to='pdfs/')
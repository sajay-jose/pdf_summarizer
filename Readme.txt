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


# Enviando E-mails SMTP
import os
from dotenv import load_dotenv
import pathlib
import string
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

HTML_PATH = pathlib.Path(__file__).parent / 'aula303.html'
load_dotenv()

# dados remetente
remetente = os.getenv('FROM_EMAIL', '')
password = os.getenv('EMAIL_PASSWORD', '')

# dados destinatario
destinatario = 'ed.henrique.picolo@gmail.com'

# configurações SMTP
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_user = os.getenv('FROM_EMAIL', '')
smtp_password = os.getenv('EMAIL_PASSWORD', '')

with open(HTML_PATH, 'r', encoding='utf-8') as file:
    texto = file.read()
    template = string.Template(texto)
    email = template.substitute(nome='Edson')

#  Transformar msg em MIMEMultipart
mime_mult = MIMEMultipart()
mime_mult['from'] = remetente
mime_mult['to'] = destinatario
mime_mult['subject'] = 'Este é o assunto do e-mail'

corpo_email = MIMEText(texto, 'html', 'utf-8')
mime_mult.attach(corpo_email)

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_user, smtp_password)
    server.send_message(mime_mult)
    print('E-mail enviado com sucesso')

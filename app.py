from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
import os
import smtplib
from email.mime.text import MIMEText
# import mailtrap as mt
# from sendgrid import SendGridAPIClient
# from sendgrid.helpers.mail import Mail

app = FastAPI()

# Modelo de datos del empleado que llegara al servicio
class Employee(BaseModel):
    first_name: str
    last_name: str
    email: str
    token: str

# El token compartido con Symfony
BACKEND_SHARED_TOKEN_PHP_PY = os.environ.get("BACKEND_SHARED_TOKEN_PHP_PY")  

if BACKEND_SHARED_TOKEN_PHP_PY is None:
    raise Exception("SHARED_TOKEN not set in environment variables.")

@app.post("/smtplib-gmail")
async def send_welcome_email(employee: Employee):

    print("Incoming request data: ", employee)
    
    if employee.token != BACKEND_SHARED_TOKEN_PHP_PY:
        raise HTTPException(status_code=403, detail="Invalid token")

    body = f"Hola {employee.first_name} {employee.last_name},\n\n¡Bienvenido a la empresa! Estamos emocionados de tenerte en el equipo.\n\nPuedes entrar a nuestro sistema <a href='http://localhost:5173/login'> -entrar- </a> y ver tus datos. \n\n Tus datos de acceso son tu correo y la clave temporal de: 123456"
    subject = f"Bienvenido a la empresa {employee.first_name} {employee.last_name}"
    sender = os.environ.get("BACKEND_EMAIL_SENDER_PY")
    recipients = [ sender , employee.email ]

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = ', '.join(recipients)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_sender:
        
        smtp_sender.login(sender, os.environ.get("BACKEND_EMAIL_TOKEN_PY") )
        smtp_sender.sendmail(sender, recipients, msg.as_string())

    return "Email sent!"
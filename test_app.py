import os
import pytest
from fastapi.testclient import TestClient
from app import app

# Configurar variables de entorno necesarias para las pruebas
os.environ["BACKEND_SHARED_TOKEN_PHP_PY"] = os.environ.get("BACKEND_SHARED_TOKEN_PHP_PY")

client = TestClient(app)

# Mock para evitar enviar correos reales
class MockSMTP:
    def __init__(self, *args, **kwargs):
        pass

    def login(self, *args, **kwargs):
        pass

    def sendmail(self, sender, recipients, msg):
        print(f"Mock email sent from {sender} to {recipients}. Content: {msg}")

    def quit(self):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

@pytest.fixture
def mock_smtp(monkeypatch):
    monkeypatch.setattr("smtplib.SMTP_SSL", MockSMTP)

def test_send_welcome_email(mock_smtp):
    # Datos del empleado para la prueba
    employee_data = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "token": os.environ["BACKEND_SHARED_TOKEN_PHP_PY"],  # Debe coincidir con BACKEND_SHARED_TOKEN_PHP_PY
    }

    # Llamar al endpoint
    response = client.post("/smtplib-gmail", json=employee_data)

    # Verificar el estado de la respuesta
    assert response.status_code == 200
    assert response.json() == "Email sent!"

import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    respuesta = client.get('/api/health')
    assert respuesta.status_code == 200

def test_obtener_productos(client):
    respuesta = client.get('/api/productos')
    assert respuesta.status_code == 200
    assert len(respuesta.get_json()["productos"]) >= 2

def test_crear_producto_exitoso(client):
    nuevo_prod = {"nombre": "Cheesecake", "precio": 14000, "stock": 8}
    respuesta = client.post('/api/productos', json=nuevo_prod)
    assert respuesta.status_code == 201
    assert respuesta.get_json()["producto"]["nombre"] == "Cheesecake"

def test_crear_producto_fallido(client):
    prod_malo = {"nombre": "Galletas sin precio"}
    respuesta = client.post('/api/productos', json=prod_malo)
    assert respuesta.status_code == 400
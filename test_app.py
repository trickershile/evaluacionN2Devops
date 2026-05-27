import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    rv = client.get('/health')
    assert rv.status_code == 200
    assert b'ok' in rv.data

def test_get_productos(client):
    rv = client.get('/productos')
    assert rv.status_code == 200
    assert b'Torta de Chocolate' in rv.data

def test_create_producto(client):
    rv = client.post('/productos', json={"nombre": "Galletas", "precio": 5000})
    assert rv.status_code == 201
    assert b'Galletas' in rv.data

def test_create_producto_invalido(client):
    # Prueba de manejo de error 400
    rv = client.post('/productos', json={"nombre": "Galletas"})  # Falta el precio
    assert rv.status_code == 400
    assert b'Faltan datos requeridos' in rv.data


def test_update_producto(client):
    rv = client.put('/productos/1', json={"precio": 16000})
    assert rv.status_code == 200
    assert b'16000' in rv.data


def test_delete_producto_no_existente(client):
    # Prueba de manejo de error 404
    rv = client.delete('/productos/999')
    assert rv.status_code == 404
    assert b'no existe' in rv.data

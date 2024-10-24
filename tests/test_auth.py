def test_register(client):
    response = client.post('/api/auth/register', json={
        'email': 'test@example.com',
        'phone': '+1234567890',
        'password': 'SecurePass123!'
    })
    assert response.status_code == 201
    assert b'User registered successfully' in response.data

def test_login(client, farmer):
    response = client.post('/api/auth/login', json={
        'email': 'farmer@example.com',
        'password': 'SecurePass123!'
    })
    assert response.status_code == 200
    assert 'access_token' in response.json

# tests/test_marketplace.py
def test_create_product(client, farmer):
    # First create a farm for the farmer
    farm_response = client.post('/api/profile/farm', 
        headers={'Authorization': f'Bearer {farmer.get_auth_token()}'},
        json={
            'name': 'Test Farm',
            'location': 'Test Location',
            'size': 100,
            'farming_methods': ['organic']
        })
    assert farm_response.status_code == 201
    
    # Then create a product
    response = client.post('/api/marketplace/products',
        headers={'Authorization': f'Bearer {farmer.get_auth_token()}'},
        json={
            'name': 'Test Product',
            'crop_type': 'Tomatoes',
            'quantity': 100,
            'unit': 'kg',
            'price_per_unit': 2.50,
            'quality_grade': 'A',
            'harvest_date': '2024-12-01',
            'description': 'Fresh tomatoes'
        })
    assert response.status_code == 201
    assert b'Product created successfully' in response.data
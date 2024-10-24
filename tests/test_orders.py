def test_create_order(client, farmer):
    # Create a buyer
    buyer_response = client.post('/api/auth/register', json={
        'email': 'buyer@example.com',
        'phone': '+9876543210',
        'password': 'SecurePass123!'
    })
    assert buyer_response.status_code == 201
    
    # Login as buyer
    login_response = client.post('/api/auth/login', json={
        'email': 'buyer@example.com',
        'password': 'SecurePass123!'
    })
    token = login_response.json['access_token']
    
    # Create order
    response = client.post('/api/marketplace/orders',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'product_id': 1,
            'quantity': 10
        })
    assert response.status_code == 201
    assert b'Order created successfully' in response.data
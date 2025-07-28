def test_get_all_products():
    response = test_get_all_products.get('/products/')
    assert response.status_code == 200

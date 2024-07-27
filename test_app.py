import pytest
import jwt
import json
from unittest.mock import MagicMock

# Assuming your Flask app is defined in app.py
from app import app, user_manager, SECRET_KEY

@pytest.fixture
def client(mocker):
    app.config['TESTING'] = True
    mocker.patch('app.user_manager', autospec=True)
    return app.test_client()

# def test_profile_success(client, mocker):
#     # Mock the JWT decode method
#     mocker.patch('jwt.decode', return_value={'user': '12345'})

#     # mock_user = {
#     #     'id': 1,
#     #     'full_name': 'John Doe',
#     #     'matric_no': '12345',
#     #     'password': 'hashed_password'
#     # }
#     # json_user_object= json.dumps(mock_user)
#     # print(json_user_object)

#     mock_user = ('1', 'John Doe', '12345', 'hashed_password')

#     user_manager.get_user_by_matric_no = MagicMock(return_value=mock_user)

#     # Send a request with a valid token
#     response = client.get('/profile', headers={
#         'Authorization': 'Bearer valid_token'
#     })

#     print(response.json)

#     assert response.status_code == 200
    # assert response.json['message'] == 'User profile'
    # assert 'data' in response.json
    # assert response.json['data']['full_name'] == 'John Doe'
    # assert 'password' not in response.json['data']
def test_profile_missing_token(client):
    # Send a request without an Authorization header
    response = client.get('/profile')

    assert response.status_code == 401
    assert response.json['message'] == 'Token is missing!'

def test_profile_invalid_token(client, mocker):
    # Mock the JWT decode method to raise an exception
    mocker.patch('jwt.decode', side_effect=jwt.PyJWTError('Invalid token'))

    # Send a request with an invalid token
    response = client.get('/profile', headers={
        'Authorization': 'Bearer invalid_token'
    })

    assert response.status_code == 401
    assert response.json['message'] == 'Token is invalid!'

def test_profile_server_error(client, mocker):
    # Mock the JWT decode method
    mocker.patch('jwt.decode', return_value={'user': '12345'})

    # Make the user_manager.get_user_by_matric_no method raise an exception
    user_manager.get_user_by_matric_no = MagicMock(side_effect=Exception('Database error'))

    # Send a request with a valid token
    response = client.get('/profile', headers={
        'Authorization': 'Bearer valid_token'
    })

    assert response.status_code == 500
    assert response.json['message'] == 'An error occurred!'




import requests
from requests.structures import CaseInsensitiveDict

def add_order(token, bookId, customerName):
    headers = CaseInsensitiveDict()
    headers['Accept'] = 'application/json'
    headers['Authorization'] = f'Bearer {token}'
    json = {
        'bookId': bookId,
        'customerName': customerName
    }
    response = requests.post('https://simple-books-api.glitch.me/orders', headers=headers, json=json)
    return response

def delete_order(token, bookId):
    headers = CaseInsensitiveDict()
    headers['Accept'] = 'application/json'
    headers['Authorization'] = f'Bearer {token}'
    response = requests.delete(f'https://simple-books-api.glitch.me/orders/{bookId}', headers=headers)
    return response

def get_orders(token):
    headers = CaseInsensitiveDict()
    headers['Accept'] = 'application/json'
    headers['Authorization'] = f'Bearer {token}'
    response = requests.get(f'https://simple-books-api.glitch.me/orders', headers=headers)
    return response

def get_order(token, orderId):
    headers = CaseInsensitiveDict()
    headers['Accept'] = 'application/json'
    headers['Authorization'] = f'Bearer {token}'
    response = requests.get(f'https://simple-books-api.glitch.me/orders/{orderId}', headers=headers)
    return response


def edit_order(token, order_id, customerName):
    headers = CaseInsensitiveDict()
    headers['Accept'] = 'application/json'
    headers['Authorization'] = f'Bearer {token}'
    body = {
        'customerName': customerName
    }
    response = requests.patch(f'https://simple-books-api.glitch.me/orders/{order_id}', headers=headers, json=body)
    return response
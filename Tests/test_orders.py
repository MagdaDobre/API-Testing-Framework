from API_project.Requests.orders import *
from API_project.Requests.api_clients import *

class TestOrders:
    def setup_method(self):
        self.token = get_token()

    def test_add_order_book_out_of_stock(self):
        response = add_order(self.token, 2, 'Andrei')
        assert response.status_code == 404, 'Status code is not correct'
        assert response.json()['error'] == 'This book is not in stock. Try again later.'

    def test_add_valid_order(self):
        response = add_order(self.token, 1, 'Andrei')
        assert response.status_code == 201, 'Status code is not correct'
        assert response.json()['created'] is True, 'Order not created'
        # cleanup
        delete_order(self.token, response.json()['orderId'])

    def test_get_orders(self):
        add1 = add_order(self.token, 1, 'user1')
        add2 = add_order(self.token, 3, 'user2')
        response = get_orders(self.token)
        assert response.status_code == 200, 'Status code is not correct'
        assert len(response.json()) == 2, 'Total of orders returned is incorrect'
        #cleanup
        delete_order(self.token, add1.json()['orderId'])
        delete_order(self.token, add2.json()['orderId'])

    def test_delete_order(self):
        add = add_order(self.token, 1, 'user1')
        response = delete_order(self.token, add.json()['orderId'])
        assert response.status_code == 204, 'Status code is not correct'
        # extra verification if the order was deleted
        get_all = get_orders(self.token)
        assert len(get_all.json()) == 0, 'Order was not deleted'

    def test_delete_invalid_order_id(self):
        response = delete_order(self.token, '3434rdasd34')
        assert response.status_code == 404, 'Status code is not correct'
        assert response.json()['error'] == 'No order with id 3434rdasd34.', 'The error returned is not correct'

    def test_get_order(self):
        order_id = add_order(self.token, 1, 'user1').json()['orderId']
        response = get_order(self.token, id)
        assert response.status_code == 200, 'Status code is not correct'
        assert response.json()['id'] == order_id, 'order id is not correct'
        assert response.json()['bookId'] == 1, 'book Id is not correct'
        assert response.json()['customerName'] == 'User1', 'customerName is not correct'
        assert response.json()['quantity'] == 1, 'quantity is not correct'
        # # cleanup
        delete_order(self.token, order_id)

    def test_get_invalid_order_id(self):
        response = get_order(self.token, '768526329789')
        assert response.status_code == 404, 'Status code is not OK'
        assert response.json()['error'] == 'No order with id 768526329789.', 'The error returned is not correct'

    def test_patch_invalid_order_id(self):
        response = edit_order(self.token, '11519589', 'Alexandru')
        assert response.status_code == 404, 'Status code is not correct'
        assert response.json()['error'] == 'No order with id 11519589.', 'The error returned is not correct'

    def test_patch_valid_order(self):
        order_id = add_order(self.token, 1, 'Andrei').json()['orderId']
        response = edit_order(self.token, order_id, 'Stefan')
        assert response.status_code == 204, 'Status code is not correct'
        get = get_order(self.token, order_id)
        assert get.json()['customerName'] == 'Stefan', 'Customer name was not updated'
        #cleanup
        delete_order(self.token,order_id)
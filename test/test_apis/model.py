import uuid
import time


class User(object):
    user_id = None
    username = None

    def __init__(self, username: str):
        self.user_id = str(uuid.uuid4())
        self.username = username


class Book(object):
    book_id = None
    book_name = None
    price = None

    def __init__(self, book_name: str, book_price: float):
        self.book_id = str(uuid.uuid4())
        self.book_name = book_name
        self.price = book_price


class Order(object):
    order_id = None
    user_id = None
    book_id = None
    created_at = None

    def __init__(self, user_id, book_id):
        self.order_id = str(uuid.uuid4())
        self.user_id = user_id
        self.book_id = book_id
        self.created_at = int(time.time())

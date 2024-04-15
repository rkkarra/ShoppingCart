from cart import Cart

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.cart = Cart()



class Cart():
    def __init__(self, request):
        self.session = request.session
        self.cart = self.session.get('session_key', {})

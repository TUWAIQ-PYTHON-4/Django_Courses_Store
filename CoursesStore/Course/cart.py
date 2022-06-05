from .models import Course
from decimal import Decimal


class Cart():
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('skey')
        if 'skey' not in request.session:
            cart = self.session['skey'] = {}
        self.cart = cart

    def add(self, course):
        course_id = course.id
        if course_id not in self.cart:
            self.cart[course_id] = {'price': str(course.price)}

        self.session.modified = True

    def __iter__(self):
        courses_id = self.cart.keys()
        courses = Course.objects.filter(id__in=courses_id)
        cart = self.cart.copy()
        for c in courses:
            cart[str(c.id)]['course'] = c

        for item in cart.values():
            item['price'] = (item['price'])
            item['totalprice'] = item['price'] * 1.50



from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, JsonResponse


# def cart_summary(request: HttpRequest):
#     cart = Cart(request)
#     return render(request, 'cart.html', {'cart': cart})
#
#
# def add_to_cart(request: HttpRequest):
#     cart = Cart(request)
#     if request.POST.get('action') == 'post':
#         course_id = int(request.POST.get('courseid'))
#         course = get_object_or_404('Course.Course', id=course_id)
#         cart.add(course=course)
#         response = JsonResponse({'test': 'data'})
#         return response

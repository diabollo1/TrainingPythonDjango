from django.shortcuts import render
from django.http import HttpResponse
from django.template import context

from cake.models import *


def index(request):
    products = Cake.objects.all()
    categories = Category.objects.all()
    data = {'products': products, 'categories': categories}
    return render(request, 'cake_list.html', data)


def category(request, category_id):
    category_output = Category.objects.get(pk=category_id)
    return HttpResponse(category_output)


def product(request, product_id):
    product_output = Cake.objects.get(pk=product_id)
    output = "<h1>" + str(product_output) + "</h1>" + \
             "<p>" + str(product_output.description) + "</p>" + \
             "<p>" + str(product_output.price) + "</p>" + \
             "<p><img src='../" + str(product_output.img.url) + "'></p>"
    return HttpResponse(output)

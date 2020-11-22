from django.shortcuts import render
from cake.models import *


def website(request):
    products = Cake.objects.all()
    categories = Category.objects.all()
    data = {'products': products, 'categories': categories}
    return render(request, 'index.html', data)
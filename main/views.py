from django.shortcuts import render

from main.models import Product


def index(request):

    for product_item in Product.objects.all().order_by('-pk')[:5]:
        print(product_item)

    return render(request, 'main/home.html')


def contacts(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        print(f"{name} - {phone} - {message}")

    return render(request, 'main/contacts.html')
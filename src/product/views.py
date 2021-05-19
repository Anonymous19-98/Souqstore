from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator

# Create your views here.


def product_list(request):
    product_list = Product.objects.all()

    paginator = Paginator(product_list, 8)  # Show 25 contacts per page.
    page = request.GET.get('page')
    product_list = paginator.get_page(page)

    context = {'product_list': product_list}
    return render(request, 'product/product_list.html', context)


def product_details(request, slug):
    product_details = Product.objects. get(PRDSlug=slug)
    context = {'product_details': product_details}
    return render(request, 'product/product_details.html', context)

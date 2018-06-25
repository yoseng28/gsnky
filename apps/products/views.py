from django.shortcuts import render

from products.models import ProductType, Product


def productsTreeView(request):
    product_list = Product.objects.all()
    product_type_nodes = ProductType.objects.all()
    return render(request, 'zblist.html', {'nodes': product_type_nodes, 'product_list': product_list})

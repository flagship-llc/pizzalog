from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Shop


def index(request):
    shop_list = Shop.objects.order_by('-pub_date')[:5]
    context = {
        'shop_list': shop_list,
    }
    return render(request, 'shops/index.html', context)


def detail(request, shop_id):
    shop = get_object_or_404(Shop, pk=shop_id)
    return render(request, 'shops/detail.html', {'shop': shop})

from django.shortcuts import render, get_object_or_404
from .models import Item


def item_list(request):
    ob_items = Item.objects.all()
    return render(request, 'item_list.html', {'items': ob_items})

def item_detail(request, pk):
    ob_item = get_object_or_404(Item, pk=pk)
    return render(request, 'item_detail.html', {'item': ob_item})
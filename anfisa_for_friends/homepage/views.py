# Для применения Q-объектов их нужно импортировать:
from django.db.models import Q
from django.shortcuts import render

from ice_cream.models import IceCream

def index(request):
    template_name = 'homepage/index.html'
    # Запрос:
    ice_cream_list = (
        IceCream.objects
        .filter(is_on_main=True, is_published=True)
        .order_by('title')
        .values('id', 'title', 'description', 'wrapper__title')
    )
    context = {
        # 'ice_cream_list': ice_cream_list,
        'categories': categories
    }
    return render(request, template_name, context) 
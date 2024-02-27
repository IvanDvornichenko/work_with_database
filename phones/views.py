from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phone_list = Phone.objects.all()
    sort = request.GET.get('sort')
    if sort == 'max_price':
        phone_list_max = phone_list.order_by('-price')
        context = {'phones': phone_list_max}
        return render(request, template, context)
    elif sort == 'min_price':
        phone_list_max = phone_list.order_by('price')
        context = {'phones': phone_list_max}
        return render(request, template, context)
    elif sort == 'name':
        phone_list_max = phone_list.order_by('name')
        context = {'phones': phone_list_max}
        return render(request, template, context)
    else:
        context = {'phones': phone_list}
        return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {'phone': Phone.objects.filter(slug=slug).first()}
    print(context)
    return render(request, template, context)

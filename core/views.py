from django.shortcuts import render, get_object_or_404
from .models import Produto


def index(request):
    produtos = Produto.objects.all()
    context = {
        'curso': 'Programação com Django Frameworks',
        'produtos': produtos,
    }
    return render(request, 'core/index.html', context)


def contato(request):
    return render(request, 'core/contato.html')


def produto(request, id):
    # produto = Produto.objects.get(id=id)
    prod = get_object_or_404(Produto, id=id)
    context = {
        'produto': prod,
    }
    return render(request, 'core/produto.html', context)


def handler_404(request, exception):
    return render(request, 'core/404.html')

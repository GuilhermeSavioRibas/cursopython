from django.shortcuts import render, get_object_or_404
from .models import Cliente
from django.core.paginator import Paginator
from django.http import Http404
from django.db.models import Q, Value
from django.db.models.functions import Concat
# Create your views here.


def index(request):
    clientes = Cliente.objects.order_by('-id')
    paginator = Paginator(clientes, 20)
    page = request.GET.get('p')
    clientes = paginator.get_page(page)
    return render(request, 'clientes/index.html', {
        'clientes': clientes
    })


def ver_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)

    return render(request, 'clientes/ver_cliente.html', {
        'cliente': cliente
    })


def busca(request):
    termo = request.GET.get('termo')

    if termo is None:
        raise Http404()
    campos = Concat('nome', Value(' '), 'sobrenome')

    clientes = Cliente.objects.annotate(
        nome_completo=campos
    ).filter(
        Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo)
    ).order_by('-id')
    paginator = Paginator(clientes, 20)
    page = request.GET.get('p')
    clientes = paginator.get_page(page)
    return render(request, 'clientes/busca.html', {
        'clientes': clientes
    })

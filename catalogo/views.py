from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render

from .forms import LugarForm
from .models import Categoria, LugarPatrimonial


# ---------------------------------------------------------------
# Vistas públicas: cualquier visitante puede verlas
# ---------------------------------------------------------------

def inicio(request):
    # Los 3 últimos lugares agregados (select_related evita una consulta extra por cada categoría)
    recientes = LugarPatrimonial.objects.select_related('categoria').order_by('-id')[:3]
    contexto = {
        'recientes': recientes,
        'total_lugares': LugarPatrimonial.objects.count(),
        'total_categorias': Categoria.objects.count(),
    }
    return render(request, 'inicio.html', contexto)


def catalogo(request):
    lugares = LugarPatrimonial.objects.select_related('categoria')
    return render(request, 'catalogo.html', {'lugares': lugares})


def detalle_lugar(request, pk):
    # Si el id no existe responde 404 en vez de romper la página
    lugar = get_object_or_404(LugarPatrimonial.objects.select_related('categoria'), pk=pk)
    return render(request, 'detalle_lugar.html', {'lugar': lugar})


def lista_categorias(request):
    # annotate + Count agrega a cada categoría la cantidad de lugares que tiene
    categorias = Categoria.objects.annotate(total_lugares=Count('lugares'))
    return render(request, 'categorias.html', {'categorias': categorias})


def lugares_por_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    lugares = LugarPatrimonial.objects.filter(categoria=categoria)
    contexto = {'categoria': categoria, 'lugares': lugares}
    return render(request, 'lugares_por_categoria.html', contexto)


# ---------------------------------------------------------------
# Área de gestión: solo usuarios autenticados
# ---------------------------------------------------------------

@login_required
def gestion(request):
    lugares = LugarPatrimonial.objects.select_related('categoria')
    return render(request, 'gestion.html', {'lugares': lugares})


# Dos filtros apilados:
#   1) login_required: si no hay sesión, redirige al login.
#   2) permission_required: si hay sesión pero falta el permiso, responde 403.
@login_required
@permission_required('catalogo.add_lugarpatrimonial', raise_exception=True)
def crear_lugar(request):
    if request.method == 'POST':
        form = LugarForm(request.POST)
        if form.is_valid():
            lugar = form.save()
            messages.success(request, f'Se agregó "{lugar.nombre}" al catálogo.')
            return redirect('gestion')
    else:
        form = LugarForm()
    contexto = {'form': form, 'titulo': 'Agregar lugar patrimonial'}
    return render(request, 'formulario_lugar.html', contexto)


@login_required
@permission_required('catalogo.change_lugarpatrimonial', raise_exception=True)
def editar_lugar(request, pk):
    lugar = get_object_or_404(LugarPatrimonial, pk=pk)
    if request.method == 'POST':
        form = LugarForm(request.POST, instance=lugar)
        if form.is_valid():
            form.save()
            messages.success(request, f'Se actualizó "{lugar.nombre}".')
            return redirect('gestion')
    else:
        form = LugarForm(instance=lugar)
    contexto = {'form': form, 'titulo': f'Editar: {lugar.nombre}'}
    return render(request, 'formulario_lugar.html', contexto)

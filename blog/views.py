from django.shortcuts import render, get_object_or_404, redirect
from .models import Publicacion
from .forms import PublicacionForm

# Vista para mostrar la lista de publicaciones
def lista_publicaciones(request):
    publicaciones = Publicacion.objects.all()
    return render(request, 'blog/lista_publicaciones.html', {'publicaciones': publicaciones})

# Vista detallada para mostrar el contenido completo de una publicación
def detalle_publicacion(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    return render(request, 'blog/detalle_publicacion.html', {'publicacion': publicacion})

# Vista para crear una nueva publicación
def crear_publicacion(request):
    if request.method == 'POST':
        form = PublicacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_publicaciones')  # Redirige a la lista de publicaciones después de guardar
    else:
        form = PublicacionForm()
    return render(request, 'blog/crear_publicacion.html', {'form': form})

# Create your views here.

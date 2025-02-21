from django.shortcuts import render
from mainapp.models import Himnosycoros, Categorias, Tipos, Notas
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q


# Create your views here.

def index(request):

    return render(request, 'index.html', {
        'titulo': "Administrador de Himnario con Notas"
        
    })

@login_required(login_url="login")
def register_song(request):

    notas = Notas.objects.order_by('nota')
    tipos = Tipos.objects.order_by('tipo')
    categorias = Categorias.objects.order_by('categoria')

    return render(request, 'guardar_cancion.html',{
        'titulo': "Registrar Himno o Coro",
        'notas': notas,
        'tipos': tipos,
        'categorias': categorias
    })

@login_required(login_url="login")
def save_song(request):

    if request.method == "POST":
        
        titulo = request.POST['titulo']
        tono = request.POST['tono']
        nota = request.POST['nota']
        tipo = request.POST['tipo']
        urlvideo = request.POST['urlvideo']
        himno = request.POST['cancion']
        autor = request.POST['autor']
        categoria = request.POST['categoria']

        songs = Himnosycoros(
            titulo = titulo,
            tono = tono,
            nota = nota,
            tipo = tipo,
            autor = autor,
            himno = himno,
            url = urlvideo,
            categoria = categoria
        )

        songs.save()
        messages.success(request, f'Se ha guardado el himno {titulo}')

        return redirect('table_song')

    else:
        messages.error(request, 'No se ha podido guardar')

@login_required(login_url="login")
def table_song(request):

    queryset = request.GET.get("buscar_cancion")
    song = Himnosycoros.objects.order_by('titulo')

    if queryset:
        query = Q(titulo__contains=queryset)
        query.add(Q(himno__contains=queryset), Q.OR)

        song = Himnosycoros.objects.filter(query)

    paginator = Paginator(song, 10)
    #recoger numero de pagina
    page = request.GET.get('page')
    page_canciones = paginator.get_page(page)

    return render(request, 'tabla_canciones_agregadas.html',{
        'titulo': "Himnos y Coros",
        'canciones': page_canciones,  
        'paginator': paginator  
    })

@login_required(login_url="login")
def show_form_song_edit(request):

    if request.method == "POST":
        id_cancion = request.POST['id_cancion']
        pagina_actual = request.POST['pagina_actual']

    cancion = Himnosycoros.objects.get(pk=id_cancion)

    return render(request, 'editar_cancion.html',{
        'titulo': "Editar canción",
        'cancion': cancion,
        'pagina_actual': pagina_actual
    })

@login_required(login_url="login")
def edit_song(request):

    if request.method == "POST":
        
        id_himno = request.POST['id_cancion']
        titulo = request.POST['titulo']
        tono = request.POST['tono']
        nota = request.POST['nota']
        tipo = request.POST['tipo']
        urlvideo = request.POST['urlvideo']
        himno = request.POST['cancion']
        autor = request.POST['autor']
        estado = request.POST['estado']
        categoria = request.POST['categoria']

        pagina_actual = request.POST['pagina_actual']

        song = Himnosycoros.objects.get(pk=id_himno)
        song.titulo = titulo
        song.tono = tono
        song.nota = nota
        song.tipo = tipo
        song.autor = autor
        song.himno = himno
        song.url = urlvideo
        song.estado = estado
        song.categoria = categoria

        song.save()
        messages.success(request, f'Se ha editado el himno {titulo}')

        return redirect(pagina_actual)

    else:
        messages.error(request, 'No se ha podido editar')


def see_song(request, id_cancion):

    cancion = Himnosycoros.objects.get(id_himno=id_cancion)
    #cancion = get_object_or_404(Himnosycoros, id=id_cancion)

    #artista = cancion.artista
    #canciones = Canciones.objects.filter(artista=artista).order_by('titulo')

    #tipo_acordes = cancion.tipo_acordes
    letra = cancion.himno
    letra2 = letra.replace('{', f'<b><span class="chord0">')
    letra_cancion = letra2.replace('}','</span></b>')

    return render(request, 'ver_cancion.html',{
        'cancion': cancion,
        'letra': letra_cancion
    })

@login_required(login_url="login")
def user_logout(request):
    logout(request)
    return redirect('index')
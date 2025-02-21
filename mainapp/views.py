from django.shortcuts import render
from mainapp.models import Himno, Alabanza, HimnosFeAlabanza, Himnosycoros, Categorias, Tipos, Notas
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



def register_praise(request):

    return render(request, 'guardar_cancion.html',{
        'titulo': "Registrar Coro de alabanza",
        'tipo': "Alabanza",
        'url_save': "save_praise"
    })


def save_praise(request):

    if request.method == "POST":
        
        titulo = request.POST['titulo']
        tono = request.POST['tono']
        nota = request.POST['nota']
        tipo = request.POST['tipo']
        urlvideo = request.POST['urlvideo']
        himno = request.POST['cancion']
        autor = request.POST['autor']

        praise = Alabanza(
            titulo = titulo,
            tono = tono,
            nota = nota,
            tipo = tipo,
            autor = autor,
            himno = himno,
            url = urlvideo
        )

        praise.save()
        messages.success(request, f'Se ha guardado el coro {titulo}')

        return redirect('register_praise')

    else:
        messages.error(request, 'No se ha podido guardar')


def register_hymns(request):

    return render(request, 'guardar_cancion.html',{
        'titulo': "Registrar Himno de Fe y Alabanza",
        'tipo': "Congregacional",
        'url_save': "save_hymns"
    })


def save_hymns(request):

    if request.method == "POST":
        
        titulo = request.POST['titulo']
        tono = request.POST['tono']
        nota = request.POST['nota']
        tipo = request.POST['tipo']
        urlvideo = request.POST['urlvideo']
        himno = request.POST['cancion']
        autor = request.POST['autor']

        hymns = HimnosFeAlabanza(
            titulo = titulo,
            tono = tono,
            nota = nota,
            tipo = tipo,
            autor = autor,
            himno = himno,
            url = urlvideo
        )

        hymns.save()
        messages.success(request, f'Se ha guardado el himno {titulo}')

        return redirect('register_hymns')

    else:
        messages.error(request, 'No se ha podido guardar')



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


def table_praise(request):

    queryset = request.GET.get("buscar_cancion")
    praise = Alabanza.objects.order_by('titulo')

    if queryset:
        query = Q(titulo__contains=queryset)
        query.add(Q(himno__contains=queryset), Q.OR)

        praise = Alabanza.objects.filter(query)

    paginator = Paginator(praise, 10)
    #recoger numero de pagina
    page = request.GET.get('page')
    page_canciones = paginator.get_page(page)

    return render(request, 'tabla_canciones_agregadas.html',{
        'titulo': "Coros de Alabanza",
        'canciones': page_canciones,  
        'paginator': paginator  
    })



def table_hymns(request):

    queryset = request.GET.get("buscar_cancion")
    hymns = HimnosFeAlabanza.objects.order_by('titulo')

    if queryset:
        query = Q(titulo__contains=queryset)
        query.add(Q(himno__contains=queryset), Q.OR)
        query.add(Q(categoria__contains=queryset), Q.OR)

        hymns = HimnosFeAlabanza.objects.filter(query)

    paginator = Paginator(hymns, 10)
    #recoger numero de pagina
    page = request.GET.get('page')
    page_canciones = paginator.get_page(page)

    return render(request, 'tabla_canciones_agregadas.html',{
        'titulo': "Himnos de Fe y Alabanza",
        'canciones': page_canciones,  
        'paginator': paginator  
    })



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


def user_logout(request):
    logout(request)
    return redirect('index')
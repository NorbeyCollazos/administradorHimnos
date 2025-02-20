from django.shortcuts import render
from mainapp.models import Himno, Alabanza, HimnosFeAlabanza
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.core.paginator import Paginator
from django.db.models import Q


# Create your views here.
def register_worship(request):

    return render(request, 'guardar_cancion.html',{
        'titulo': "Registrar Himno de Adoración",
        'tipo': "Adoracion",
        'url_save': "save_worship"
    })


def save_worship(request):

    if request.method == "POST":
        
        titulo = request.POST['titulo']
        tono = request.POST['tono']
        nota = request.POST['nota']
        tipo = request.POST['tipo']
        urlvideo = request.POST['urlvideo']
        himno = request.POST['cancion']
        autor = request.POST['autor']

        worship = Himno(
            titulo = titulo,
            tono = tono,
            nota = nota,
            tipo = tipo,
            autor = autor,
            himno = himno,
            url = urlvideo
        )

        worship.save()
        messages.success(request, f'Se ha guardado el himno {titulo}')

        return redirect('register_worship')

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



def table_worship(request):

    queryset = request.GET.get("buscar_cancion")
    worship = Himno.objects.order_by('titulo')

    if queryset:
        query = Q(titulo__contains=queryset)
        query.add(Q(himno__contains=queryset), Q.OR)

        worship = Himno.objects.filter(query)

    paginator = Paginator(worship, 10)
    #recoger numero de pagina
    page = request.GET.get('page')
    page_canciones = paginator.get_page(page)

    return render(request, 'tabla_canciones_agregadas.html',{
        'titulo': "Himnos de Adoración",
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



def show_form_worship_edit(request):

    if request.method == "POST":
        id_cancion = request.POST['id_cancion']
        pagina_actual = request.POST['pagina_actual']

    cancion = Himno.objects.get(pk=id_cancion)

    return render(request, 'editar_cancion.html',{
        'titulo': "Editar canción",
        'cancion': cancion,
        'pagina_actual': pagina_actual
    })


def edit_worship(request):

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

        pagina_actual = request.POST['pagina_actual']

        worship = Himno.objects.get(pk=id_himno)
        worship.titulo = titulo
        worship.tono = tono
        worship.nota = nota
        worship.tipo = tipo
        worship.autor = autor
        worship.himno = himno
        worship.url = urlvideo
        worship.estado = estado

        worship.save()
        messages.success(request, f'Se ha editado el himno {titulo}')

        return redirect(pagina_actual)

    else:
        messages.error(request, 'No se ha podido editar')
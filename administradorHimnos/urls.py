"""administradorHimnos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

import mainapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('',mainapp.views.index, name='index'),
    path('logout/',mainapp.views.user_logout, name='user_logout'),
    path('register-song/',mainapp.views.register_song, name='register_song'),
    path('save-song/',mainapp.views.save_song, name='save_song'),
    path('register-praise/',mainapp.views.register_praise, name='register_praise'),
    path('save-praise/',mainapp.views.save_praise, name='save_praise'),
    path('register-hymns/',mainapp.views.register_hymns, name='register_hymns'),
    path('save-hymns/',mainapp.views.save_hymns, name='save_hymns'),

    path('table-song/',mainapp.views.table_song, name='table_song'),
    path('table-praise/',mainapp.views.table_praise, name='table_praise'),
    path('table-hymns/',mainapp.views.table_hymns, name='table_hymns'),

    path('song-edit/',mainapp.views.show_form_song_edit, name='show_form_song_edit'),
    path('data-song-edit/',mainapp.views.edit_song, name='data_song_edit'),

]

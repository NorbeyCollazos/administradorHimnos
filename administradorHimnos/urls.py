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
from django.urls import path

import mainapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register-worship/',mainapp.views.register_worship, name='register_worship'),
    path('save-worship/',mainapp.views.save_worship, name='save_worship'),
    path('register-praise/',mainapp.views.register_praise, name='register_praise'),
    path('save-praise/',mainapp.views.save_praise, name='save_praise'),
    path('register-hymns/',mainapp.views.register_hymns, name='register_hymns'),
    path('save-hymns/',mainapp.views.save_hymns, name='save_hymns'),

    path('table-worship/',mainapp.views.table_worship, name='table_worship'),
    path('table-praise/',mainapp.views.table_praise, name='table_praise'),
    path('table-hymns/',mainapp.views.table_hymns, name='table_hymns'),

    path('worship-edit/',mainapp.views.show_form_worship_edit, name='show_form_worship_edit'),
    path('data-worship-edit/',mainapp.views.edit_worship, name='data_worship_edit'),

]

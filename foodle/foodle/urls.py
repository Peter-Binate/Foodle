"""
URL configuration for foodle project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from ingredients import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'ingredients/', 
        views.ingredient_list, 
        name='ingredient-list'
    ),
    path(
        'ingredients/<int:ingredient_id>/', 
        views.ingredient_detail, 
        name='ingredient-detail'
    ),
    path(
        'contact-us/',
         views.contact,
         name='contact'   
    ),
    path(
        'ingredients/add',
        views.ingredient_create,
        name='ingredient-create'
    ),
    path(
        'ingredients/<int:ingredient_id>/update/',
        views.ingredient_update,
        name='ingredient-update'
    ),
    path(
        'ingredients/<int:ingredient_id>/delete/',
        views.ingredient_delete,
        name='ingredient-delete'
    )

]

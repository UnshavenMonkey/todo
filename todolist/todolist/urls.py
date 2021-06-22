"""todolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from mainapp.views import add_task, delete_task, add_category, filter_category, delete_category, complite_task
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls')),
    path('add/', add_task, name='add_task'),
    path('delete_task/<int:id>/', delete_task, name='delete_task'),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('register/', include('authapp.urls')),
    path('add_category/', add_category, name='add_category'),
    path('filter_category/<slug:category_name>/', filter_category, name='filter_category'),
    path('delete_category/<int:id>/', delete_category, name='delete_category'),
    path('complite_task/<int:id>/', complite_task, name='complite_task'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

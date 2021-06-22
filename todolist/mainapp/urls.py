from django.urls import path
from .views import add_task, index
from .views import by_category

urlpatterns = [
    path('<int:category_id>/', by_category),
    path('', index, name='index'),
]



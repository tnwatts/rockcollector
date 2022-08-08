from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('what', views.what, name='what'),
    path('rocks/', views.rocks_index, name='index'),
    path('rocks/<int:rock_id>/', views.rock_detail, name= 'detail'),
    path('rocks/create/', views.RockCreate.as_view(), name='rocks_create')
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('what', views.what, name='what'),
    path('rocks/', views.rocks_index, name='index'),
    path('rocks/<int:rock_id>/', views.rock_detail, name= 'detail'),
    path('rocks/create/', views.RockCreate.as_view(), name='rocks_create'),
    path('rocks/<int:pk>/update/', views.RockUpdate.as_view(), name='rocks_update'),
    path('rocks/<int:pk>/delete/', views.RockDelete.as_view(), name='rocks_delete'),
    path('rocks/<int:rock_id>/add_cleaning/', views.add_cleaning, name='add_cleaning'),
    path('rocks/<int:rock_id>/assoc_dirt/<int:dirt_id>/', views.assoc_dirt, name='assoc_dirt'),
    path('rocks/<int:rock_id>/unassoc_dirt/<int:dirt_id>/', views.unassoc_dirt, name='unassoc_dirt'),
    path('rocks/<int:rock_id>/add_photo/', views.add_photo, name='add_photo'),
    path('dirt/', views.DirtList.as_view(), name='dirt_index'),
    path('dirt/<int:pk>/', views.DirtDetail.as_view(), name='dirt_detail'),
    path('dirt/create/', views.DirtCreate.as_view(), name='dirt_create'),
    path('dirt/<int:pk>/update/', views.DirtUpdate.as_view(), name='dirt_update'),
    path('dirt/<int:pk>/delete/', views.DirtDelete.as_view(), name='dirt_delete'),    
]


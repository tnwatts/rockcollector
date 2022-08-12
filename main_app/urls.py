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
    path('rocks/<int:cat_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
  path('cats/<int:cat_id>/unassoc_toy/<int:toy_id>/', views.unassoc_toy, name='unassoc_toy'),
    path('dirt/', views.DirtList.as_view(), name='dirt_index'),
    path('rocks/<int:rock_id>/add_cleaning/', views.add_cleaning, name='add_cleaning'),
    # new path below
    path('rocks/<int:rock_id>/add_photo/', views.add_photo, name='add_photo'),
]


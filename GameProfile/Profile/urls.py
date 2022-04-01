from django.urls import path, include
from . import views

urlpatterns = [
    path('list/', views.list,name='account-list'),
    path('create/', views.create, name="account-create"),
    path('delete/<str:id>/', views.delete, name="account-delete"),
    path('edit/<str:id>/', views.edit, name="account-edit")
]

from django.urls import path, include
from . import views

urlpatterns = [
    path('list/', views.list, name='account-list'),
    path('create/', views.create, name="account-create"),
    path('delete/<str:id>/', views.delete, name="account-delete"),
    path('edit/<str:id>/', views.edit, name="account-edit"),
    path('account-list/', views.accountList, name="api-account-list"),
    path('account-detail/<str:id>/',views.accountDetail,name="api-account-detail"),
    path('account-create/',views.accountCreate,name="api-account-create"),
    path('account-delete/<str:id>/',views.accountDelete,name="api-account-delete"),
    path('account-update/<str:id>/',views.accountUpdate,name="api-account-update")
]

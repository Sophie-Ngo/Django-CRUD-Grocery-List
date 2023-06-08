from django.urls import path

from . import views

app_name = 'groceryapp'

urlpatterns = [
    path('', views.GroceriesListView.as_view(), name='grocerieslist'),
    path('<int:pk>/', views.GroceriesDetailView.as_view(), name='groceriesdetail'),
    path('create/', views.GroceriesCreateView.as_view(), name='groceriescreate'),
    path('<int:pk>/update/', views.GroceriesUpdateView.as_view(), name='groceriesupdate'),
    path('<int:pk>/delete/', views.GroceriesDeleteView.as_view(), name='groceriesdelete'),
]
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:id>/', views.listing_detail, name='listing_detail'),
    path('search/', views.search, name= 'search'),
]

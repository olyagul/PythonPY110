from django.urls import path
from . import views

app_name = 'app_wishlist'

urlpatterns = [
    path('', views.wishlist_view, name='wishlist_view'),
    path('api/', views.wishlist_view_json, name='wishlist_json'),
    path('api/add/<str:id_product>/', views.wishlist_add_view_json, name='wishlist_add_json'),
    path('api/del/<str:id_product>/', views.wishlist_del_view_json, name='wishlist_del_json'),
    path('remove/<str:id_product>/', views.wishlist_remove_view, name='wishlist_remove'),
]
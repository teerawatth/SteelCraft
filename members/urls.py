from django.urls import path
from .views import *

urlpatterns = [
    path('favorite/<int:id>/',add_favorite,name='favorite'),
    path('favorite/',favorite,name='fav'),
    path('delete_favorite/<int:id>/',delete_favorite,name='delete_favorite'),
    path('checkout/product/<int:id>/',checkout,name='checkout'),
    path('create_order/product/<int:id>/',create_order,name='create_order'),
    path('orders/',order_list,name='orders'),

]
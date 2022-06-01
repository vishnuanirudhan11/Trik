from django.urls import path
from .import views

urlpatterns=[
    path('cartlist/',views.cart,name='cart'),
    path('add/<int:prod_id>/',views.add,name='add'),
    path('minus/<int:prod_id>/',views.minus,name='minus'),
    path('delete/<int:prod_id>/',views.delete,name='delete'),
    path('checkout/',views.checkout,name='buyout')
]
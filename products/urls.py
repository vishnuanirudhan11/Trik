from django.urls import path
from.import views


urlpatterns=[
    path('',views.home,name='home'),
    path('catg/<slug:ct_slug>',views.catg,name='catg'),
    path('search/',views.search,name='search'),
    path('details/<int:id>/',views.details,name='details'),
    path('recent_ord/<date>/',views.details_ord,name='recent_ord')
]
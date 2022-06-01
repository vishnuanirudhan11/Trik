from django.urls import path
from.import views
urlpatterns=[
    path('comment/<int:ids>',views.cmmt,name="comment"),
    path('mssg/',views.msg,name="mssg"),
    path('msgtrik/<int:id>',views.msgtrik,name="msgtrik"),
    path('msgtrik/<int:id>/<str:true>',views.msgtrik,name="msgtrik"),
    path('deletemsg/',views.deletemsg,name="deletemsg")
]
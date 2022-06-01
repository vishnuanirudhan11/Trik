from django.urls import path
from.import views



urlpatterns=[
    path('api/rest/<int:year>/<int:month>',views.chart_data.as_view(),name='api_view'),
    path('api/rest/<int:year>', views.chart_data.as_view(), name='api_view'),
    path('detail/<int:id>',views.detail,name='ord_detail'),
    path('ord_process/<int:id>/<str:comd>',views.ord_process,name='ord_process'),
    path('msg_detail/<int:id>',views.msg_view,name='msg_details'),
    path('admin_home/',views.admin_home,name='admin_home'),
    path('htmlfile/',views.htmlfile,name='htmlfile'),
    path('post_details/<int:id>',views.post_detail,name='post_detail'),
]
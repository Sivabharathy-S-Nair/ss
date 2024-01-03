from django.urls import path

from  . import views
app_name='storeapp'
urlpatterns = [

    path('',views.index,name='index'),
    path('buttonpage',views.buttonpage,name='buttonpage'),
    path('newpage',views.newpage,name='newpage'),
    path('ordered',views.order,name='order'),
    path('computerscience',views.computerscience,name='computerscience'),
    path('commerce',views.commerce,name='commerce'),
    path('humanities',views.humanities,name='humanities'),
    path('physics',views.physics,name='physics'),
    path('mathematics',views.mathematics,name='mathematics'),
    ]

from django.urls import path
from kjp_app import views

app_name = 'kjp_app'

urlpatterns = [
        path('add_clients',views.add_clients,name='add_clients'),
        path('view_clients',views.view_clients,name='view_clients'),
]

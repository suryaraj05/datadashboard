from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload_file, name='upload_file'),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('filtered-data/',views.filtered_data,name='filtered_data'),
]   

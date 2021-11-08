from django.urls import path
from . import views
urlpatterns = [
    path('', views.add_show, name='addshow'),
    path('delete/<int:id>/', views.delete_data, name='deletedata'),
    path('<int:update_id>/', views.update_show, name='updateshow'),
  
]

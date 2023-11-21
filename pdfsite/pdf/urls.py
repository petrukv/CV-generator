from django.urls import path
from pdf import views

urlpatterns = [
    path('', views.accept, name='accept'),
    path('<int:id>/', views.resume, name='resume'),
    path('list/',views.list,name="list"),
]

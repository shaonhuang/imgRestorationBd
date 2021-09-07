from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload),
    path("getlist/", views.getFileList),
    path('info/<int:id>/', views.getInfo),
    path('getfile/<str:type>/<int:id>/', views.getFile),
    path('123', views.test)
]
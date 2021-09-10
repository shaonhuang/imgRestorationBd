from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload),
    path("getlist/", views.getFileList),
    path('info/<int:id>/', views.getInfo),
    path('getfile/byid/<str:type>/<int:id>/', views.getFileById),
    path('getfile/byname/<str:name>/', views.getFileByName),
    path('delete/byid/<int:id>/', views.deleteById),
    path('delete/byname/<str:name>/', views.deleteByName),
    path('check/byname/<str:name>/', views.checkDoneByName),
    path('123/', views.test)
]

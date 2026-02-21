from django.urls import path
from . import views

urlpatterns = [
    path('', views.index), 
     path('<int:bookId>', views.viewbook),
    path('index2/<int:val1>/', views.index2),
    path('index3/<int:val1>/<int:val2>/', views.index3),
]

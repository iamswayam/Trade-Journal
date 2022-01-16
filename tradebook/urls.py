from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signup/', views.SignupPage, name="signup"),
    # path('signin/', views.SigninPage, name="signin"),
    
    # path('newnote/', views.newnote, name="newnote"),
    #     path('delete/<stock_id>', views.delete, name="delete"),
    #     path('delete_stock.html', views.delete_stock, name="delete_stock"),
]

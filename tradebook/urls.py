from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signup/', views.SignupPage, name="signup"),
    path('login/', views.LoginPage, name="login"),
    path('logout/', views.logoutuser, name='logoutuser'),
    # path('q/', views.nse_data, name='q'),
    # path('newnote/', views.newnote, name="newnote"),
    #     path('delete/<stock_id>', views.delete, name="delete"),
    #     path('delete_stock.html', views.delete_stock, name="delete_stock"),
]

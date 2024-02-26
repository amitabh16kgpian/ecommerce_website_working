from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('login/', views.login_user, name ='login'),
    path('logout/', views.logout_user, name= 'logout'),
    path('register/', views.register_user, name = 'register'),
    path('view_product/<int:pk>', views.view_product, name = 'view_product'),
    path('view_by_category/<str:catg>', views.view_by_categories, name = 'view_by_category')
    
]


from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.models import User
urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_user, name="register"),
    path('update_password/', views.update_password, name="update_password"),
    path('update_user/', views.update_user, name="update_user"),
    path('update_info/', views.update_info, name="update_info"),
    path('product/<int:pk>/', views.product, name="product"),
    path('category/<str:var>', views.category, name="category"),
    path('category_summary/', views.category_summary, name="category_summary"),
    path('search/', views.search, name="search"),
    path('index/', views.index, name="index"),
    path('contact/', views.contact, name="contact"),
    path('contactinfo/', views.contactinfo, name="contactinfo"),
]


from . import views
from django . urls import path



urlpatterns = [
    path('', views.home, name='home'),
    path('book_appointment/', views.book_appointment, name='book_appointment'),
    path('login_view/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('logout_view/', views.logout_view, name='logout_view'),
    path('gallery/', views.gallery, name='gallery'),
    


]
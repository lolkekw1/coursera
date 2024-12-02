from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView 
from pages import views 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  
    path('about/', views.about, name='about'), 
    path('pages/', include('pages.urls')),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login_view, name='login'),
    path('logout-warning/', views.logout_warning, name='logout_warning'),
    path('confirm-logout/', views.confirm_logout, name='confirm_logout'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('sign-up/', views.sign_up, name='sign_up'),
]

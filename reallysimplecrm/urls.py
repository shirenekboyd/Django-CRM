from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
   
   # home page
   path('', views.home, name='home'),
#    path('login/', views.login_user, name='login'),
   path('logout/', views.logout_user, name='logout'),
   path('register/', views.register_user, name='register'),
   path('contact/<int:pk>/', views.contact_detail, name='contact_detail'),
   path('contacts/<int:pk>/delete/', views.contact_delete, name='contact_delete'),
   path('contacts/new/', views.contact_create, name='contact_create'),
]
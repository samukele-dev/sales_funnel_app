from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from .views import register, CustomLoginView

urlpatterns = [
    path('leads/', login_required(views.lead_list), name='lead_list'),
    path('', views.home, name='home'), # Add this line for the default redirect
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('create_lead/', views.create_lead, name='create_lead'),  # Add this line
    path('update_lead_status/<int:lead_id>/', views.update_lead_status, name='update_lead_status'),  # Add this line
    path('lead_detail/<int:lead_id>/', views.lead_detail, name='lead_detail'),  # Add this line
    path('delete/<int:lead_id>/', views.delete_lead, name='delete_lead'),

]

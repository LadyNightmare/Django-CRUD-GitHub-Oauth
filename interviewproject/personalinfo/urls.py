from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path('logout/', views.logout, name='logout'),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('', TemplateView.as_view(template_name='personalinfo/home.html'), name="home"),
    path('create_info/', views.create_info, name="create_info"),
    path('update_info/', views.update_info, name="update_info"),
    path('delete_info/', views.delete_info, name="delete_info"),
]

from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('', TemplateView.as_view(template_name='personalinfo/home.html'), name="home"),
]

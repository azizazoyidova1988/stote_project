from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('teams/', views.teams, name='team'),
    path('project/', views.project, name='project'),
    path('project/<int:project_id>/project_single/', views.project_single, name='project_single'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:news_id>/blog_single/', views.blog_single, name='blog_single'),
    path('contact/', views.contact, name='contact'),
    # path('dashboard/', include('dashboard.urls'))
]

from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.homepage_view, name="homepage_view"),
    path("contact/", views.contact_view, name="contact_view"),
    path("blog/", views.blog_view, name="blog_view"),
    path("blog/<str:slug>/", views.blog_detail, name="blog_detail"),
    path("projects/", views.projects_view, name="projects_view"),
    path("projects/<str:slug>/", views.project_detail, name="project_detail"),
]

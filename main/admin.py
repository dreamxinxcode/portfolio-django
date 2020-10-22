from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models
from blog.models import BlogPost
from projects.models import Project
from . models import Homepage
# Register your models here.


class BlogPostAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Title/date", {"fields": ["blog_title", "blog_date"]}),
        ("URL", {"fields": ["slug"]}),
        ("Content", {"fields": ["blog_image", "blog_text"]})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }


class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Title/date", {"fields": ["project_title", "project_date"]}),
        ("URL", {"fields": ["slug"]}),
        ("Content", {"fields": ["project_image", "project_intro", "project_overview", "open_source", "project_github", "project_client",
                                "project_client_website", "project_client_industry", "project_featured"]})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }


admin.site.register(Homepage)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Project, ProjectAdmin)

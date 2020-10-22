from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseNotFound
from django.utils import timezone
from . models import Homepage
from blog.models import BlogPost
from projects.models import Project
from django.conf import settings
# Create your views here.

# For Footer
blog_footer = BlogPost.objects.all()[0:6]
projects_footer = Project.objects.filter(project_featured=True)[0:6]


def homepage_view(request):
    context = {
        "title": "Dream in Code | Home",
        "description": "",
        "homepage": Homepage.objects.first(),
        "blog_home": BlogPost.objects.all()[0:6],
        "projects_home": Project.objects.filter(project_featured=True).order_by('-project_date')[0:6],
        "blog_footer": blog_footer,
        "projects_footer": projects_footer,
    }
    return render(request, "main/index.html", context)


def blog_view(request):
    context = {
        "title": "Dream in Code | Blog",
        "description": "",
        "blog_footer": blog_footer,
        "projects_footer": projects_footer,
        "blog": BlogPost.objects.filter(blog_date__lte=timezone.now()).order_by('-blog_date')
    }
    return render(request, "main/blog.html", context)


def blog_detail(request, slug):
    try:
        blog = BlogPost.objects.get(slug=slug)
        context = {
            "title": "Dream in Code | %s" % blog.blog_title,
            "description": "",
            "blog_footer": blog_footer,
            "projects_footer": projects_footer,
            "blog": BlogPost.objects.get(slug=slug),
        }
    except BlogPost.DoesNotExist:
        return HttpResponseNotFound()
    return render(request, 'main/blog_detail.html', context)


def projects_view(request):
    context = {
        "title": "Dream in Code | Projects",
        "description": "",
        "blog_footer": blog_footer,
        "projects_footer": projects_footer,
        "projects": Project.objects.filter(project_date__lte=timezone.now()).order_by('-project_date'),
    }
    return render(request, "main/projects.html", context)


def project_detail(request, slug):
    try:
        project = Project.objects.get(slug=slug)
        context = {
            "title": "Dream in Code | %s" % project.project_title,
            "description": "",
            "blog_footer": blog_footer,
            "projects_footer": projects_footer,
            "project": project,

        }
    except Project.DoesNotExist:
        return HttpResponseNotFound()
    return render(request, 'main/project_detail.html', context)


def contact_view(request):
    subject = str(request.POST.get("subject"))
    name = str(request.POST.get("name"))
    email = request.POST.get("email")
    message = str(request.POST.get("message")) + "\n\n" + \
        "Name: " + str(name) + "\n" + "Email: " + str(email)
    if request.method == "POST":
        send_mail(subject, message, settings.EMAIL_HOST_USER,
                  ['brandon@dreamincode.dev'], fail_silently=False)
        redirect("main:homepage_view")
    context = {
        "title": "Dream in Code | Contact",
        "description": "",
        "blog_footer": blog_footer,
        "projects_footer": projects_footer,
    }
    return render(request, "main/contact.html", context)


def services_view(request):
    context = {
        "title": "Dream in Code | Services",
        "description": "",
        "blog_footer": blog_footer,
        "projects_footer": projects_footer,
    }
    return render(request, "main/services.html", context)

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def contact(request):
    return render(request, "contact.html")

def articles(request):
    return render(request, "articles.html")

def article(request):
    return render(request, "article.html")

def sitemap(request):
    return render(request, "sitemap.html")

def abouts(request):
    return render(request, "abouts.html")
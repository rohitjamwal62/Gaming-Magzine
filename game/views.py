from django.shortcuts import render, redirect, render_to_response
from django.shortcuts import render



from .models import SearchQuery


from .models import User

def home(request):

    return render(request, "index.html")



def contact(request):
    return render(request, "contact.html")



def about(request):
    return render(request, "about.html")

def single(request):
    return render(request, "single.html")



def games(request):
    return render(request, "games.html")



def review(request):
    return render(request, "review.html")


def blog(request):
    return render(request, "blog.html")





def search(request):
    query = request.GET.get('q', None)
    user = None
    if request.user.is_authenticated:
        user = request.user
    context =  {"query": query}
    if query is not None:
        SearchQuery.objects.create(user=user, query=query)
        blog_list = BlogPost.objects.search(query=query)
        context['blog_list'] = blog_list
    return render(request, 'search.html')
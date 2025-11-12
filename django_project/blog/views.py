from django.shortcuts import render

# Create your views here.

posts = [
    {
        'author': 'Corey',
        'title': 'My First Post',
        'content': 'My First Post',
        'date_posted': 'Nov 12, 2025',
    },
    {
        'author': 'John Doe',
        'title': 'My Second Post',
        'content': 'My Second Post',
        'date_posted': 'Nov 13, 2025',
    }
]
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html',{'title':'About'})
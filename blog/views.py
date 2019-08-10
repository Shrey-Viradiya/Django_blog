from django.shortcuts import render
# from django.http import HttpResponse

posts = [
    {
        'author' : 'Shrey Viradiya',
        'title' : 'Django is Cool',
        'content' : 'I am using Django',
        'date_posted' : '10 August, 2019'
    },
    {
        'author' : 'Betty Cooper',
        'title' : 'Riverdale',
        'content' : 'Where is blackhood?',
        'date_posted' : '11 August, 2019'
    }

]


def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html',{'title' : 'About'})
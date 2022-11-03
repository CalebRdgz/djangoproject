from django.shortcuts import render

posts = [
    {
        "author": "Caleb",
        "title": "Blog post 1",
        "content": "First post",
        "date_posted": "August",
    },
    {
        "author": "Ash",
        "title": "Blog post 2",
        "content": "Second post",
        "date_posted": "September",
    },
]

# Create your views here.
def home(request):
    context = {"posts": posts}
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {"title": "About"})

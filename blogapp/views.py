from django.shortcuts import render
from blogapp.models import Post

# Create your views here.
def post_list(request):
    # post1 = Post(
    #     title = "Python",
    #     contend = "dfghuijopsdfghhjj",
    # )
    # post1.save()
    posts = Post.objects.all()
    context={
        "posts": posts,
    }
    return render(request, 'blogapp/post_list.html', context=context)

from django.shortcuts import render
from app.models import Post
# Create your views here.


def all_posts(request):
    posts = Post.object.all()

    context = {
       "all_posts": all_posts

   }
    return render(
        request,
        template_name="app/all_poducts.html",
        context=context, 

    )
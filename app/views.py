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
        template_name="app/post_list.html",
        context=context, 

    )


def page_post(request):
    post = Post.objects.get(id = post_id)

    context = {
       "post": post

   }
    return render(
        request,
        template_name="app/page_post.html",
        context=context, 

    )
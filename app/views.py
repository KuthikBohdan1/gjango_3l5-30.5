from django.shortcuts import render
from app.models import Post, User, Author
# Create your views here.


def all_posts(request):

    posts = Post.objects.all()
    # posts = "hi from posts"  # Тимчасове значення для перевірки
    context = {
        "all_posts": posts  # Виправлено форматування
    }
    return render(
        request,
        template_name="page_post.html",
        context=context,
    )


def users(request):
    users = User.objects.all()
    context = {

        "all_users" : users
    }
    return render(
        request,
        template_name="users_info_test.html",
        context=context,

    )

# def page_post(request, post_id):
#     post = Post.objects.get(id = post_id)

#     context = {
#        "post": post

#    }
#     return render(
#         request,
#         template_name="app/page_post.html",
#         context=context

#     )


# def page_author(request, post_id):
#     post = Post.objects.get(id = post_id)

#     context = {
#        "author": author_post,

#    }
#     return render(
#         request,
#         template_name="app/page_post.html",
#         context=context

#     )
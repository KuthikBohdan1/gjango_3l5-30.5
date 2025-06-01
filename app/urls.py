from django.contrib import admin
from django.urls import path, include
from app.views import all_posts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', all_posts, name='all_posts'),
]

from django.urls import path
import post.views as post_list


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', post)
    path('post-page/<int:post_id>', page_post, name = 'page_post')
]





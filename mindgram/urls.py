#Mindgram URLs module

#Django
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


from mindgram import views as local_views
from posts import views as posts_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('holis', local_views.hello_world),
    path('hi/<str:name>/<int:age>/', local_views.say_hi),

    path('posts/', posts_views.list_posts),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
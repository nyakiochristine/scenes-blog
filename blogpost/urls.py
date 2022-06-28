from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from blogpost.views import PostList,PostDetail
from .views import PostList,PostDetail
from . import views

urlpatterns = [
    path('blog/', views.PostList.as_view(), name='home'),
    path('postdetail/<int:pk>', views.PostDetail.as_view(), name='post_detail'),
    path('postComment/',views.postComment,name='postComment'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


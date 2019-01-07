from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('about/',views.blog_about, name='blog-about'),
    path('blog/<int:pk>/', PostDetailView.as_view(), name ='post-detail'),
    path('blog/new', PostCreateView.as_view(), name='post-create'),
    path('blog/<int:pk>/update/', PostUpdateView.as_view(), name ='post-update'),
    path('blog/<int:pk>/delete/', PostDeleteView.as_view(), name ='post-delete')
]

from django.urls import path
from .views import list_view, detail_view

urlpatterns = [
    path('', list_view, name="blog_index"),
    path(r'^posts/<int:post_id>/', detail_view, name="blog_detail"),
]
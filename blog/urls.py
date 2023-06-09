from django.urls import path
from blog.views import post_list, post_details, PostListView, post_share, post_comment

app_name = 'blog'
urlpatterns = [
    path('list/', post_list, name="post"),
    path('comment/<int:pk>/', post_comment, name='comment'),
    # path('list/', PostListView.as_view(), name="post"),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', post_details, name="post_detail"),
    path('<int:post_id>/share/', post_share, name='post_share'), ]

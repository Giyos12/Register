from django.urls import path
from blog.views import post_list, post_details

app_name = 'blog'
urlpatterns = [
    path('list/', post_list, name="post"),
    path('detail/<int:pk>', post_details, name="post_detail"),
]

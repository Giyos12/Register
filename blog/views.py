from django.http import Http404
from django.shortcuts import render, get_object_or_404

from blog.models import Post


# Create your views here.
def post_list(request):
    posts = Post.published.all()
    print(posts)
    return render(request, 'blog/post/list.html', {'posts': posts})


def post_details(request, pk):
    # 1- usha malumot db da bomasa 404
    # db da shu id lik malumot kop bolasa
    # post = Post.published.filter(id=pk).first()
    try:
        post = Post.published.get(id=pk)
    except Post.DoesNotExist:
        raise Http404("No Post found")
    return render(request, 'blog/post/detail.html', {'post': post})

from django.shortcuts import render

from blog.models import Post


# Create your views here.
def post_list(request):
    posts = Post.published.all()
    print(posts)
    return render(request, 'blog/post/list.html', {'posts': posts})


def post_details(request, pk):
    # 1- usha malumot db da bomasa 404
    # db da shu id lik malumot kop bolasa
    post = Post.published.filter(id=pk).first()
    return render(request, 'blog/post/detail.html', {'post': post})

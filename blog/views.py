from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404

from auth2.forms import EmailPostForm
from blog.models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView


# Create your views here.
def post_list(request):
    posts = Post.published.all()
    p = Paginator(posts, 2)
    page_number = request.GET.get('page')
    try:
        posts = p.page(page_number)
    except PageNotAnInteger:
        posts = p.page(1)
    except EmptyPage:
        posts = p.page(p.num_pages)
    return render(request, 'blog/post/list.html', {'posts': posts})


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 2
    template_name = 'blog/post/list.html'


def post_details(request, year, month, day, post):
    # 1- usha malumot db da bomasa 404
    # db da shu id lik malumot kop bolasa
    post = get_object_or_404(Post, status="PB",
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})


def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status="PB")
    sent = False

    if request.method == "POST":
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # send email
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f'{cd["name"]} recommend you read' \
                      f'{post.title}'
            message = f' read {post.title} at {post_url}\n\n'
            send_mail(subject, message, 'giyosoripov5@gmail.com', ['giyosoripov5@gmail.com'], fail_silently=False)
            sent = True
        else:
            return render(request, 'blog/post/share.html', {'post': post, 'form': form})
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'post': post, 'form': form, 'sent': sent})

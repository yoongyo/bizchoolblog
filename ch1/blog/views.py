from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
from .models import Post, Category
from .forms import PostForm


category_list = ListView.as_view(model=Category)

def post_list(request, name):
    qs = Post.objects.all()
    qs1 = Category.objects.all()

    path = request.path
    filter = path.split('/')[2]
    print(filter)

    qs = qs.filter(category__name=filter)
    return render(request, 'blog/post_list.html', {
        'category_list': qs1,
        'post_list': qs,
        'filter': filter
    })


def post_detail(request, name, id):
    get_object_or_404(Post, id=id)
    qs1 = Category.objects.all()
    q = request.GET.get('q', '')
    if q:
        qs1 = qs1.filter(content__icontains=q)
    post = Post.objects.get(id=id)
    return render(request, 'blog/post_detail.html', {
        'post': post,
        'category_list': qs1,
    })


def post_new(request):
     if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect(post)      # post.get_absolute_url() =>  post detail
     else:
        form = PostForm()
     return render(request, 'blog/post_form.html', {
     'form': form,
     })


def post_edit(request, name, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect(post)         # post.get_absolute_url() =>  post detail
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {
        'form': form,
    })

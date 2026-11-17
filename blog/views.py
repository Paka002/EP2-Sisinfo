from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .forms import PostForm
from .models import Post


def post_list(request):
    return render(request, "blog/post_list.html", {"posts": Post.objects.all()})


def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist as exc:
        raise Http404("Post não encontrado.") from exc
    return render(request, "blog/post_detail.html", {"post": post})


def post_create(request):
    form = PostForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        post = form.save()
        return HttpResponseRedirect(reverse("blog:post_detail", args=[post.pk]))
    return render(request, "blog/post_form.html", {"action": "Criar", "form": form})


def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, instance=post)
    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("blog:post_detail", args=[post.pk]))
    return render(request, "blog/post_form.html", {"post": post, "action": "Editar", "form": form})


def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return HttpResponseRedirect(reverse("blog:post_list"))
    return render(request, "blog/post_confirm_delete.html", {"post": post})

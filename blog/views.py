from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import PostForm
from .models import Post


class PostListView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "blog/post_list.html"


class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"
    template_name = "blog/post_detail.html"


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"
    extra_context = {"action": "Criar"}

    def get_success_url(self):
        return reverse_lazy("blog:post_detail", kwargs={"pk": self.object.pk})


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    context_object_name = "post"
    template_name = "blog/post_form.html"
    extra_context = {"action": "Editar"}

    def get_success_url(self):
        return reverse_lazy("blog:post_detail", kwargs={"pk": self.object.pk})


class PostDeleteView(DeleteView):
    model = Post
    context_object_name = "post"
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("blog:post_list")

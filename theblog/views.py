from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import PostForm, EditForm
from .models import Post, Category


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats)
    context = {
        'cats': cats.title(),
        'category_posts': category_posts
    }
    return render(request, 'theblog/categories.html', context)


class HomeView(ListView):
    model = Post
    template_name = "theblog/home.html"
    ordering = ['-id']


class ArticleDetailView(DetailView):
    model = Post
    template_name = "theblog/article_details.html"


"""
Jika kita menggunakan form_class maka tidak perlu lagi fields
"""


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'theblog/add_post.html'
    # fields = '__all__'


class AddCategoryView(CreateView):
    model = Category
    # form_class = PostForm
    template_name = 'theblog/add_category.html'
    fields = '__all__'


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'theblog/update_post.html'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'theblog/delete_post.html'
    success_url = reverse_lazy('home')

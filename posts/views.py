from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import Postform, Editform
from django.urls import reverse_lazy
from .models import Post, category


class Homeview(ListView):
    model = Post
    template_name = "home.html"
    ordering = ['-post_date']


class Articleview(DetailView):
    model = Post
    template_name = "article.html"


class Addview(CreateView):
    model = Post
    template_name = "add_post.html"
    form_class = Postform


class Categoryview(CreateView):
    model= category
    template_name="add_category.html"
    fields= '__all__'

class Updateview(UpdateView):
    model = Post
    template_name = "edit_post.html"
    form_class = Editform


class Deleteview(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy('home')


def Category_view(request , cats):
    category_post = Post.objects.filter(category=cats) # filters category to those which matched
    return render(request, 'categories.html' , {'cats':cats, 'category_post': category_post} )

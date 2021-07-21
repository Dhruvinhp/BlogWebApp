from django.shortcuts import render
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blogApp/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blogApp/home.html'
    # <app>/<model>_<viewtype>.html in our case its looking for blogApp/post_list.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView): #here we use Detail View
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView): #here we use Create View
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): #here we use update View
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): #here we use Delete View
    model = Post
    success_url = '/' 

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'blogApp/about.html', {'title': 'About'})     

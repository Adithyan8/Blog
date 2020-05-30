from django.shortcuts import render,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)
from .models import Post
# Create your views here.   

class PostListView(ListView):
    model = Post
    template_name='blog/home.html'
    context_object_name='posts'     #variable to be used in templates(variable that has all posts)
    ordering = ['-date_posted']     #orders according to date_posted. date_posted - oldest to newest
    paginate_by=4                                # -date_posted - newest to oldest    
                                    #We cant use login decorators on classes only function. So we use Mixin for classes
class PostDetailView(DetailView):
    model = Post
    
class UserPostListView(ListView):
    model = Post
    template_name='blog/user_posts.html'
    context_object_name='posts'
    paginate_by=5
    
    def get_queryset(self):
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        postuser = Post.objects.filter(author=user).first()
        return Post.objects.filter(author=user).order_by('-date_posted')
        
class PostCreateView(LoginRequiredMixin,CreateView):          
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):           #So we use Mixin for classes
    model = Post                    #UserPassesTestMixinhelps to checkif user and author are the same while editing a post.
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)    
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author :
            return True
        return False    

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

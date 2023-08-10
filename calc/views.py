
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post,Category, Comment
from .forms import PostForm, UpdateForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth import get_user
from django.http import HttpResponseRedirect


# Create your views here.

# def home(request):
#     return render(request, 'home.html')

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']   
    
    def get_context_data(self, *args, **kwargs):
        pet_menu = Category.objects.all()
        context = super(HomeView,self).get_context_data(*args, **kwargs)
        context["pet_menu"] = pet_menu
        return context
        

def CategoryView(request, pets):
    category_posts = Post.objects.filter(category=pets)
    return render(request, 'categoris.html', {'pets': pets.title(), 'category_posts':category_posts})

def CategoryListView(request):
    pet_menu_list = Category.objects.all()
    return render(request, 'category_list.html', {'pet_menu_list':pet_menu_list})

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
         post.likes.remove(request.user)
         liked = False
    else:    
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('details', args=[str(pk)]))

    

class DetailsView(DetailView):  
    model = Post
    template_name = 'details.html'

    def get_context_data(self, *args, **kwargs):
        pet_menu = Category.objects.all()
        context = super(DetailsView,self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
            
        context["pet_menu"] = pet_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context 

class AddCategoryView(CreateView):
    model = Category
    template_name = 'category.html'
    
    fields = ['name']
        


class AddCreateView(CreateView):
    model = Post
    template_name = 'create.html'
    form_class = PostForm
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class AddCommentView(CreateView):
    model = Comment
    form_calss = CommentForm
    template_name = 'add_comment.html'
    fields = ['name', 'body']
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('home')
    
    

    

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'update.html'
    form_calss = UpdateForm
    fields = ['title', 'body']  
    


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('home')     
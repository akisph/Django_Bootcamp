from django.shortcuts import render,get_object_or_404, redirect
# get_object_or_404 : 
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
from django.contrib.auth.decorators import login_required # login_required decorator
from django.contrib.auth.mixins import LoginRequiredMixin # if we also inherit from this class the login required fro this view
from django.urls import reverse_lazy


from django.utils import timezone

from blog.forms import PostForm, CommentForm
from blog.models import Post, Comment

# Create your views here.

class AboutView(TemplateView):
    """ This is the about page """
    template_name  = 'about.html'

class PostListView(ListView):
    """ This is the HOME PAGE, which is a List view for all the post """
    model  = Post    # Connect list view to a model.
    # In this case is the Post Model
    # THis allows to use the django query set (ORM)
    def get_queryset(self):
        """ This says which objects i want to return and how """
        # In this example we return the whole list but ordered by published date
        ## SELECT * FROM Post WHERE published_date < timezone.now() 
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date') # __lte: less than or equals to

        

class PostDetailView(DetailView):
    """ This is a detailed view of each post """
    model = Post 

class CreatePostView(CreateView, LoginRequiredMixin):
    """ This is a view to create a new Post """
    
    # for the login required mixin
    login_url = '/login/'
    redirect_field  = 'blog/post_detail.html' # where to redirect
    # ------------------------- #
    form_class  = PostForm
    model = Post    

class PostUpdateView(LoginRequiredMixin,UpdateView):

    """ This is a view to update a  Post """    
    # for the login required mixin
    login_url = '/login/'
    redirect_field  = 'blog/post_detail.html' # where to redirect
    # ------------------------- #
    form_class  = PostForm
    model = Post

class PostDeleteView(LoginRequiredMixin,DeleteView):
    """ View handling the delete of a post """

    # for the login required mixin
    login_url = '/login/'
    redirect_field  = 'blog/post_detail.html' # where to redirect
    # ------------------------- #
    model = Post
    success_url =  reverse_lazy('post_list')  

class DraftListView(LoginRequiredMixin,ListView):
    """ this is a list view for all the drafted posts """

    # for the login required mixin
    login_url = '/login/'
    redirect_field  = 'blog/post_list.html' # where to redirect
    # ------------------------- #
    model  = Post    # Connect list view to a model.
    # In this case is the Post Model
    # THis allows to use the django query set (ORM)

    def get_queryset(self):
        """ This says which objects i want to return and how """

        # In this example we return the whole list but ordered by published date
        return Post.objects.filter(published_date__isnull=True).order_by('create_date') # this returns all the unpublished posts


#########################################################
##########################################################
@login_required
def post_publish(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_detail',pk=pk)

@login_required
def add_comment_to_post(request,pk):
    """ This function allows to add a comment to a post """

    post = get_object_or_404(Post,pk=pk) # this functions retrieve a post based on the primary key
    # in case of error returns 404 http response

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment  = form.save(commit=False) # Do not commit yet 
            comment.post = post # We nned to assign it to a post 
            comment.save()
            return redirect('post_detail', pk=post.pk) # This page needs a priomary key 
    else:
        form = CommentForm()

    return render(request,  'blog/comment_form.html',{'form' : form} )           

@login_required
def comment_approve(request,pk):
    comment  = get_object_or_404(Comment,pk=pk)
    comment.approve()   
    redirect('post_detail',pk = comment.post.pk)

@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk=post_pk)

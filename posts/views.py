'''Posts views'''

#Django
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

#Forms
from posts.forms import PostForm

#Models
from posts.models import Post


#Return all pubished posts
class PostsFeedView(LoginRequiredMixin, ListView):
    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created',)
    paginate_by = 2
    context_object_name = 'posts'


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        #if the data is valid create the post
        if form.is_valid():
            form.save()
        
            return redirect('posts:feed')
    #if the method is not post, sends an empty form instance 
    else:
        form = PostForm()
    
    return render(
        request = request,
        template_name= 'posts/new.html',
        context= {
            'form': form, 
            'user': request.user,
            'profile': request.user.profile
        }
    )
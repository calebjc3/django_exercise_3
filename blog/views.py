from django.views import generic
from django.urls import reverse_lazy
from .models import Post
from django.contrib.auth.models import User

admin = User.objects.get(username='admin')
me = User.objects.get(username='cjc')

class IndexView(generic.ListView):
  template_name = 'blog/index.html'
  context_object_name = 'post_list'

  def get_queryset(self):
    """Return all the posts."""
    return Post.objects.all()

class CreateView(generic.edit.CreateView):
  template_name = 'blog/create.html'
  model = Post
  fields = ['author', 'title', 'text', 'created_date', 'published_date']
  success_url = reverse_lazy('blog:index')

class UpdateView(generic.edit.UpdateView):
  template_name = 'blog/update.html'
  model = Post
  fields = ['author', 'title', 'text', 'created_date', 'published_date']
  success_url = reverse_lazy('blog:index')

class DeleteView(generic.edit.DeleteView):
  template_name = 'blog/delete.html'
  model = Post
  success_url = reverse_lazy('blog:index')

class FilteredView(generic.ListView):
  template_name = 'blog/filtered.html'
  context_object_name = 'post_list'

  def get_queryset(self):
    """Return filtered posts."""
    return Post.objects.filter(author=admin)

class OrderedView(generic.ListView):
  template_name = 'blog/ordered.html'
  context_object_name = 'post_list'

  def get_queryset(self):
    """Return ordered posts."""
    return Post.objects.order_by('created_date')

class FilteredOrderedView(generic.ListView):
  template_name = 'blog/filteredordered.html'
  context_object_name = 'post_list'
  
  def get_queryset(self):
    """Return filtered and ordered posts."""
    return Post.objects.filter(author=admin).order_by('created_date')


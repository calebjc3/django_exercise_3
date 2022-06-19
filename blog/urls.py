from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
  path('', views.IndexView.as_view(), name='index'),
  path('new', views.CreateView.as_view(), name='create'),
  path('update/<int:pk>', views.UpdateView.as_view(), name='update'),
  path('delete/<int:pk>', views.DeleteView.as_view(), name='delete'),
  path('filter', views.FilteredView.as_view(), name='filter'),
  path('order', views.OrderedView.as_view(), name='order'),
  path('filterorder', views.FilteredOrderedView.as_view(), name='filterorder'),
]
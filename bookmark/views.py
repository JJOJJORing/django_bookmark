from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import Bookmark
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from .serializers import BookmarkSerializer


class ApiBookmarkList(ListAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer


class ApiBookmarkDetail(RetrieveUpdateDestroyAPIView):
   queryset = Bookmark.objects.all()
   serializer_class = BookmarkSerializer


# Create your views here.
class BookmarkListView(ListView):
    model = Bookmark
    paginate_by = 3

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('list')

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')

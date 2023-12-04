# views.py
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Product, BlogPost
from .forms import BlogPostForm


class HomeView(TemplateView):
    template_name = 'main/home.html'


class IndexView(ListView):
    model = Product
    template_name = 'main/index.html'
    context_object_name = 'products'
    queryset = Product.objects.all().order_by('-pk')[:5]


class ContactsView(TemplateView):
    template_name = 'main/contacts.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'


class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blog/post_list.html'


class BlogPostCreateView(CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blog/post_create.html'
    success_url = reverse_lazy('blog:post_list')


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blog/post_update.html'
    success_url = reverse_lazy('blog:post_list')


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('blog:post_list')

# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Product
from .models import BlogPost
from .forms import BlogPostForm


class HomeView(View):
    def get(self, request):
        return render(request, 'main/home.html')


class IndexView(View):
    def get(self, request):
        products = Product.objects.all().order_by('-pk')[:5]
        return render(request, 'main/index.html', {'products': products})


class ContactsView(View):
    def get(self, request):
        return render(request, 'main/contacts.html')

    def post(self, request):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        print(f"{name} - {phone} - {message}")

        return render(request, 'main/contacts.html')


class ProductDetailView(View):
    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        return render(request, 'product_detail.html', {'product': product})


class BlogPostListView(View):
    def get(self, request):
        blog_posts = BlogPost.objects.all()
        return render(request, 'blog/post_list.html', {'blog_posts': blog_posts})


class BlogPostCreateView(View):
    def get(self, request):
        form = BlogPostForm()
        return render(request, 'blog/post_create.html', {'form': form})

    def post(self, request):
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog:post_list')
        return render(request, 'blog/post_create.html', {'form': form})


class BlogPostUpdateView(View):
    def get(self, request, slug):
        blog_post = get_object_or_404(BlogPost, slug=slug)
        form = BlogPostForm(instance=blog_post)
        return render(request, 'blog/post_update.html', {'form': form, 'blog_post': blog_post})

    def post(self, request, slug):
        blog_post = get_object_or_404(BlogPost, slug=slug)
        form = BlogPostForm(request.POST, request.FILES, instance=blog_post)
        if form.is_valid():
            form.save()
            return redirect('blog:post_list')
        return render(request, 'blog/post_update.html', {'form': form, 'blog_post': blog_post})


class BlogPostDeleteView(View):
    def get(self, request, slug):
        blog_post = get_object_or_404(BlogPost, slug=slug)
        return render(request, 'blog/post_delete.html', {'blog_post': blog_post})

    def post(self, request, slug):
        blog_post = get_object_or_404(BlogPost, slug=slug)
        blog_post.delete()
        return redirect('blog:post_list')
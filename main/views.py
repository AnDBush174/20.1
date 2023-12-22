# views.py
from django.core.mail import send_mail
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import BlogPost, Product, Version
from .forms import BlogPostForm, ProductForm, VersionForm, ContactForm
from django.shortcuts import render, redirect, get_object_or_404


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # process the form data and perform necessary actions
            # for example, send an email using the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # perform additional actions as needed
    else:
        form = ContactForm()

    return render(request, 'contacts.html', {'form': form})


def create_version(request):
    if request.method == 'POST':
        form = VersionForm(request.POST)
        if form.is_valid():
            form.save()
            # Реализуйте нужную логику после сохранения формы
    else:
        form = VersionForm()
    return render(request, 'create_version.html', {'form': form})


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'create_product.html', {'form': form})


def product_list(request):
    products = Product.objects.all()
    active_versions = Version.objects.filter(is_current_version=True)
    active_products = [version.product for version in active_versions]
    return render(request, 'product_list.html', {'products': products}, {'active_products': active_products})


def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'update_product.html', {'form': form})


def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'delete_product.html', {'product': product})


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


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'main/post_detail.html'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.view_count += 1
        obj.save()
        if obj.view_count == 1:
            send_mail(
                'Уведомление о просмотрах',
                f'Ваш блог {obj.title} был просмотрен {obj.view_count} раз',
                'from@example.com',
                ['to@example.com'],
                fail_silently=False,
            )
        return obj


class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'main/post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']

    def get_queryset(self):
        return BlogPost.objects.filter(is_published=True)


class BlogPostCreateView(CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'main/post_create.html'

    def get_success_url(self):
        return reverse('main:post_detail', kwargs={'slug': self.object.slug})


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    form_class = BlogPostForm

    def get_success_url(self):
        return reverse('main:post_detail', kwargs={'slug': self.object.slug})


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'main/post_delete.html'
    success_url = reverse_lazy('main:post_list')


def send_test_email(request):
    send_mail(
        'Добро пожаловать в наше сообщество!',
        'Рады видеть вас здесь!',
        'from@example.com',
        ['thestudybox@mail.ru'],
        fail_silently=False,
    )
    return HttpResponse('Test email sent.')

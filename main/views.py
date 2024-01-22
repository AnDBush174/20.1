# main/views.py
from django.core.mail import send_mail
from django.http import HttpResponse
from django.views.decorators.cache import cache_page
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from .models import Product, Version, BlogPost
from .forms import ProductForm, VersionForm, ContactForm, BlogPostForm
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse
from django.contrib.auth.decorators import login_required


class ContactView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'contacts.html', {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            # Обработка данных формы и выполнение необходимых действий
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Выполнение дополнительных действий по необходимости
        return render(request, 'contacts.html', {'form': form})


class CreateVersionView(View):
    def get(self, request):
        form = VersionForm()
        return render(request, 'create_version.html', {'form': form})

    def post(self, request):
        form = VersionForm(request.POST)
        if form.is_valid():
            form.save()
            # Реализуйте нужную логику после сохранения формы
        return render(request, 'create_version.html', {'form': form})


class CreateProductView(View):
    def get(self, request):
        form = ProductForm()
        return render(request, 'create_product.html', {'form': form})

    def post(self, request):
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
        return render(request, 'create_product.html', {'form': form})


@login_required
def product_list(request):
    products = Product.objects.all()
    active_versions = Version.objects.filter(is_current_version=True)
    active_products = [version.product for version in active_versions]
    return render(request, 'product_list.html', {'products': products, 'active_products': active_products})


class UpdateProductView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'update_product.html'
    success_url = reverse_lazy('product_list')


class DeleteProductView(DeleteView):
    model = Product
    template_name = 'delete_product.html'
    success_url = reverse_lazy('product_list')


class HomeView(TemplateView):
    template_name = 'main/home.html'


class IndexView(ListView):
    model = Product
    template_name = 'main/index.html'
    context_object_name = 'products'
    queryset = Product.objects.all().order_by('-pk')[:5]


class ContactsView(TemplateView):
    template_name = 'main/contacts.html'


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_update.html'
    success_url = reverse_lazy('product_list')


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

    def get_success_url(self):
        return reverse_lazy('main:post_list')


def send_test_email(request):
    send_mail(
        'Добро пожаловать в наше сообщество!',
        'Рады видеть вас здесь!',
        'from@example.com',
        ['thestudybox@mail.ru'],
        fail_silently=False,
    )
    return HttpResponse('Test email sent.')


@cache_page(60 * 15)  # Кеширование на 15 минут
def product_detail(request, product_id):
    product = Product.objects.get(pk=product_id)  # Получение объекта продукта по его идентификатору
    # Дополнительная логика для получения дополнительных данных о продукте, например, его версий, отзывов и т.д.

    return render(request, 'product_detail.html', {'product': product})

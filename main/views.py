# views.py
from django.core.mail import send_mail
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
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


class BlogPostDetailView(DetailView):
    model = BlogPost

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.view_count += 1
        obj.save()
        if obj.view_count == 1:
            send_mail(
                'Уведомление о просмотрах',
                'Ваш блог %s был просмотрен %s раз' % (obj.title, obj.view_count),
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


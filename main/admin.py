# main/admin.py
from django.contrib import admin
from django.core.mail import send_mail
from .models import Category, Product, Contacts
from django.contrib.auth.models import Group, Permission

admin.site.unregister(Group)  # Удаляем стандартную группу
admin.site.register(Group)  # Заменяем на свою


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description')


@admin.action(description='Send email to selected contacts')
def send_email_to_contacts(modeladmin, request, queryset):
    for contact in queryset:
        subject = 'Greetings from Django'
        message = f'Hello, {contact.name}. This is a test email.'
        from_email = 'from@example.com'
        recipient_list = ['thestudybox@mail.ru']
        send_mail(subject, message, from_email, recipient_list)
    modeladmin.message_user(request, 'Email sent successfully.')


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('pk', '__str__', 'country', 'inn', 'address')
    actions = [send_email_to_contacts]
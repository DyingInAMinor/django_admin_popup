from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import MyCustomModel



@admin.register(MyCustomModel)
class YourCustomModelAdmin(admin.ModelAdmin):
    change_form_template = 'admin/app/custom_change_form.html'
    list_display = ("my_custom_field", )  # Определите, какие поля будут отображаться в списке объектов
    list_filter = ('my_custom_field', )  # Добавьте фильтры справа
    search_fields = ('my_custom_field', )

from django.contrib import admin

from .models import Student



@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'birth_date', 'address')
    list_filter = ('user', 'phone')
    search_fields = ('full_name', 'phone', 'user')
    ordering = ('full_name',)


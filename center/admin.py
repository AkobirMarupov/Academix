from django.contrib import admin
from django.utils.html import format_html
from .models import Center, Teacher, Location



def avatar_preview(obj):
    if obj.avatar:
        return format_html(
            '<a href="{0}" target="_blank">'
            '<img src="{0}" width="40" height="40" style="border-radius:50%; object-fit:cover;" />'
            '</a>',
            obj.avatar.url
        )
    return "—"
avatar_preview.short_description = "Avatar"


def image_preview(obj):
    if obj.image:
        return format_html(
            '<a href="{0}" target="_blank">'
            '<img src="{0}" width="50" height="50" style="border-radius:5px; object-fit:cover;" />'
            '</a>',
            obj.image.url
        )
    return "—"
image_preview.short_description = "Rasm"




class TeacherInline(admin.TabularInline):
    model = Teacher
    extra = 1
    fields = ('first_name', 'last_name', 'subject', 'experience_years', 'age')
    readonly_fields = ('experience_years',)
    show_change_link = True


class LocationInline(admin.TabularInline):
    model = Location
    extra = 1
    fields = ('address', 'google_maps_link')
    show_change_link = True



@admin.register(Center)
class CenterAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'email', 'phone', 'telegram', 'subject',avatar_preview)
    search_fields = ('name', 'owner__username', 'email', 'phone')
    list_filter = ('owner', 'created_at')
    readonly_fields = ('created_at', 'updated_at', avatar_preview)
    inlines = [TeacherInline, LocationInline]

    fieldsets = (
        ('Asosiy malumotlar', {
            'fields': ('name', 'bio', 'owner', 'subject')
        }),
        ('Aloqa malumotlari', {
            'fields': ('phone', 'email', 'telegram')
        }),
        ('Rasm va tizim', {
            'fields': ('avatar', avatar_preview, 'created_at', 'updated_at')
        }),
    )

    ordering = ('-created_at',)
    list_per_page = 20


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'subject', 'center', 'experience_years', 'age', image_preview)
    list_filter = ('center', 'subject')
    search_fields = ('first_name', 'last_name', 'subject', 'center__name')
    readonly_fields = ('created_at', 'updated_at', image_preview)

    fieldsets = (
        ('Shaxsiy malumotlar', {
            'fields': ('first_name', 'last_name', 'age')
        }),
        ('Talim malumotlari', {
            'fields': ('subject', 'experience_years', 'center')
        }),
        ('Rasm va tizim', {
            'fields': ('image', image_preview, 'created_at', 'updated_at')
        }),
    )

    ordering = ('last_name',)
    list_per_page = 25


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'center', 'city', 'address', 'is_primary', 'is_active', 'created_at')
    list_filter = ('country', 'city', 'is_primary', 'is_active')
    search_fields = ('city', 'address', 'country')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Manzil maʼlumotlari', {
            'fields': ('center', 'address', 'google_maps_link', 'is_active')
        }),
        ('Tizim maʼlumotlari', {
            'fields': ('created_at', 'updated_at')
        }),
    )

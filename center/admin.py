from django.contrib import admin
from django.utils.text import slugify
from django.utils.html import format_html
from .models import Center, Teacher, Location, Subject


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
    fields = ('get_full_name', 'get_subjects', 'experience_years')
    readonly_fields = ('get_full_name', 'get_subjects')
    show_change_link = True

    def get_full_name(self, obj):
        return obj.user.profile.full_name if hasattr(obj.user, 'profile') else str(obj.user)
    get_full_name.short_description = "O‘qituvchi"

    def get_subjects(self, obj):
        return ", ".join([s.name for s in obj.subjects.all()])
    get_subjects.short_description = "Fanlar"


class LocationInline(admin.TabularInline):
    model = Location
    extra = 1
    fields = ('city', 'address', 'is_primary')
    show_change_link = True


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'level', 'is_active')
    list_filter = ('level', 'is_active')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('id',)
    list_editable = ('is_active',)

    def save_model(self, request, obj, form, change):
        if not obj.slug:
            obj.slug = slugify(obj.name)
        super().save_model(request, obj, form, change)

@admin.register(Center)
class CenterAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'email', 'phone', 'telegram', 'get_subjects', avatar_preview)
    search_fields = ('name', 'owner__email', 'email', 'phone')
    list_filter = ('owner', 'created_at')
    readonly_fields = ('created_at', 'updated_at', avatar_preview)
    inlines = [TeacherInline, LocationInline]
    filter_horizontal = ('subjects',)  


    def get_subjects(self, obj):
        return ", ".join([s.name for s in obj.subjects.all()])
    get_subjects.short_description = "Fanlar"

    ordering = ('-created_at',)
    list_per_page = 20

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('get_full_name', "first_name", "last_name", 'get_center', 'get_subjects', 'experience_years', image_preview)
    list_filter = ('center',)
    search_fields = ('user__profile__full_name', 'center__name')
    readonly_fields = ('created_at', 'updated_at', image_preview)

    fieldsets = (
        ('Shaxsiy maʼlumotlar', {
            'fields': ('user', "first_name", "last_name")
        }),
        ('Taʼlim va ish', {
            'fields': ('subjects', 'experience_years', 'center')
        }),
        ('Rasm va tizim', {
            'fields': ('image', image_preview, 'created_at', 'updated_at')
        }),
    )

    def get_full_name(self, obj):
        return obj.user.profile.full_name if hasattr(obj.user, 'profile') else str(obj.user)
    get_full_name.short_description = "O‘qituvchi"

    def get_center(self, obj):
        return obj.center.name
    get_center.short_description = "Markaz"

    def get_subjects(self, obj):
        return ", ".join([s.name for s in obj.subjects.all()])
    get_subjects.short_description = "Fanlar"

    ordering = ('user__email',)
    list_per_page = 25


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'center', 'country', 'city', 'address', 'is_primary', 'is_active', 'created_at')
    list_filter = ('country', 'city', 'is_primary', 'is_active')
    search_fields = ('city', 'address', 'country')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Manzil maʼlumotlari', {
            'fields': (
                'center', 'country', 'city', 'region',
                'address', 'postal_code', 'google_maps_link',
                'latitude', 'longitude', 'is_primary', 'is_active'
            )
        }),
        ('Tizim maʼlumotlari', {
            'fields': ('created_at', 'updated_at')
        }),
    )

    ordering = ('-created_at',)
    list_per_page = 30

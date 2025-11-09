from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from account.models import User, Profile, Story


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'
    extra = 0
    fields = ('full_name', 'phone_number', 'avatar', 'bio', 'birth_date', 'avatar_preview')
    readonly_fields = ('avatar_preview',)

    def avatar_preview(self, obj):
        if obj.avatar:
            return format_html('<img src="{}" width="60" height="60" style="border-radius:50%;" />', obj.avatar.url)
        return "—"
    avatar_preview.short_description = "Avatar ko‘rinishi"


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = (
        "id", "email", "phone_number",
        "is_center_admin", "is_teacher", "is_student",
        "is_active", "is_staff"
    )
    list_display_links = ("id", "email")
    search_fields = ("email", "phone_number")
    list_filter = ("is_active", "is_staff", "is_center_admin", "is_teacher", "is_student")
    ordering = ("email",)
    inlines = [ProfileInline]
    save_on_top = True

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Role & Permissions"), {
            "fields": (
                "is_active", "is_staff", "is_superadmin",
                "is_center_admin", "is_teacher", "is_student",
                "groups", "user_permissions",
            ),
        }),
        (_("Personal info"), {"fields": ("phone_number",)}),
        (_("Dates"), {"fields": ("date_joined",)}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2", "is_center_admin", "is_teacher", "is_student"),
        }),
    )

    readonly_fields = ("date_joined",)
    filter_horizontal = ("groups", "user_permissions",)

    def get_inline_instances(self, request, obj=None):
        """Inline Profile faqat User yaratilgandan keyin chiqadi."""
        if not obj:
            return []
        return super().get_inline_instances(request, obj)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "full_name", "phone_number", "birth_date", "avatar_preview")
    list_display_links = ("id", "user", "full_name")
    search_fields = ("full_name", "phone_number", "user__email")
    list_filter = ("birth_date",)
    readonly_fields = ("avatar_preview",)

    def avatar_preview(self, obj):
        if obj.avatar:
            return format_html('<img src="{}" width="40" height="40" style="border-radius:50%;" />', obj.avatar.url)
        return "—"
    avatar_preview.short_description = "Avatar"


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "title", "is_active", "expires_at", "preview_image", "preview_video")
    list_display_links = ("id", "user", "title")
    search_fields = ("user__email", "title")
    list_filter = ("is_active", "expires_at")
    readonly_fields = ("is_expired", "view_count")

    def preview_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="60" height="60" style="border-radius:8px;" />', obj.image.url)
        return "—"
    preview_image.short_description = "Rasm"

    def preview_video(self, obj):
        if obj.video:
            return format_html('<video src="{}" width="80" controls />', obj.video.url)
        return "—"
    preview_video.short_description = "Video"

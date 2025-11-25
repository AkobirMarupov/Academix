from django.contrib import admin
from .models import Application, StudentForm, LoginPassword, ApplicationStatusNotification



class StudentFormInline(admin.StackedInline):
    model = StudentForm
    extra = 0
    readonly_fields = ()
    fieldsets = (
        (None, {
            'fields': (
                'full_name', 'birth_date', 'phone_number',
                'region', 'district', 'study_days',
                'format', 'language', 'experience',
            )
        }),
    )


@admin.action(description="Arizani TASDIQLASH")
def approve_application(modeladmin, request, queryset):
    queryset.update(status='approved')
    for app in queryset:
        ApplicationStatusNotification.objects.create(
            application=app,
            message="Sizning arizangiz tasdiqlandi.",
            status=app.status
        )


@admin.action(description="Arizani RAD ETISH")
def reject_application(modeladmin, request, queryset):
    queryset.update(status='rejected')
    for app in queryset:
        ApplicationStatusNotification.objects.create(
            application=app,
            message="Kechirasiz, arizangiz rad etildi.",
            status=app.status
        )


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'center', 'status', 'submitted_at')
    list_filter = ('status', 'center', 'course')
    search_fields = ('student__email', 'student__username', 'course__name')
    ordering = ('-submitted_at',)

    inlines = [StudentFormInline]
    actions = [approve_application, reject_application]

    fieldsets = (
        ("Ariza ma'lumotlari", {
            'fields': ('student', 'center', 'course', 'teacher', 'status')
        }),
        ("Vaqt", {
            'fields': ('submitted_at',),
        }),
    )

    readonly_fields = ('submitted_at',)


@admin.register(LoginPassword)
class LoginPasswordAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'login', 'is_active')
    list_filter = ('course', 'is_active')
    search_fields = ('student__email', 'course__name', 'login')
    ordering = ('-created_at',)

    fieldsets = (
        ("Kirish ma'lumotlari", {
            'fields': ('student', 'course', 'login', 'password', 'is_active')
        }),
    )

@admin.register(ApplicationStatusNotification)
class ApplicationStatusNotificationAdmin(admin.ModelAdmin):
    list_display = ('application', 'message', 'status', 'status_changed_at')
    list_filter = ('status',)
    search_fields = ('application__student__email', 'application__course__name')
    ordering = ('-status_changed_at',)


@admin.register(StudentForm)
class StudentFormAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'phone_number',
        'region',
        'district',
        'format',
        'language',
        'experience',
        'application'
    )
    search_fields = ('full_name', 'phone_number')
    list_filter = ('format', 'language', 'experience')

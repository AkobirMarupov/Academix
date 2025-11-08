from django.contrib import admin
from .models import Course, Review


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        'subject',
        'center',
        'teacher',
        'title',
        'schedule',
        'language',
        'start_time',
        'max_student',
    )
    list_filter = ('schedule', 'language', 'center', 'teacher')
    search_fields = ('title', 'center__name', 'teacher__first_name', 'teacher__last_name')
    list_editable = ('schedule', 'language', 'max_student')
    ordering = ('-start_time',)
    list_per_page = 20

    fieldsets = (
        ("Asosiy ma'lumotlar", {
            'fields': ('title', 'center', 'owner', 'teacher', 'subject')
        }),
        ("Vaqt va format", {
            'fields': ('start_time', 'end_time', 'schedule', 'language')
        }),
        ("Qo‘shimcha ma’lumot", {
            'fields': ('max_student',)
        }),
    )

    def get_queryset(self, request):
        """Optimallashtirish: select_related bilan bog‘langan modellarni oldindan yuklash"""
        qs = super().get_queryset(request)
        return qs.select_related('center', 'teacher')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'rating_stars', 'created_at')
    list_filter = ('rating', 'course', 'student')
    search_fields = ('student__first_name', 'student__last_name', 'course__title')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
    list_per_page = 25

    def rating_stars(self, obj):
        return '⭐' * obj.rating
    rating_stars.short_description = "Bahosi"

    fieldsets = (
        ("Asosiy ma'lumotlar", {
            'fields': ('student', 'course', 'rating', 'comment')
        }),
        ("Tizim ma'lumotlari", {
            'fields': ('created_at',),
        }),
    )

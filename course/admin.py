from django.contrib import admin
from .models import Course, Review, Homework
from django.utils.html import format_html



class HomeworkInline(admin.TabularInline):
    model = Homework
    extra = 1
    fields = ('title', 'due_date', 'created_by', 'is_checked')
    readonly_fields = ()
    show_change_link = True


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'center', 'teacher', 'subject', 'schedule', 'language', 'max_student')
    list_filter = ('center', 'teacher', 'subject', 'schedule', 'language')
    search_fields = ('name', 'center__name', 'teacher__user__profile__full_name')
    inlines = [HomeworkInline]
    ordering = ('-start_time',)
    list_per_page = 25

    fieldsets = (
        ('Asosiy maʼlumotlar', {
            'fields': ('name', 'center', 'teacher', 'subject', 'owner')
        }),
        ('Sozlamalar', {
            'fields': ('start_time', 'end_time', 'schedule', 'language', 'max_student')
        }),
    )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'rating', 'comment', 'created_at')
    list_filter = ('course', 'rating')
    search_fields = ('student__full_name', 'course__title')
    ordering = ('-created_at',)
    list_per_page = 30


@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'due_date', 'is_checked')
    list_filter = ('course', 'is_checked')
    search_fields = ('title', 'course__title', 'user__profile__full_name')
    ordering = ('-created_at',)
    list_per_page = 30

from django.contrib import admin
from .models import Group, GroupStudent, StudentRating


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'teacher', 'max_students', 'get_schedule', 'room_number', 'start_time', 'end_time')
    list_filter = ('course', 'teacher')
    search_fields = ('name', 'course__name', 'teacher__full_name')
    ordering = ('name',)
    list_per_page = 20

    def get_schedule(self, obj):
        if obj.schedule:
            return ", ".join(obj.schedule)
        return "-"
    
    get_schedule.short_description = "Schedule"




@admin.register(GroupStudent)
class GroupStudentAdmin(admin.ModelAdmin):
    list_display = ('student', 'group', 'join_date')
    list_filter = ('group', 'join_date')
    search_fields = ('student__full_name', 'group__name')
    ordering = ('group', 'join_date')
    list_per_page = 20


@admin.register(StudentRating)
class StudentRatingAdmin(admin.ModelAdmin):
    list_display = ('student', 'group', 'score', 'position_in_group', 'position_in_center')
    list_filter = ('group',)
    search_fields = ('student__full_name', 'group__name')
    ordering = ('-score',)
    list_per_page = 20

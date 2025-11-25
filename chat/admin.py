from django.contrib import admin
from .models import ChatRoom, Message

@admin.register(ChatRoom)
class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'admin', 'student', 'is_active', 'created_at')
    list_filter = ('is_active', 'admin', 'student')
    search_fields = ('admin__email', 'student__email')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'chat_room', 'sender', 'short_content', 'is_read', 'created_at')
    list_filter = ('is_read', 'sender')
    search_fields = ('content', 'sender__email')
    readonly_fields = ('created_at', 'updated_at')

    def short_content(self, obj):
        return obj.content[:50]
    short_content.short_description = 'Content'

from django.db import models
from django.conf import settings
from common.models import BaseModel

class ChatRoom(BaseModel):
    admin = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='admin_chats',limit_choices_to={'is_center_admin': True})
    student = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='student_chats',limit_choices_to={'is_student': True})
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('admin', 'student')
        verbose_name = "Chat xonasi"
        verbose_name_plural = "Chat xonalari"

    def __str__(self):
        return f"{self.admin.email} ↔ {self.student.email}"


class Message(BaseModel):
    chat_room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_at']
        verbose_name = "Xabar"
        verbose_name_plural = "Xabarlar"

    def __str__(self):
        return f"{self.sender.email}: {self.content[:20]}"

# chat/models.py
from django.db import models
from django.contrib.auth import get_user_model
from projects.models import Project  # 引入项目模型

User = get_user_model()

class PrivateMessage(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f'From {self.sender} to {self.receiver} at {self.timestamp}'


class ChatInvitation(models.Model):
    sender = models.ForeignKey(User, related_name='sent_invitations', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_invitations', on_delete=models.CASCADE)
    project = models.ForeignKey(Project, related_name='invitations', on_delete=models.CASCADE)
    message = models.TextField()  # 邀请附带的消息
    timestamp = models.DateTimeField(auto_now_add=True)
    is_accepted = models.BooleanField(default=False)

    def __str__(self):
        return f'Invitation from {self.sender} to {self.receiver} for project {self.project}'

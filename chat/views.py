# chat/views.py
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import PrivateMessage, ChatInvitation
from projects.models import Project
from django.contrib.auth import get_user_model
from django.db import models
from rest_framework.decorators import api_view
from rest_framework import status
from projects.models import ProjectMember
from django.db import IntegrityError

User = get_user_model()


@api_view(['POST'])
def send_message(request):
    sender = request.user
    receiver_id = request.data.get('receiver_id')
    message = request.data.get('message')

    receiver = get_object_or_404(User, id=receiver_id)

    # 创建消息记录
    new_message = PrivateMessage.objects.create(sender=sender, receiver=receiver, message=message)
    return Response({
        'message': 'Message sent successfully',
        'data': {
            'sender': sender.username,
            'receiver': receiver.username,
            'message': new_message.message,
            'timestamp': new_message.timestamp
        }
    }, status=200)


@api_view(['GET'])
def get_chat_history(request, user_id):
    current_user = request.user
    other_user = get_object_or_404(User, id=user_id)

    # 获取两者之间的所有私聊信息
    messages = PrivateMessage.objects.filter(
        (models.Q(sender=current_user) & models.Q(receiver=other_user)) |
        (models.Q(sender=other_user) & models.Q(receiver=current_user))
    ).order_by('timestamp')

    # 返回聊天记录
    message_list = [{'sender': msg.sender.name, 'message': msg.message, 'timestamp': msg.timestamp} for msg in messages]
    return Response(message_list, status=200)

@api_view(['POST'])
def send_chat_invitation(request):
    sender = request.user
    receiver_id = request.data.get('receiver_id')
    project_id = request.data.get('project_id')
    message = request.data.get('message')

    receiver = get_object_or_404(User, pk=receiver_id)
    project = get_object_or_404(Project, pk=project_id)

    invitation = ChatInvitation.objects.create(
        sender=sender,
        receiver=receiver,
        project=project,
        message=message
    )

    return Response({"message": "Chat invitation sent successfully."}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def accept_chat_invitation(request, invitation_id):
    # 获取邀请对象
    invitation = get_object_or_404(ChatInvitation, pk=invitation_id)

    # 检查请求用户是否为邀请的接收者
    if request.user != invitation.receiver:
        return Response({"error": "You do not have permission to accept this invitation."},
                        status=status.HTTP_403_FORBIDDEN)

    # 获取项目并将用户添加为成员
    project = invitation.project
    try:
        ProjectMember.objects.create(project=project, user=request.user)
    except IntegrityError:
        return Response({"error": "User is already a member of this project."}, status=status.HTTP_400_BAD_REQUEST)

    # 更新邀请状态为已接受
    invitation.is_accepted = True
    invitation.save()

    return Response({"message": "Chat invitation accepted and user added to project."}, status=status.HTTP_200_OK)

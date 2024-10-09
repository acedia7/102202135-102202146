from django.urls import path
from .views import send_message, get_chat_history, send_chat_invitation, accept_chat_invitation

urlpatterns = [
    path('message/send/', send_message, name='send_message'),
    path('message/history/<int:user_id>/', get_chat_history, name='get_chat_history'),
    path('invite/send/', send_chat_invitation, name='send_chat_invitation'),
    path('invite/<int:invitation_id>/accept/', accept_chat_invitation, name='accept_chat_invitation'),
]

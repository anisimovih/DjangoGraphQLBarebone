"""Chat app resolvers."""
from __future__ import annotations

from ariadne import QueryType, MutationType, convert_kwargs_to_snake_case
from django.contrib.auth import get_user_model
from .models import Message

User = get_user_model()
query = QueryType()
mutation = MutationType()


@convert_kwargs_to_snake_case
@query.field("messages")
def list_messages(*_,
                  id: int | None = None,
                  text: str | None = None,
                  sender_id: int | None = None,
                  recipient_id: int | None = None):
    """List message objects with optional filters."""
    messages = Message.objects.all()
    if id is not None:
        messages = messages.filter(id=id)
    if text is not None:
        messages = messages.filter(text=text)
    if sender_id is not None:
        messages = messages.filter(sender_id=sender_id)
    if recipient_id is not None:
        messages = messages.filter(recipient_id=recipient_id)
    return [
        {
            'id': message.id,
            'text': message.text,
            'sender': message.sender,
            'recipient': message.recipient,
            'created_at': message.created_at,
            'updated_at': message.updated_at,
        }
        for message in messages
    ]


@convert_kwargs_to_snake_case
@mutation.field("createMessage")
def create_message(*_, text: str, sender_id: int, recipient_id: int):
    """Create message object."""
    message = Message.objects.create(text=text, sender_id=sender_id, recipient_id=recipient_id)
    return {
        'id': message.id,
        'text': message.text,
        'sender_id': message.sender_id,
        'recipient_id': message.recipient_id,
        'created_at': message.created_at,
        'updated_at': message.updated_at,
    }

"""Users app resolvers."""
from __future__ import annotations

from ariadne import QueryType, MutationType, convert_kwargs_to_snake_case
from django.contrib.auth import get_user_model

User = get_user_model()
query = QueryType()
mutation = MutationType()


@convert_kwargs_to_snake_case
@query.field("users")
def list_users(*_,
               id: int | None = None,
               username: str | None = None,
               email: str | None = None,
               first_name: str | None = None,
               last_name: str | None = None):
    """List user objects with optional filters."""
    users = User.objects.all()
    if id is not None:
        users = users.filter(id=id)
    if username is not None:
        users = users.filter(username=username)
    if email is not None:
        users = users.filter(email=email)
    if first_name is not None:
        users = users.filter(first_name=first_name)
    if last_name is not None:
        users = users.filter(last_name=last_name)
    return [
        {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'date_joined': user.date_joined,
        }
        for user in users
    ]


@convert_kwargs_to_snake_case
@mutation.field("createUser")
def create_user(*_, email: str, username: str, first_name: str = '', last_name: str = ''):
    """Create user object."""
    user = User.objects.create(email=email, username=username, first_name=first_name, last_name=last_name)
    return {
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'date_joined': user.date_joined,
    }

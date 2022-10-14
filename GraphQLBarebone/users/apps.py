"""Root point for auth app."""
from django.apps import AppConfig


class AuthConfig(AppConfig):
    """Main auth app class."""

    name = 'GraphQLBarebone.users'
    label = 'GraphQLBarebone_users'

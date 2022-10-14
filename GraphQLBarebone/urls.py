"""GraphQLBarebone URL Configuration."""

from ariadne_django.views import GraphQLView

from django.contrib import admin
from django.urls import path

from .graphql_config import schema as GQL_schema

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', GraphQLView.as_view(schema=GQL_schema), name='graphql'),
]

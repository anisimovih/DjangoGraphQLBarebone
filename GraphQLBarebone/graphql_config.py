"""Root GQL configuration."""

from ariadne import (
    load_schema_from_path,
    make_executable_schema,
    snake_case_fallback_resolvers
)
from ariadne_django.scalars import date_scalar, datetime_scalar

from .users.resolvers import query as user_queries, mutation as user_mutations
from .chat.resolvers import query as chat_queries, mutation as chat_mutations

type_defs = [
    load_schema_from_path("GraphQLBarebone/schema.graphql"),
    load_schema_from_path("GraphQLBarebone/users/schema.graphql"),
    load_schema_from_path("GraphQLBarebone/chat/schema.graphql"),
]

schema = make_executable_schema(
    type_defs,
    [
        user_queries,
        user_mutations,
        chat_queries,
        chat_mutations,
        date_scalar,
        datetime_scalar,
        snake_case_fallback_resolvers
    ]
)

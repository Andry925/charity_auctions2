from django.contrib.auth.models import AnonymousUser
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
from channels.middleware import BaseMiddleware
from rest_framework_simplejwt.tokens import AccessToken
from urllib.parse import parse_qs

User = get_user_model()

@database_sync_to_async
def get_user(token_key):
    try:
        token = AccessToken(token_key)
        user_id = token['user_id']
        user = User.objects.get(pk=user_id)
        return user
    except Exception as e:
        print(f"Error getting user: {e}")
        return AnonymousUser()

class TokenAuthMiddleware(BaseMiddleware):

    def __init__(self, inner):
        self.inner = inner

    async def __call__(self, scope, receive, send):
        query_string = scope['query_string'].decode()
        query_params = parse_qs(query_string)
        token_key = query_params.get('access_token')
        if token_key:
            scope['user'] = await get_user(token_key[0])
        return await super().__call__(scope, receive, send)

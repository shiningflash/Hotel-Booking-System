import os, logging, requests, json
from rest_framework import permissions
from django.conf import settings

logger = logging.getLogger(__name__)


class EvalyAPIUserPermission(permissions.BasePermission):

    def is_authorized(self, action, module, role):
        payload = {
            "platform": "ebilling",
            "module": module,
            "role": role,
            "action": action
        }
        response = requests.post(
            f"{os.environ.get('AUTHORIZATION_SERVICE')}/authorize",
            json=payload,
            headers={'secret-key': settings.EVALY_API_SECRET_KEY}
        )
        return response.json().get('success')

    """
    Allows access only to users who have the appropriate permission.
    """
    action_name = ""
    module = ""

    def __init__(self, action_name, module):
        super().__init__()
        self.action_name = action_name
        self.module = module

    def __call__(self):
        return self

    def has_permission(self, request, view):
        try:
            return self.is_authorized(
                self.action_name, self.module, request.users.get('role')
            )
        except:
            return False


class EvalyAPISecretPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if 'HTTP_SECRET_KEY' not in request.META or request.META['HTTP_SECRET_KEY'] != settings.EVALY_API_SECRET_KEY:
            return False
        else:
            return True

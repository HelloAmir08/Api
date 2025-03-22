from datetime import timedelta

from rest_framework.permissions import BasePermission
import datetime
from django.utils.timezone import now


class OnlyWeekDays(BasePermission):
    def has_permission(self, request, view):
        today = datetime.date.today().weekday()

        if request.method in ['GET', 'POST'] and today in range(5):
            return True
        return False


class CommentPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        time_difference = now() - obj.created_at
        if time_difference < timedelta(minutes=2):
            return True

        return False

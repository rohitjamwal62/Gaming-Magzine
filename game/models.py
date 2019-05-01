
from django.contrib.auth.models import User



from django.db import models
from django.conf import settings
from django.db import models


class SearchQuery(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL)
    query = models.CharField(max_length=220)
    timestamp = models.DateTimeField(auto_now_add=True)


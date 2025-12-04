from django.db import models
import uuid

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True, verbose_name="氏名")
    password = models.CharField(max_length=255, verbose_name="パスワード")

    def __str__(self):
        return self.name

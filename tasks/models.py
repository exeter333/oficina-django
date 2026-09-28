from django.db import models


class Task(models.Model):
    title = models.CharField("título", max_length=200)
    completed = models.BooleanField("concluída", default=False)
    created_at = models.DateTimeField("criada em", auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

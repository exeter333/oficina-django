from django.db import models


class Task(models.Model):
    PRIORITY_CHOICES = [
        (1, "Baixa"),
        (2, "Média"),
        (3, "Alta"),
    ]

    title = models.CharField("título", max_length=200)
    completed = models.BooleanField("concluída", default=False)
    priority = models.PositiveSmallIntegerField("prioridade", choices=PRIORITY_CHOICES, default=2)
    created_at = models.DateTimeField("criada em", auto_now_add=True)

    class Meta:
        ordering = ["-priority", "-created_at"]

    def __str__(self):
        return self.title

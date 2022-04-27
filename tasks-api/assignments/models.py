from django.db import models


class Assignment(models.Model):
    creator = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        related_name="assignment",
        verbose_name="Criador da tarefa",
    )
    task_name = models.CharField("Nome da tarefa", max_length=100)
    description = models.TextField("Descrição da tarefa", blank=True)
    create_day = models.DateField("Dia da criação", auto_now_add=True)
    final_day = models.DateField("Dia da finalização", blank=True, null=True)
    active = models.BooleanField("Tarefa ativa", default=True)

    def __str__(self):
        return f"{self.creator.username} -> {self.task_name}"

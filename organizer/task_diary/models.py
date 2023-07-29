from django.db import models




class Tasks(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название задания")
    memo = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    datecompleted = models.DateTimeField(null=True, verbose_name="Время выполнения")
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title or ''



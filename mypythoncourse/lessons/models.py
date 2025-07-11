from django.db import models

class Lesson(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    code_example = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

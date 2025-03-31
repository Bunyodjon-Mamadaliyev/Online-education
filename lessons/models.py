from django.db import models

class Lesson(models.Model):
    module = models.ForeignKey('modules.Module', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    video_url = models.URLField(null=True, blank=True)
    duration = models.PositiveIntegerField()
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.order}. {self.title}"

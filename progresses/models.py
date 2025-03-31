from django.db import models


class Progress(models.Model):
    enrollment = models.ForeignKey('enrollments.Enrollment', on_delete=models.CASCADE)
    lesson = models.ForeignKey('lessons.Lesson', on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.enrollment.user.username} - {self.lesson.title} ({'Completed' if self.is_completed else 'In Progress'})"

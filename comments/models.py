from django.db import models
from elements.models import Element

# Create your models here.
class Comment(models.Model):
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    element = models.ForeignKey(Element, related_name='comments', on_delete=models.CASCADE, null=True)
    def __str__(self):
        return 'Comentario #{}'.format(self.id)
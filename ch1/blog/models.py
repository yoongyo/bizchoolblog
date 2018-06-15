from django_summernote import models as summer_model
from django_summernote import fields as summer_fields
from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Post(summer_model.Attachment):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=20)
    content = summer_fields.SummernoteTextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
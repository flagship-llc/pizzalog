from django.db import models

class Style(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Shop(models.Model):
    name = models.CharField(max_length=100)
    readable_name = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    style = models.ForeignKey(Style, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

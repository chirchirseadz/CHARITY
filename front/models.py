from django.db import models

# Create your models here.


class Message(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField()
    subject = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    body = models.TextField()

    def __str__(self):
        return f'Message sent to you by {self.name}'


class Gallary(models.Model):
    title = models.CharField(max_length=100, null=True)
    venue = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    image = models.ImageField(default='empty.jpg', null=True)
    event_date = models.DateField(auto_now=True)

    def __str__(self):
        pass
        # return f'{self.title}'




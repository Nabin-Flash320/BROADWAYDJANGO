from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=200)
    subject = models.TextField()
    message = models.TextField()

    def __str__(self):
        return f"{self.name}, {self.email}, {self.subject}, {self.message}"


class FeedBack(models.Model):
    name = models.CharField(max_length=400)
    post = models.CharField(max_length=200)
    comment = models.TextField()
    image = models.TextField()

    def __str__(self):
        return f"{self.name}, {self.post}, {self.comment}, {self.image}"

class Informations(models.Model):
    address1 = models.CharField(max_length=500)
    address1 = models.CharField(max_length=500, blank=True)
    phonenumber = models.CharField(max_length=50)
    time = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return f"{self.address1}, {self.address2}, {self.phonenumber}, {self.time}, {self.email}"


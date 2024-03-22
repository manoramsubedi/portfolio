from django.db import models

# Create your models here.

#About model
class About(models.Model):
    short_description = models.TextField(max_length=225)
    description = models.TextField()
    image = models.ImageField(upload_to="about")

    class Meta:
        verbose_name = "about-me"
        verbose_name_plural = "about-me"
    
    def __str__(self):
        return "About"
    
#Service model
class Service(models.Model):
    name = models.CharField(max_length=100, verbose_name="service-name")
    description = models.TextField(verbose_name="about-service")

    def __str__(self):
        return self.name
    
#Recent work
class RecentWork(models.Model):
    title = models.CharField(max_length=100, verbose_name="Work-title")
    image = models.ImageField(upload_to="works")
    #description = models.TextField(verbose_name="work")

    def __str__(self):
        return self.title
    
#Client
class Client(models.Model):
    name = models.TextField(verbose_name="client-name")
    description = models.TextField(verbose_name="client-description")
    image = models.ImageField(upload_to="clients", default="default.png")

    def __str__(self):
        return self.title

    




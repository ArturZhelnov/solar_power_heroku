from django.db import models
#from django.contrib.auth.models import User

# Create your models here.
'''
class Social_link(models.Model):
    #user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    social_name = models.CharField(max_length=10)
    link = models.URLField(max_length=200)
    
    def __str__(self):
        return self.social_name
'''    
    
class Contact(models.Model):
    name = models.CharField(max_length=120)
    #email = models.EmailField()
    phone = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    # f'Comment by {self.name} on {self.post}'
    # f'{self.name}'
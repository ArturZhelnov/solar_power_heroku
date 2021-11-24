from django.db import models
#from django.contrib.auth.models import User

# Create your models here.

class Social_link(models.Model):
    #user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    #about = models.ForeignKey(SOCIAL, on_delete=models.CASCADE)
    soc_name = models.CharField(max_length=10)
    #soc_img = models.ImageField(upload_to='Social_images', verbose_name='Social Picture')
    soc_img = models.FileField(upload_to='Social_images')
    link = models.URLField(max_length=200)
    # is_active = models.BooleanField(default=False)
    
    class Meta:
        ordering = ('soc_name',)#or in admin.py
        #verbose_name = 'Skill'
        #verbose_name_plural = 'Skills'
    
    def __str__(self):
        return self.soc_name


# TEENUSED
class Service(models.Model):
    heading = models.CharField(max_length=150)
    #text = models.CharField(max_length=500)
    text = models.TextField(blank=False)
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('id',)#or in admin.py

    def __str__(self):
        return f'{self.heading[:15]}..'
        #return self.heading
    
class Service_img(models.Model):
    name = models.CharField(max_length=50)
    service_img = models.ImageField(upload_to='service', blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'
    
#STEPS START
class Step(models.Model):
    heading = models.CharField(max_length=150)
    #text = models.CharField(max_length=500)
    text = models.TextField(blank=False)
    # number = models.IntegerField(default=01, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('id',)#or in admin.py

    def __str__(self):
        return f'{self.heading[:15]}..'
        #return self.heading
    
class Steps_img(models.Model):
    name = models.CharField(max_length=50)
    st_img = models.ImageField(upload_to='steps', blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'
    
#STEPS END
#PARTNERS START
class Partner(models.Model):
    name = models.CharField(max_length=20)
    img = models.ImageField(upload_to='partners')
    link = models.URLField(max_length=200)
    is_active = models.BooleanField(default=False)
    
    class Meta:
        ordering = ('id',)#or in admin.py
        verbose_name = 'Partner'
        verbose_name_plural = 'Partners'
    
    def __str__(self):
        return self.name
    
# PARTNERS END
class Contact(models.Model):
    name = models.CharField(max_length=120)
    #email = models.EmailField()
    phone = models.CharField(max_length=20)
    #is_contacted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    # f'Comment by {self.name} on {self.post}'
    # f'{self.name}'
    
class Footer_contact(models.Model):
    address = models.CharField(max_length=120, blank=True)
    email = models.EmailField(verbose_name="Email", blank=True)
    phone = models.CharField(max_length=20, blank=True)
    working_hours = models.CharField(max_length=200, blank=True)
    reg_code = models.CharField(max_length=150, blank=True,)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.address}'
    

class Blockquote(models.Model):
    citate = models.TextField()
    owner = models.CharField(max_length=120, blank=True)
    position = models.CharField(max_length=120, blank=True)
    
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.citate[:20]}..'
    
    
class Client(models.Model):
    img = models.ImageField(upload_to='clients/')
    img_name = models.CharField(max_length=50)
    heading = models.CharField(max_length=100)
    heading_img = models.FileField(upload_to='clients/heading_img', blank=True)#default='clients/heading_img/example.svg'
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.heading}'
    
    
class Client_item(models.Model):
    client_name = models.ForeignKey(Client, on_delete=models.CASCADE)
    
    text = models.CharField(max_length=120, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    

class Info_tab(models.Model):
    name = models.CharField(max_length=20)
    tab_id = models.CharField(max_length=4)
    
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tab_id
    
    
class Info_tab_context(models.Model):#Tab_context
    tab_id = models.ForeignKey(Info_tab, on_delete=models.CASCADE)
    
    tab_img = models.ImageField(upload_to='info/')
    tab_img_name = models.CharField(max_length=20, blank=True)
    # tab_text = models.CharField(max_length=500)
    tab_text = models.TextField()
    
    # objects = models.Manager() # The default manager.
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-tab_id',)#or in admin.py
    
    def __str__(self):
        return f'{self.tab_img_name} for {self.tab_id}'#self.tab_img_name
    
    
    
from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100,unique=True,null=False)
    email = models.EmailField(null=False)
    img = models.ManyToManyField('Image',related_name='img')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Image(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    user_img = models.ImageField(upload_to='user_images/')

    def __str__(self):
        return '%s %s' % (self.owner,self.user_img)
    

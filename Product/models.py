from django.db import models
from django.utils.safestring import mark_safe
from django.db.models import Count, Sum, Avg
from django.contrib.auth.models import User
from django.forms import ModelForm

# Create your models here.
class Category(models.Model):
    status = {
        ('True','True'),
        ('False','False'),
    }

    my_choices = {
        ('Male','Male'),
        ('Female','Female'),
    }


    title = models.CharField(max_length=200)
    Image = models.ImageField(blank=True,upload_to='category/')
    status = models.CharField(max_length=20,choices=status)
    gender = models.CharField(max_length=20,choices=my_choices)
    slug = models.SlugField(null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


    def ImageUrl(self):
        if self.Image:
            return self.Image.url
        else:
            return ""

    def image_tag(self):
        return mark_safe('<img src="{}" heights="70" width="60" />'.format(self.image.url))
        image_tag.short_description = 'Image'


#product models

class Product(models.Model):
    status = (
        ('True', 'True'),
        ('False', 'False'),)


    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    keywords = models.CharField(max_length=100)
    image = models.ImageField(blank=True, upload_to='product/')
    new_price = models.DecimalField(decimal_places=2, max_digits=15, default=0)
    old_price = models.DecimalField(decimal_places=2, max_digits=15)
    amount = models.IntegerField(default=0)
    short_detail = models.TextField()
    long_detail = models.TextField()
    status = models.CharField(max_length=20, choices=status)
    slug = models.SlugField(null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


    def ImageUrl(self):
        if self.image:
            return self.image.url
        else:
            return ""

    def image_tag(self):
        return mark_safe('<img src="{}" heights="70" width="60" />'.format(self.image.url))
    image_tag.short_description = 'Image'


#comment model 
class Comment(models.Model):
    STATUS = (
        ('New', 'New'),
        ('True', 'True'),
        ('False', 'False'),

    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200, blank=True)
    comment = models.CharField(max_length=500, blank=True)
    rate = models.IntegerField(default=1)
    ip = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=40, choices=STATUS, default='New')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject



#comment form
class CommenttForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['subject', 'comment', 'rate']

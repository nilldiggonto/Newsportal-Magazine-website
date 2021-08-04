from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from .utils import unique_slugify
from django.urls import reverse



# def getcurrentusername(instance, filename):
#     return "device/request/{0}/{1}".format(instance.agent.username, filename)
# Create your models here.
class PostCategory(models.Model):
    category    =   models.CharField(max_length=20,unique=True)
    slug        = models.SlugField(max_length=300,unique=True,null=True,blank=True)
    rank        =   models.IntegerField(default=1)
    active      =   models.BooleanField(default=True)
    created_at  =   models.DateTimeField(auto_now=True)
    updated_at  =   models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category

    def save(self, **kwargs):
        slug_str = str(self.category)
        unique_slugify(self, slug_str) 
        return super().save(**kwargs)

    def get_absolute_url(self):
        # return f"/category/{self.slug}/"
        return reverse("category-page", kwargs={"slug": self.slug})


class PostSubCategory(models.Model):
    category    =   models.ForeignKey(PostCategory,related_name='subcategory',on_delete=models.CASCADE)
    slug        =   models.SlugField(max_length=300,unique=True,null=True,blank=True)
    sub_name    =   models.CharField(max_length=20)
    rank        =   models.IntegerField(default=1)
    featured    =   models.BooleanField(default=False)
    active      =   models.BooleanField(default=True)
    created_at  =   models.DateTimeField(auto_now=True)
    updated_at  =   models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sub_name

    def save(self, **kwargs):
        slug_str = str(self.sub_name)
        unique_slugify(self, slug_str) 
        return super().save(**kwargs)

class Post(models.Model):

    scategory           =   models.ForeignKey(PostSubCategory,related_name='post',on_delete=models.CASCADE)
    title               =   models.CharField(max_length=200)
    intro_image         =   models.ImageField(upload_to='content/',null=True,blank=True)
    intro_link          =   models.URLField(null=True,blank=True)
    slug                =   models.SlugField(max_length=300,unique=True,null=True,blank=True)


    intro               =   models.CharField(max_length=200)
    summary_one         =   models.TextField(null=True,blank=True)
    
    summary_two         =   models.TextField(null=True,blank=True)
    summary_three       =   models.TextField(null=True,blank=True)
    summary_four        =   models.TextField(null=True,blank=True)

    primary_featured    =   models.BooleanField(default=True)
    popular             =   models.BooleanField(default=False)

    featured            =   models.BooleanField(default=False)
    active              =   models.BooleanField(default=False)

    def __str__(self):
        return self.intro

    def save(self, **kwargs):
        slug_str = str(self.title)
        unique_slugify(self, slug_str) 
        return super().save(**kwargs)

    class Meta:
        ordering = ['-id']


    



    



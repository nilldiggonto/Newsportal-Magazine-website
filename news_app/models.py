from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from .utils import unique_slugify
from django.urls import reverse
from django.contrib.auth.models import User


# def getcurrentusername(instance, filename):
#     return "device/request/{0}/{1}".format(instance.agent.username, filename)
# Create your models here.
class PostCategory(models.Model):
    category    =   models.CharField(max_length=20,unique=True)
    slug        = models.SlugField(max_length=300,unique=True,null=True,blank=True)
    rank        =   models.IntegerField(default=1)
    icon        =   models.CharField(null=True,blank=True,max_length=250)
    active      =   models.BooleanField(default=True)
    bangla      =   models.BooleanField(default=False)
    updated_at  =   models.DateTimeField(auto_now=True)
    created_at  =   models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category

    def save(self, **kwargs):
        slug_str = str(self.category)
        unique_slugify(self, slug_str) 
        return super().save(**kwargs)

    # def get_absolute_url(self):
    #     # return f"/category/{self.slug}/"
    #     return reverse("category-page", kwargs={"slug": self.slug})


class PostSubCategory(models.Model):
    category    =   models.ForeignKey(PostCategory,related_name='subcategory',on_delete=models.CASCADE)
    slug        =   models.SlugField(max_length=300,unique=True,null=True,blank=True)
    sub_name    =   models.CharField(max_length=20)
    icon        =   models.CharField(null=True,blank=True,max_length=250)

    rank        =   models.IntegerField(default=1)
    featured    =   models.BooleanField(default=False)
    active      =   models.BooleanField(default=True)
    bangla      =   models.BooleanField(default=False)

    updated_at  =   models.DateTimeField(auto_now=True)
    created_at  =   models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sub_name

    def save(self, **kwargs):
        slug_str = str(self.sub_name)
        unique_slugify(self, slug_str) 
        return super().save(**kwargs)
        
    def get_absolute_url(self):
        # return f"/category/{self.slug}/"
        return reverse("category-page", kwargs={"slug": self.slug})

class Post(models.Model):

    author               = models.ForeignKey(User,related_name='user_post',on_delete=models.CASCADE)

    scategory           =   models.ForeignKey(PostSubCategory,related_name='post',on_delete=models.CASCADE)
    title               =   models.CharField(max_length=200)
    intro_image         =   models.ImageField(upload_to='content/',null=True,blank=True)
    intro_link          =   models.URLField(null=True,blank=True)
    slug                =   models.SlugField(max_length=300,unique=True,null=True,blank=True,allow_unicode=True)


    intro               =   models.TextField(null=True,blank=True)
    summary_one         =   models.TextField(null=True,blank=True)
    
    summary_two         =   models.TextField(null=True,blank=True)
    summary_three       =   models.TextField(null=True,blank=True)
    summary_four        =   models.TextField(null=True,blank=True)

    primary_featured    =   models.BooleanField(default=False)
    popular             =   models.BooleanField(default=False)
    view_count          =   models.BigIntegerField(default=0)

    featured            =   models.BooleanField(default=False)
    bangla      =   models.BooleanField(default=False)

    active              =   models.BooleanField(default=False)
    updated_at          =   models.DateTimeField(auto_now=True)
    created_at          =   models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    # def save(self, *args, **kwargs):                                  # add this
    #     self.slug = slugify(self.title, allow_unicode=True)           # add this
    #     super().save(*args, **kwargs)  

    def save(self, **kwargs):
        slug_str = str(self.title)
        unique_slugify(self, slug_str) 
        return super().save(**kwargs)

    class Meta:
        ordering = ['-id']

    def get_absolute_url(self):
        return reverse("single-page", kwargs={"slug": self.slug})



class Comment(models.Model):
    comment_to = models.ForeignKey(User,related_name='comment_user',on_delete=models.CASCADE)
    post    =   models.ForeignKey(Post,related_name='comment',on_delete=models.CASCADE)
    name    =   models.CharField(max_length=50)
    oponion =   models.CharField(max_length=120)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


    



    



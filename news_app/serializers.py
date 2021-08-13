from .models import Post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['scategory','title','intro_image','intro_link','get_absolute_url','intro']
        depth = 1
        # ordering = ['-id']
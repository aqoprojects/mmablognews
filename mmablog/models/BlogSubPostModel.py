from django.db import models
from mmablog.models.BlogPostModel import BlogPost
from mmablog.models.BlogCategoryModel import BlogCategory
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
from django.conf import settings
import uuid


class BlogSubPost(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=True)
    blogheadline = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    topic_image  = models.ImageField(upload_to='blog/BlogExtraPhotos',null=True, blank=True,validators=[
            FileExtensionValidator(allowed_extensions=['jpeg', 'jpg', 'png']),
        ],)
    topic = models.CharField(max_length=250, null=True, blank=True)
    article = models.TextField(null=True,blank=True)
    total_clicks = models.BigIntegerField(default=0)
    total_comments = models.BigIntegerField(default=0)   
    publisher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='%(class)s_publisher')
    author = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='%(class)s_author') 
    posted_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    
    class Meta:
        ordering = ['-topic_image']
        db_tablespace = 'BSPtableIndexStorage'
        
        indexes = [models.Index(fields=['topic_image', 'topic', 'article', 'posted_date'])]    
    


    
    def sub_topic_image(self):
        try:
            return self.topic_image.url
        except:
            pass
    
    
    def __str__(self):
        return self.topic
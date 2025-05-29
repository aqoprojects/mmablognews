from django.db import models
from mmablog.models.BlogCategoryModel import BlogCategory
from django.core.validators import FileExtensionValidator
from django.utils.text import slugify
import uuid
from django.conf import settings

# def topic_image_file_path(instance, filename):
#     # Construct the file path based on the album's title and the song's title
#     return os.path.join('blog/photos', instance.category.name, filename)

# def topic_image_small_file_path(instance, filename):
#     # Construct the file path based on the album's title and the song's title
#     return os.path.join('blog/photos', instance.category.name, 'small_size/', filename)
    


class BlogPost(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=True)
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    topic_image = models.ImageField(upload_to='blogPhotos/',null=True, blank=True,validators=[
            FileExtensionValidator(allowed_extensions=['jpeg', 'jpg', 'png']),
        ],)
    # topic_image_small = models.ImageField(upload_to=topic_image_small_file_path,null=True, blank=True,validators=[
    #         FileExtensionValidator(allowed_extensions=['jpeg', 'jpg', 'png']),
    #     ],)
    topic = models.CharField(max_length=250, null=True, blank=True)
    slug = models.SlugField(max_length=100, null=True, blank=True)
    article = models.TextField(null=True,blank=True)
    total_clicks = models.BigIntegerField(default=0)
    total_comments = models.BigIntegerField(default=0)    
    publisher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='%(class)s_publisher')
    author = models.ManyToManyField(settings.AUTH_USER_MODEL,  related_name='%(class)s_author')
    posted_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_tablespace = 'BPtableIndexStorage'
        
        indexes = [models.Index(fields=['topic_image', 'topic', 'article', 'posted_date'])]    
    
    
    def publisher_image(self):
        try:
            self.topic_image.url
        except:
            return 'img/news-800x500-3.jpg'

    def save(self, *args, **kwargs):

        if self.slug == None:
            topic_slug = slugify(self.topic)
            check_slug = BlogPost.objects.filter(slug__startswith=topic_slug).count()
            if check_slug:
                topic_slug = f'{slugify(topic_slug)}-{check_slug + 1}'
            
            self.slug = topic_slug
        return super().save(*args, **kwargs)

    
    
    def __str__(self):
        return self.topic
    
# for i in BlogPost.objects.all():
#     i.topic_slug = slugify(i.topic)
#     i.save()
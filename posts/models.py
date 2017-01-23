from django.db import models
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=120)
    #author = models.ForeignKey(User,name='posts')
    content = models.TextField()
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    highlighted = models.TextField()


    class Meta:
    	ordering = ('created_date',)

'''
def save(self, *args, **kwargs):
    """
    Use the `pygments` library to create a highlighted HTML
    representation of the code post
    """
    options = self.title and {'title': self.title} or {}
    formatter = HtmlFormatter(style=self.style,
                              full=True, **options)
    self.highlighted = highlight(self.content, formatter)
    super(Post, self).save(*args, **kwargs)
'''

	

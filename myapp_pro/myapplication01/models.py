from django.db import models
from django.urls import reverse



class Articles(models.Model):
    """
    A typical class defining a model, derived from the Model class.
    """

    # Fields
    my_articles_name = models.CharField(max_length=100, help_text="Enter field documentation")  #  第几作者  # 5
    my_articles_index = models.CharField(max_length=200)  # 文章的网址或者项目网址
    my_articles_DOI = models.CharField(max_length=200)  # 文章标识号，或者githubw网址
    my_articles_title = models.CharField(max_length=200)   # 文章或项目名称
    my_articles_date = models.CharField(max_length=20)    #制作好的日期
    # Metadata
    class Meta:
        ordering = ['my_articles_date']

    # Methods
    def get_absolute_url(self):
            """
            Returns the url to access a particular instance of MyModelName.
            """
            return reverse('article_id', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.my_articles_index
    
class edu(models.Model):
    my_edu_index = models.CharField(max_length=20)
    my_edu_name = models.CharField(max_length=100)
    my_edu_major = models.CharField(max_length=100)
    my_edu_degree = models.CharField(max_length=100)
    my_edu_date = models.CharField(max_length=30)
    
    # Methods
    def get_absolute_url(self):
            """
            Returns the url to access a particular instance of MyModelName.
            """
            return reverse('article_id', args=[str(self.id)])
    class Meta:
        ordering = ['my_edu_index']


    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.my_edu_index
    

class award(models.Model):
     my_award_name = models.CharField(max_length=100)
     my_award_index = models.CharField(max_length=10)
     my_award_date = models.CharField(max_length=20)

     class Meta:
          ordering = ['my_award_index']


     def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.my_award_index
# Create your models here.

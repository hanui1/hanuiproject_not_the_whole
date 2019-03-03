from django.db import models
from django.utils import timezone


# Create your models here.

# class Category(models.Model):
#     name = models.CharField(max_length=250)
#     slug = models.SlugField(max_length=250, unique=True)

#     class Meta:
#         ordering = ('name',)
#         verbose_name = 'category'
#         verbose_name_plural = 'categories'

#     def __str__(self):
#         return self.name

class Category(models.Model):
    class Meta:
        verbose_name = u'분류'
        ordering = ['name']

    name = models.CharField(verbose_name=u'이름', max_length=50)

    def __unicode__(self):
        return self.name

    objects = models.Manager()


class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete = "set null", verbose_name=u'분류', null=True, blank=True)

    def __str__(self):
        return self.title
    
    objects = models.Manager()
    #오 이거 넣으니까 해결 됐네

    def summary(self):
        return self.body[:100] #pylint: disable=E1136

    

    # def get_cat_list(self):           #for now ignore this instance method,
    #     k = self.category
    #     breadcrumb = ["dummy"]
    #     while k is not None:
    #         breadcrumb.append(k.slug)
    #         k = k.parent

    #     for i in range(len(breadcrumb)-1):
    #         breadcrumb[i] = '/'.join(breadcrumb[-1:i-1:-1])
    #     return breadcrumb[-1:0:-1]



    

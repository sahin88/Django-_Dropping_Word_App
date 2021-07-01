from django.db import models
from django.contrib.postgres.fields import ArrayField
import os


class Keys(models.Model):
    keys = ArrayField(models.CharField(max_length=50, blank=True),size=5,blank=True)
    docfile = models.FileField(upload_to='documents/%Y/%m/%d', blank=True, null=True)
   

    def __str__(self):
        return str(self.id)
    

    @property
    def get_keyword_property(self):
        return self.id

    @property
    def filename(self):
        return os.path.basename(self.docfile.name)
    @property
    def filesize(self):
        file_size=round(self.docfile.size/1000, 2)
        return ' {} kB'.format(file_size)
    @property
    def fileUrl(self):
        try:
            url = self.docfile.url
        except Exception as e:
            url = ''
        return url


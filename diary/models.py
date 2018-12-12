from django.db import models


class Diary(models.Model):
    diary_name = models.CharField(max_length = 80)
    created_date = models.DateTimeField('date created')
    def __str__(self):
        return self.diary_name

class Message(models.Model):
    
    diary = models.ForeignKey(Diary, on_delete=models.CASCADE)
    post_text = models.CharField(max_length = 200)
    posted_date = models.DateTimeField('date posted')
    def __str__(self):
        return self.post_text
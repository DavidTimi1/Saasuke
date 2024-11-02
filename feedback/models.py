
from django.utils import timezone
from django.db import models


# Create your models here.
class FeedApp(models.Model):
    app = models.CharField(max_length=20)



class FeedForm(models.Model):
    appName = models.ForeignKey(FeedApp, on_delete=models.SET_NULL, null=True, related_name="feedback")
    author = models.CharField("author", max_length=30, null=True)
    date = models.DateTimeField("date published", default=timezone.now)
    email = models.EmailField("email", null=True)
    rating = models.IntegerField("rated", null=True)
    text = models.TextField()
    title = models.CharField(max_length=20)


    def __str__(self):
        return (
            f"""{self.appName} Feedback {self.title and ('- ' + self.title)}\n
            {self.text}\n\n
            { f'rated - {self.rating} stars' if self.rating else 'not rated' }
            """
        )
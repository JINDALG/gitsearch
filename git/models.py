from django.db import models
from django_extensions.db.models import TimeStampedModel


class User(TimeStampedModel):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField()
    name = models.CharField(max_length=50)
    image = models.URLField()
    followers_url = models.URLField()
    organizations_url = models.URLField()
    repos_url = models.URLField()
    company = models.CharField(max_length=50, blank=True, null=True)
    blog = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    public_repos = models.IntegerField(default=0)
    followers = models.IntegerField(default=0)
    following = models.IntegerField(default=0)
    account_created = models.DateField()

    def __str__(self):
        return self.username

    def get_image(self):
        return "<img src='{0}', height='50', width='50px'><img>".format(self.image)

    get_image.allow_tags = True
    get_image.short_description = 'Photo'

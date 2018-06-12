from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.urls import reverse #Generate urls by reversing the url pattern
import uuid
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_google_maps import fields as map_fields
from django_google_maps.fields import AddressField, GeoLocationField
from geoposition.fields import GeopositionField
from embed_video.fields import EmbedVideoField


# Create your models here.

class Genre(models.Model):
    '''
    Model representing a book genre
    '''
    name = models.CharField(max_length=200, help_text="Music Genre")

    def __str__(self):
        '''
        string for representing Model object(Admin Site)
        '''
        return self.name

class Song(models.Model):

    '''
    Model representing a song (not a specific one)
    '''

    title = models.CharField(max_length=200)
    artist = models.ForeignKey('Artist', on_delete=models.SET_NULL, null=True)
    #Foreign Key because Song can only have one Artist, but Artist has many songs
    #Author as a string rather than objects because it hasn't been declared yet in file
    album = models.TextField(max_length=200, help_text='Album Name')
    genre = models.ManyToManyField(Genre, help_text='Select Genre')
    # Many to Many because genre can contain many songs ang songs many genre's


    def get_absolute_url(self):
        '''
        returns the url to access a detail record for this song
        '''

        return reverse('song-detail', args=[str(self.id)])

    def __str__(self):

        return self.title

class SongInstance(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique for each song")
    song = models.ForeignKey('Song', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        '''
        string representing the Model object
        '''

        return '{0} ({1})'.format(self.id, self.book.title)

class Artist(models.Model):
    """
    Model representing an artist.
    """
    first_name = models.CharField(max_length=100)
    stage_name = models.CharField(max_length=100)


    class Meta:
        ordering = ["stage_name","first_name"]

    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('artist-detail', args=[str(self.id)])


    def __str__(self):
        """
        String for representing the Model object.
        """
        return '{0}, {1}'.format(self.stage_name,self.first_name)

    
    
class ProfilePic(models.Model):
    image = models.ImageField(upload_to='pictures', blank=True)  


class PointOfInterest(models.Model):
    name = models.CharField(max_length=100)
    position = GeopositionField()

    class Meta:
        verbose_name_plural = 'points of interest'  



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, default="")
    city = models.CharField(max_length=100, default="")
    website = models.URLField(default="")
    phone = models.IntegerField(default=0)
    image = models.ImageField(upload_to='pictures', blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)



class Post(models.Model):
    post = models.CharField(max_length=250)
    image = models.ImageField(upload_to='pictures', blank=True)

    def __str__(self):
        return '{0}<br>{1}'.format(self.post, self.image)


class Video(models.Model):
    title = models.CharField(max_length=50)
    video = EmbedVideoField(verbose_name='My video',
                            help_text='This is a help text')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('video-detail', kwargs={'pk': self.pk})




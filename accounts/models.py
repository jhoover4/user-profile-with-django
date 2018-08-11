from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    fav_animal = models.CharField(max_length=100, blank=True)
    hobby = models.CharField(max_length=100, blank=True)
    avatar = models.URLField()

    # TODO: Clean Avatar

    def clean(self):
        bio_length = 10

        if len(self.bio) <= bio_length:
            raise ValidationError("Bio data must be at least {} characters long.".format(bio_length))


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

import pytz
import uuid
from django.db import models
from cloudinary.models import CloudinaryField


class User(models.Model):
    user_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
        )
    mentor = models.BooleanField(default=False)
    mentee = models.BooleanField(default=True)
    display_name = models.CharField(
        blank=False, max_length=300,
        help_text='Include first name and last name here')
    about = models.TextField(max_length=1000, help_text='a brief description of you')
    avatar = CloudinaryField('image')
    stacks = models.ManyToManyField('Stack', related_name='stacks')

    PRONOUN_CHOICES = [
        ('They', 'They/Them'),
        ('She', 'She/Her'),
        ('He', 'He/Him')
    ]
    preferred_pronouns = models.CharField(
        max_length=5,
        choices=PRONOUN_CHOICES,
        null=False
    )
    spoken_languages = models.ManyToManyField('SpokenLanguage', related_name='speaks')
    website = models.URLField(max_length=200, blank=True)

    # Pytz Timezone package http://pytz.sourceforge.net/
    # https://stackoverflow.com/questions/47477109/how-to-store-timezones-efficiently-in-django-model
    ALL_TIMEZONES = sorted((item, item) for item in pytz.all_timezones)

    timezone = models.CharField(max_length=300, choices=ALL_TIMEZONES)
    availability = models.BooleanField(
        default=True,
        help_text='switch to false if you\'re not open to being matched'
        )

    def __str__(self):
        return self.display_name


class Stack(models.Model):
    name = models.CharField(max_length=100, null=False)

    STACK_PROFICIENCY = [
        ('B', 'Beginner'),
        ('I', 'Intermediate'),
        ('A', 'Advanced')
    ]
    proficiency = models.CharField(
        max_length=1,
        choices=STACK_PROFICIENCY,
        null=False
    )

    def __str__(self):
        return self.name


class SpokenLanguage(models.Model):
    name = models.CharField(max_length=100, null=False)

    LANGUAGE_PROFICIENCY = [
        ('NP', 'No Proficiency'),
        ('EP', 'Elementary Proficiency'),
        ('LWP', 'Limited Working Proficiency'),
        ('PWP', 'Professional Working Proficiency'),
        ('FWP', 'Full Working Proficiency'),
        ('NBP', 'Native Bilingual Proficiency')
    ]
    proficiency = models.CharField(
        max_length=3,
        choices=LANGUAGE_PROFICIENCY,
        null=False
    )

    def __str__(self):
        return self.name


class Request(models.Model):
    stack = models.ManyToManyField(Stack, related_name='tech_stacks')
    description = models.TextField(
        max_length=500,
        help_text='brief overview of what you\'d like to learn, your available days, etc'
        )
    mentee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='your_name')
    interested_mentors = models.ManyToManyField('InterestedMentor', blank=True, related_name='prospective_mentor')
    matched_mentor = models.ForeignKey(
        User,
        related_name='matched',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
        )

    def __str__(self):
        return self.mentee.display_name


class InterestedMentor(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    personalised_note = models.TextField(
        max_length=1000,
        blank=False,
        help_text='''say hi to your new mentee, include important details that you think
        will be helpful during the mentorship'''
        )
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return self.name.display_name

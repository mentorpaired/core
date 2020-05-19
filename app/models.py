import pytz
import uuid
from django.db import models
from cloudinary.models import CloudinaryField


def timezone():
    # Pytz Timezone package http://pytz.sourceforge.net/
    # https://stackoverflow.com/questions/47477109/how-to-store-timezones-efficiently-in-django-model
    return sorted((item, item) for item in pytz.all_timezones)


class Pronoun(models.Model):
    PRONOUNS = [
        ('They', 'They/Them'),
        ('She', 'She/Her'),
        ('He', 'He/Him')
    ]
    pronoun = models.CharField(
        max_length=20,
        choices=PRONOUNS
    )


class User(models.Model):
    user_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
        )
    role = models.ManyToManyField('Role', related_name='roles')
    display_name = models.CharField(
        blank=False, max_length=300,
        help_text='Include first name and last name here'
    )
    about = models.TextField(
        max_length=1000,
        help_text='a brief description of you'
    )
    avatar = CloudinaryField('image')
    skills = models.ManyToManyField('Skill', related_name='skills')
    pronoun = models.ForeignKey(Pronoun, on_delete=models.CASCADE,
                                null=True, blank=True)
    spoken_languages = models.ManyToManyField('SpokenLanguage',
                                              related_name='languages')
    website = models.URLField(max_length=200, blank=True)

    timezone = models.CharField(max_length=300, choices=timezone())
    availability = models.BooleanField(
        default=True,
        help_text='switch to false if you\'re not open to being matched'
        )

    def __str__(self):
        return self.display_name


class Role(models.Model):
    ROLES = [
        ('ADMIN', 'admin'),
        ('MENTOR', 'mentor'),
        ('MENTEE', 'mentee')
    ]
    role = models.CharField(max_length=20,
                            choices=ROLES,
                            default='MENTEE')


class SkillProficiency(models.Model):
    PROFICIENCY = [
        ('B', 'Beginner'),
        ('I', 'Intermediate'),
        ('A', 'Advanced')
    ]

    level = models.CharField(
        max_length=3,
        choices=PROFICIENCY,
        null=False,
        unique=True
    )

    def __str__(self):
        return self.level


class Skill(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)

    proficiency = models.ForeignKey(SkillProficiency, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class LanguageProficiency(models.Model):
    PROFICIENCY = [
        ('NP', 'No Proficiency'),
        ('EP', 'Elementary Proficiency'),
        ('LWP', 'Limited Working Proficiency'),
        ('PWP', 'Professional Working Proficiency'),
        ('FWP', 'Full Working Proficiency'),
        ('NBP', 'Native Bilingual Proficiency')
    ]

    level = models.CharField(
        max_length=5,
        choices=PROFICIENCY,
        null=False,
        unique=True
    )

    def __str__(self):
        return self.level


class SpokenLanguage(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)

    proficiency = models.ForeignKey(LanguageProficiency,
                                    on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Request(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE),
    description = models.TextField(
        max_length=500,
        help_text='brief overview of what you\'d \
                  like to learn, your available days, etc'
    )
    mentee = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='mentee')

    mentor = models.ForeignKey(User, on_delete=models.CASCADE, null=True,
                               blank=True, related_name='mentor')

    STATUSES = [
        ('OPEN', 'open'),
        ('HAS_INTERESTS', 'has_interests'),
        ('COMPLETED', 'completed'),
        ('CLOSED', 'closed')
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUSES,
        default='OPEN'
    )

    def __str__(self):
        return self.requester.display_name


class RequestInterest(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='mentor'),

    description = models.TextField(
        max_length=500,
        help_text='Introduce yourself to the request creator'
    )

    STATUSES = [
        ('OPEN', 'open'),
        ('ACCEPTED', 'accepted'),
        ('REJECTED', 'rejected'),
        ('WITHDRAWN', 'withdrawn')
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUSES,
        default='OPEN'
    )

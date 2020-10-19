"""
Models
"""
import typing
import uuid

import pytz
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _


def timezone() -> typing.Generator[tuple, None, None]:
    """ Build timezone table """
    # Pytz Timezone package http://pytz.sourceforge.net/
    # https://stackoverflow.com/questions/47477109/how-to-store-timezones-efficiently-in-django-model
    return sorted((item, item) for item in pytz.all_timezones)


class Pronoun(models.Model):
    """ Pronoun model """

    PRONOUNS = [("They", "They/Them"), ("She", "She/Her"), ("He", "He/Him")]
    pronoun = models.CharField(max_length=20, choices=PRONOUNS)

    def __str__(self) -> str:
        """ object string representation """
        return str(self.pronoun)


class User(AbstractUser):
    """ User model """

    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(_("email address"), unique=True, blank=False, null=False)
    role = models.ManyToManyField("Role", related_name="roles")
    about = models.TextField(max_length=1000, help_text="a brief description of you")
    avatar = models.URLField(null=True, blank=True)
    skills = models.ManyToManyField("Skill", related_name="skills")
    pronoun = models.ForeignKey(
        Pronoun, on_delete=models.CASCADE, null=True, blank=True
    )
    spoken_languages = models.ManyToManyField(
        "SpokenLanguage", related_name="languages"
    )
    website = models.URLField(max_length=200, blank=True)

    timezone = models.CharField(max_length=300, choices=timezone())
    availability = models.BooleanField(
        default=True, help_text="switch to false if you are not open to being matched"
    )

    def __str__(self):
        """ object string representation """
        return self.username


class Role(models.Model):
    """ Role model """

    ROLES = [("ADMIN", "admin"), ("MENTOR", "mentor"), ("MENTEE", "mentee")]
    role = models.CharField(max_length=20, choices=ROLES, default="MENTEE")

    def __str__(self) -> str:
        """ object string representation """
        return str(self.role)


class SkillProficiency(models.Model):
    """ SkillProficiency model """

    PROFICIENCY = [("B", "Beginner"), ("I", "Intermediate"), ("A", "Advanced")]

    level = models.CharField(max_length=3, choices=PROFICIENCY, null=False, unique=True)

    def __str__(self) -> str:
        """ object string representation """
        return str(self.level)


class Skill(models.Model):
    """ Skill model """

    name = models.CharField(max_length=100, null=False, unique=True)

    proficiency = models.ForeignKey(SkillProficiency, on_delete=models.CASCADE)

    def __str__(self) -> str:
        """ object string representation """
        return str(self.name)


class LanguageProficiency(models.Model):
    """ LanguageProficiency model """

    PROFICIENCY = [
        ("NP", "No Proficiency"),
        ("EP", "Elementary Proficiency"),
        ("LWP", "Limited Working Proficiency"),
        ("PWP", "Professional Working Proficiency"),
        ("FWP", "Full Working Proficiency"),
        ("NBP", "Native Bilingual Proficiency"),
    ]

    level = models.CharField(max_length=5, choices=PROFICIENCY, null=False, unique=True)

    def __str__(self) -> str:
        """ object string representation """
        return str(self.level)


class SpokenLanguage(models.Model):
    """ SpokenLanguage model """

    name = models.CharField(max_length=100, null=False, unique=True)

    proficiency = models.ForeignKey(LanguageProficiency, on_delete=models.CASCADE)

    def __str__(self) -> str:
        """ object string representation """
        return str(self.name)


class Request(models.Model):
    """ Request model """

    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    description = models.TextField(
        max_length=500,
        help_text="brief overview of what you would like to learn, your available days, etc",
    )
    mentee = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mentee")

    mentor = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, related_name="mentor"
    )

    STATUS = [
        ("OPEN", "open"),
        ("HAS_INTERESTS", "has_interests"),
        ("COMPLETED", "completed"),
        ("CLOSED", "closed"),
    ]

    status = models.CharField(max_length=20, choices=STATUS, default="OPEN")

    def __str__(self) -> str:
        """ object string representation """
        return self.mentee.username


class RequestInterest(models.Model):
    """ RequestInterest model """

    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    mentor = models.ForeignKey(User, on_delete=models.CASCADE, default="")

    description = models.TextField(
        max_length=500, help_text="Introduce yourself to the request creator"
    )

    STATUS = [
        ("OPEN", "open"),
        ("ACCEPTED", "accepted"),
        ("REJECTED", "rejected"),
        ("WITHDRAWN", "withdrawn"),
    ]

    status = models.CharField(max_length=20, choices=STATUS, default="OPEN")

    def __str__(self) -> str:
        return f"Interest from {self.mentor.username}"

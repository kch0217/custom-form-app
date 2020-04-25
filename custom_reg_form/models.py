from django.conf import settings
from django.db import models

# Backwards compatible settings.AUTH_USER_MODEL
USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class ExtraInfo(models.Model):
    """
    This model contains two extra fields that will be saved when a user registers.
    The form that wraps this model is in the forms.py file.
    """
    user = models.OneToOneField(USER_MODEL, null=True)
    AGE_GROUP = (
        ('below18', 'Below 18'),
        ('18_24', '18 - 24'),
        ('25_40', '25 - 40'),
        ('41_60', '41 - 60'),
        ('up60', 'Above 60')
    )

    GENDER_GROUP = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    TENURE_GROUP = (
        ('0t', '0'),
        ('1_3t','1 - 3'),
        ('4_6t', '4 - 6'),
        ('7_9t', '7 - 9'),
        ('10t', '10+')
    )

    your_age = models.CharField(
        verbose_name="Age Group",
        choices=AGE_GROUP,
        max_length=50,
    )

    your_gender = models.CharField(
        verbose_name="Gender",
        choices=GENDER_GROUP,
        max_length=50,
    )

    your_tenure = models.CharField(
        verbose_name="Job Tenure",
        choices=TENURE_GROUP,
        max_length=50,
    )




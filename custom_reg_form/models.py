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

    EMPLOYMENT_GROUP = (
        ('engineering', 'Engineering'),
        ('banking_finance', 'Banking / finance'),
        ('administration_management', 'Administration / management'),
        ('SA_CP', 'System analysis and computer programming'),
        ('accounting_auditing_taxation','Accounting / auditing / taxation'),
        ('marketing_sales','Marketing / sales'),
        ('teaching_lecturing', 'Teaching / lecturing'),
        ('scientific_research','Scientific / research work'),
        ('service_work', 'Service work'),
        ('health_medical_services', 'Health / medical services'),
        ('aircraft_and_marine', 'Aircraft and marine'),
        ('clerical_work', 'Clerical work'),
        ('insurance_res', 'Insurance / real estate services'),
        ('protective_services', 'Protective services'),
        ('economic_smw', 'Economic, statistical and mathematical work'),
        ('merchandise', 'Merchandising / purchasing'),
        ('art_design', 'Art and design'),
        ('author_journalist', 'Author / journalist'),
        ('advertising_pr', 'Advertising / public relations'),
        ('architecture_surveying', 'Architecture / surveying'),
        ('legal_service', 'Legal service'),
        ('social_services','Social services'),
        ('others', 'Others')

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

    your_employment = models.CharField(
        verbose_name="Employment sector",
        choices=EMPLOYMENT_GROUP,
        max_length=50,
    )

    your_tenure = models.CharField(
        verbose_name="Job Tenure",
        choices=TENURE_GROUP,
        max_length=50,
    )






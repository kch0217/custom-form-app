from .models import ExtraInfo
from django.forms import ModelForm

class ExtraInfoForm(ModelForm):
    """
    The fields on this form are derived from the ExtraInfo model in models.py.
    """
    def __init__(self, *args, **kwargs):
        super(ExtraInfoForm, self).__init__(*args, **kwargs)
        self.fields['your_age'].error_messages = {
            "required": u"Please tell us your age group.",
            "invalid": u"Please tell us your age group.",
        }
        self.fields['your_gender'].error_messages = {
            "required": u"Please tell us your gender.",
            "invalid": u"Please tell us your gender.",
        }

        self.fields['your_employment'].error_messages = {
            "required": u"Please tell us your employment sector.",
            "invalid": u"Please tell us your employment sector.",
        }

        self.fields['your_tenure'].error_messages = {
            "required": u"Please tell us your job tenure.",
            "invalid": u"Please tell us your job tenure.",
        }

    class Meta(object):
        model = ExtraInfo
        fields = ('your_age', 'your_gender', 'your_employment', 'your_tenure')

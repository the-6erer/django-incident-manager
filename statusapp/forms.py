from django.forms import ModelForm, BaseInlineFormSet, HiddenInput
from .models import *
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator, validate_email
from django.utils.timezone import now

class IncidentForm(ModelForm):
    class Meta:
        model = Incident
        #fields = '__all__'
        exclude = ['closed', 'start', 'end']

    def clean(self):
        cleaned_data = super().clean()
        end = cleaned_data.get("end")
        start = cleaned_data.get("start")
        closed = cleaned_data.get("closed")

        if end:
            if end < start and end < now():# and active:
                raise ValidationError(
                    "End timestamp passed already "
                    "The incident cannot be active anymore"
                )

class NotificationForm(ModelForm):
    class Meta:
        model = Notification
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        topic = cleaned_data.get("topic")
        all_topic = cleaned_data.get("all_topic")
        subject = cleaned_data.get("subject")
        address = cleaned_data.get("address")
        notification = cleaned_data.get("notification")

        if not (topic or all_topic):
            raise ValidationError('Either select single topics or check the box "All topics"')

        #unselect single topics if all_topics is selected
        if topic and all_topic:
            self.cleaned_data['topic'] = []

        if notification == 'TEAMS':
            try:
                validator = URLValidator()
                validator(address)
            except ValidationError:
                self.add_error('address', 'Enter a valid URL')
        elif notification == 'EMAIL':
            try:
                validate_email(address)
            except ValidationError:
                self.add_error('address', 'Enter a valid Email address')

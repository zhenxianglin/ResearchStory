from django import forms

from Meetings.models import Meeting


class MeetingForm(forms.ModelForm):
    monday = forms.BooleanField()
    tuesday = forms.BooleanField()
    wednesday = forms.BooleanField()
    thursday = forms.BooleanField()
    friday = forms.BooleanField()
    saturday = forms.BooleanField()
    sunday = forms.BooleanField()

    class Meta:
        model = Meeting
        fields = ('meeting_name',
                  'meeting_link',
                  'start_time',
                  'end_time',
                  )

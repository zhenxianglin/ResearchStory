from django import forms

from meeting.models import Link


class MeetingForm(forms.ModelForm):
    # monday = forms.BooleanField()
    # tuesday = forms.BooleanField()
    # wednesday = forms.BooleanField()
    # thursday = forms.BooleanField()
    # friday = forms.BooleanField()
    # saturday = forms.BooleanField()
    # sunday = forms.BooleanField()

    class Meta:
        model = Link
        fields = ('meeting_name',
                  'meeting_link',
                  'start_time',
                  'end_time',

                  'monday',
                  'tuesday',
                  'wednesday',
                  'thursday',
                  'friday',
                  'saturday',
                  'sunday',
                  )

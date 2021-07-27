from django import forms

from interview.models import Interview


class InterviewForm(forms.ModelForm):
    class Meta:
        model = Interview
        fields = ('interview_name',

                  'interview_link',
                  'start_time',
                  'end_time',

                  'monday',
                  'tuesday',
                  'wednesday',
                  'thursday',
                  'friday',
                  )

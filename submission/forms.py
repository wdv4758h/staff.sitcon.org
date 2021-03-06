from django import forms
from submission.models import Submission, SubmissionFile

class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = '__all__'
        exclude = ('status',)

class SubmissionFileForm(forms.ModelForm):
    class Meta:
        model = SubmissionFile
        fields = '__all__'

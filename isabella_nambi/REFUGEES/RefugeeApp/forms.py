from django import forms
from django.utils import timezone

from . import models

class BeneficiaryForm(forms.ModelForm):
    first_name = forms.CharField(min_length=2, max_length=100, required=True)
    last_name = forms.CharField(min_length=2, max_length=100, required=True)
    place_of_birth = forms.CharField(min_length=2, max_length=100, required=True)
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=True)
    date_of_joining_settlement = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=True)
    gender = forms.ChoiceField(choices=models.GENDER_CHOICES, widget=forms.RadioSelect(attrs={'class': 'radio-horizontal'}))
    nationality = forms.ChoiceField(choices=models.NATIONALITY_CHOICES, required=True)
    marital_status = forms.ChoiceField(choices=models.MARITAL_STATUS_CHOICES, required=True)
    settlement_camp = forms.ChoiceField(choices=models.SETTLEMENT_CAMP_CHOICES, required=True)

    class Meta:
        model = models.Beneficiary
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        today = timezone.localdate()
        self.fields['date_of_birth'].widget.attrs['max'] = (today - timezone.timedelta(days=1)).isoformat()
        self.fields['date_of_joining_settlement'].widget.attrs['max'] = today.isoformat()

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data['date_of_birth']
        if date_of_birth >= timezone.localdate():
            raise forms.ValidationError('Date of birth must be before today.')
        return date_of_birth

    def clean_date_of_joining_settlement(self):
        date_of_joining = self.cleaned_data['date_of_joining_settlement']
        if date_of_joining > timezone.localdate():
            raise forms.ValidationError('Date of joining settlement cannot be later than today.')
        return date_of_joining
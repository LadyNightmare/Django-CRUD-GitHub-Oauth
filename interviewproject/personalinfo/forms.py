from django.forms import ModelForm, CharField, DateInput

from .models import PersonalInfo


class PersonalInfoForm(ModelForm):
    address = CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['address'].initial = kwargs['instance'].address if kwargs.get('instance') else ''


    class Meta:
        model = PersonalInfo
        fields = ['address',
                  'title',
                  'name',
                  'surname',
                  'birth_date',
                  'nationality',
                  'phone_number']
        widgets = {
            'birth_date': DateInput(attrs={'type': 'date'})
        }

    def save(self, commit=True):
        self.instance.address = self.cleaned_data['address']
        super().save(commit)
        return self.instance
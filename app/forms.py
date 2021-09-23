from django import forms
from django.core import validators
def check_for_a(value):
    if value[0].lower()=='a':
        raise forms.ValidationError('name should not start with a')

def check_for_len(value):
    if len(value)>5:
        raise forms.ValidationError('length is more than 5')

def check_for_age(value):
    if value<18 or value>45:
        raise forms.ValidationError('age is less than 18')


class StudentForm(forms.Form):
    name=forms.CharField(max_length=100,validators=[check_for_a,validators.MaxLengthValidator(5)])
    age=forms.IntegerField(validators=[check_for_age])
    mobile=forms.CharField(validators=[validators.RegexValidator('[6-9]\d{9}')])
    #email=forms.EmailField(max_length=100)
    #reenteremail=forms.EmailField(max_length=100)
    botcatcher=forms.CharField(max_length=100,required=False,widget=forms.HiddenInput)

    def clean_botcatcher(self):
        bot=self.cleaned_data['botcatcher']
        if len(bot)>=1:
            raise forms.ValidationError('Bot has Catched')
    
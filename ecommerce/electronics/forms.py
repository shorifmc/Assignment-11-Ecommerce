from django import forms

class ElectronicsRegistration(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField(label_suffix="*")
    batch = forms.IntegerField(help_text="Must fil the bathc")
    rollno = forms.IntegerField( label='Class Roll ', required=False)


    
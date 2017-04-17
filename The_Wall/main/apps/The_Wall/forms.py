from django import forms

# form notes
# A Form instance has an is_valid() method
# returns True or False
# form's data is placed in cleaned_data attribute
class LoginForm(forms.Form):
    email = forms.CharField(label=
    'email', max_length=45)

# contact me form example
class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()

class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=45)
    last_name = forms.CharField(max_length=45)
    email = forms.EmailField()
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=100,widget=forms.PasswordInput)


# in views.py, form data is sent back to Django site (generally) using the same view which published the form.

#Working form process:
# Described by Django 'Form', processed by a view, rendered as an HTML <form>

# cleaned_data will be Python typed

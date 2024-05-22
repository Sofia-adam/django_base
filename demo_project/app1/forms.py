from django import forms

class student(forms.Form):
    student_id = forms.IntegerField(label="Student ID",help_text="Enter numerical values only")
    student_name = forms.CharField(label="Student Name",max_length=20)
    student_age = forms.IntegerField()
    Email = forms.EmailField(required=False)
    Password = forms.CharField(widget=forms.PasswordInput())

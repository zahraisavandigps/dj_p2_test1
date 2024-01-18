from django import forms
from django.contrib.auth.models import User

# class UserRegisterForm(forms.Form):
#     user_name=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder':'please user name'}))
#     email=forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'ایمیل خود را وارد کنید'}))
#     first_name=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder':'please user name'}))
#     last_name=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder':'please user name'}))
#     password1=forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={'placeholder':'please user name'}))
#     password2=forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={'placeholder':'repeat password'}))

class UserRegisterForm(forms.Form):
    user_name=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder':'please user name:'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'please email'}))
    first_name=forms.CharField(max_length=50)
    last_name=forms.CharField(max_length=50)
    password_1=forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={'placeholder':'پسورد خود را وارد کنید'}))
    password_2=forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={'placeholder':'تکرار پسورد'}))
#------------
    def clean_user_name(self):
        user=self.cleaned_data['user_name']
        if User.objects.filter(username=user).exists():
           raise forms.ValidationError('user exist')
        return user
#-------------
    def clean_email(self):
        email=self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('این ایمیل تکراری است')
        return email
#-----------
    def clean_password_2(self):
        password1=self.cleaned_data['password_1']
        password2=self.cleaned_data['password_2']
        if password1!=password2:
            raise forms.ValidationError('password not match.')
        elif len(password2)<8:
            raise forms.ValidationError('password was short.')
        elif not any (i.isupper() for  i in password2):
            raise forms.ValidationError('حداقل باید دارای یک حرف بزرگ باشد.')
        return password1

#------------------

class UserlogiForm(forms.Form):
    user=forms.CharField()
    password=forms.CharField()

#------------------changepassword
class ChangePasswordForm(forms.Form):
    old_password=forms.CharField(widget=forms.PasswordInput,label='پسورد فعلی')
    new_password1=forms.CharField(widget=forms.PasswordInput,label='پسورد جدید')
    new_password2=forms.CharField(widget=forms.PasswordInput,label='تکرار پسورد')

    # def clean_new_password1(self):
    #     password=self.cleaned_data['new_password1']
    #     # password = self.cleaned_data.get('new_password1')
    #     if len(password)<8:
    #         raise forms.ValidationError('پسورد نباید کمتر از 8 کاراکتر باشد.')
    #     return password
    #
    # def clean_new_password2(self):
    #     password1=self.cleaned_data['new_password1']
    #     password2=self.cleaned_data['new_password2']
    #     # password1 = self.cleaned_data.get('new_password1')
    #     # password2 = self.cleaned_data.get('new_password2')
    #     if password1!=password2:
    #         raise forms.ValidationError('پسوردها با هم مطابقت ندارند.')
    #     return password2

    # def clean_new_password2(self):
    #     password1 = self.cleaned_data.get('new_password1')
    #     password2 = self.cleaned_data.get('new_password2')
    #     if password1 != password2:
    #         raise forms.ValidationError('password not match.')
    #     elif len(password2) < 8:
    #         raise forms.ValidationError('password was short.')
    #     elif not any(i.isupper() for i in password2):
    #         raise forms.ValidationError('حداقل باید دارای یک حرف بزرگ باشد.')
    #     return password1
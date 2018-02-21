from django import forms
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField(max_length=120)
    text = forms.CharField(widget=forms.Textarea)

    def save(self):
        question = Question(**self.cleaned_data)
        question.author_id = self._user.id
        question.save()
        return question

class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput)

    def save(self):
        question = get_object_or_404(Question, pk=self.cleaned_data['question'])
        self.cleaned_data['question'] = question
        answer = Answer(**self.cleaned_data)
        answer.author_id = self._user.id
        answer.save()
        return answer

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        #error_message = 'Invalid username or password.'
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        try:
            user = User.objects.get(username=username)
            if not user.check_password(password):
                raise forms.ValidationError('Invalid username or password.')
        except User.DoesNotExist:
            raise forms.ValidationError('Invalid username or password.')
        return self.cleaned_data


class SignupForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('User with same "username" already exist.')
        return username

    def save(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        user = User.objects.create_user(username, email, password)
        user.save()
        return user
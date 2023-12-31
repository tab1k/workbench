from django import forms
from courses.models import *
from users.models import User, Stream


class StudentForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}))
    courses = forms.ModelMultipleChoiceField(queryset=Course.objects.all())
    stream = forms.ModelChoiceField(queryset=Stream.objects.all(), required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password', 'courses', 'stream']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['courses'].widget.attrs['class'] = 'form-control'
        self.fields['stream'].widget.attrs['class'] = 'form-select'  # Стилизуйте виджет выбора потока



class CuratorForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}))
    courses = forms.ModelMultipleChoiceField(queryset=Course.objects.all())

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password', 'courses']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['courses'].widget.attrs['class'] = 'form-control'



class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ['course', 'message', 'file']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course'].widget.attrs.update({'class': 'form-control'})
        self.fields['message'].widget.attrs.update({'class': 'form-control'})
        self.fields['file'].widget.attrs.update({'class': 'form-control-file'})



from courses.models import *
from django import forms
from django.contrib.auth import get_user_model

class CourseForm(forms.ModelForm):
    curators = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.filter(groups__name='Кураторы'),  # Filter users with the 'Кураторы' group
        required=False
    )

    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)

        self.fields['title'].label = 'Название'
        self.fields['description'].label = 'Описание'
        self.fields['duration'].label = 'Длительность'
        self.fields['course_type'].label = 'Тип курса'
        self.fields['curators'].label = 'Кураторы'
        self.fields['image'].label = 'Изображение'

        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Course
        fields = ['title', 'description', 'duration', 'course_type', 'curators', 'image']


class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = ['title', 'description', 'order', 'course']

    def __init__(self, *args, **kwargs):
        super(ModuleForm, self).__init__(*args, **kwargs)

        self.fields['title'].label = 'Название'
        self.fields['description'].label = 'Описание'
        self.fields['order'].label = 'Длительность'
        self.fields['course'].label = 'Курс'

        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})




from django import forms
from .models import Topic

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'What is on your mind?'}
        ),
        max_length=4000,
        help_text="<span text-color='red' >The max length of the text is 4000.</span>"
    )

    class Meta:
        model = Topic
        fields = ['subject', 'message']
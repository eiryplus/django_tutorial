from django import forms
from crud.models import Message


class MessageForm(forms.ModelForm):
    message = forms.CharField(
        label='メッセージ',
        max_length=255,
        required=True,
        widget=forms.TextInput()
    )

    class Meta:
        model = Message
        fields = [
            "message",
        ]

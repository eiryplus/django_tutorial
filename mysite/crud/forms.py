from django import forms


class MessageForm(forms.Form):
    message = forms.CharField(
        label='メッセージ',
        max_length=255,
        required=True,
        widget=forms.TextInput()
    )

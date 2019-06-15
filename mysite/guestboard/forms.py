from django import forms
from .models import Posting


class PostingForm(forms.ModelForm):
    class Meta:
        model = Posting
        fields = ("name", "message")
        widgets = {
            "name": forms.TextInput(
                attrs={"size": 40, "class": "form-control"},

            ),
            "message": forms.Textarea(
                attrs={"cols": 40, "rows": 5, "class": "form-control"}
            ),
        }
        error_messages = {
            "name": {
                "required": "名前を入力してください。",
            },
            "message": {
                "required": "メッセージを入力してください。",
            },
        }

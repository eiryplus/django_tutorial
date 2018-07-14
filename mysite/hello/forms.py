from django import forms


class HelloForm(forms.Form):
    your_name = forms.CharField(
        label='名前',
        max_length=10,
        required=True,
        widget=forms.TextInput()
    )

EMPTY_CHOICES = (
    ('', '-'*10),
)

GENDER_CHOICES = (
    ('man', '男'),
    ('woman', '女')
)

FOOD_CHOICES = (
    ('apple', 'りんご'),
    ('beef', '牛肉'),
    ('bread', 'パン'),

)


class SampleForm(forms.Form):
    age = forms.IntegerField(
        label='年齢',
        min_value=0,
        max_value=200,
        required=True,
    )

    birthday = forms.DateField(
        label='生年月日',
        required=True,
        input_formats=[
            '%Y-%m-%d',  # 2010-01-01
            '%Y/%m/%d',  # 2010/01/01
        ]
    )

    send_message = forms.BooleanField(
        label='送信する',
        required=False,
    )

    gender_r = forms.ChoiceField(
        label='性別',
        widget=forms.RadioSelect,
        choices=GENDER_CHOICES,
        required=True,
    )

    gender_s = forms.ChoiceField(
        label='性別',
        widget=forms.Select,
        choices=EMPTY_CHOICES + GENDER_CHOICES,
        required=False,
    )

    food_s = forms.ChoiceField(
        label='食べ物',
        widget=forms.SelectMultiple,
        choices=FOOD_CHOICES,
        required=True,
    )

    food_c = forms.ChoiceField(
        label='食べ物',
        widget=forms.CheckboxSelectMultiple,
        choices=FOOD_CHOICES,
        required=True,
    )
from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='名前', max_length=100)
    email = forms.EmailField(label='メール', max_length=100)
    message = forms.CharField(
        label='お問い合わせ内容',
        widget=forms.Textarea(attrs={'placeholder':'お問い合わせ内容'}),
        max_length=1000
    )
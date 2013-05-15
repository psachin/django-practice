from django import forms

TOPIC_CHOICES = (
    ('general', 'General Enquiry'),
    ('bugs','Bug Report'),
    ('suggestions','Suggestions'),
    )

class ContactForm(forms.Form):
    topic = forms.ChoiceField(choices=TOPIC_CHOICES)
    message = forms.CharField(widget=forms.Textarea(),initial="Your feedback")
    sender = forms.EmailField(required=False, initial="user@email.com")

    def clean_message(self):
        message = self.cleaned_data.get('message','')
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError('Not enough words!')
        return message


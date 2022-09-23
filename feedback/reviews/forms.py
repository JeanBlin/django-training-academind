from django import forms
from .models import Review

# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label='Your Name', max_length=100, required=True, error_messages={
#         'required':'Your name must not be empty.',
#         'max_lenght':'Sorry, the maz length is 100 characters.'
#     })

#     review_text = forms.CharField(label='your feedback', widget=forms.Textarea, max_length=200)

#     ratings = forms.IntegerField(label='your rating', min_value=1, max_value=5 )

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        # exclude = ['Which field I don't want to render in the form']

from django import forms
from . models import PropertyReview

class PropertyReviewForm(forms.ModelForm):
    class Meta:
        model = PropertyReview
        fields = ['feedback']
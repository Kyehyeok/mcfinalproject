from django.forms import ModelForm

from profileapp.models import Profile

class ProfilecreationForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image','nickname','message']
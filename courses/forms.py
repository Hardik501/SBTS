from django import forms
from django.forms.models import inlineformset_factory
from .models import Module, Course

ModuleFormSet = inlineformset_factory(Course,
                                        Module,
                                        fields=['title', 'desc'],
                                        extra=2, can_delete=True
                                    )



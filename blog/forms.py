from django.forms import ModelForm, Textarea

from .models import Entry

class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ["title", 
                  "body_text", 
                  "tags"
                  ]
        widgets = {
            'body_text': Textarea(),
        }
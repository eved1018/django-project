from django import forms

class PDBForm(forms.Form):
    pdb = forms.CharField(label=False)
    
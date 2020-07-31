from django import forms



class PDBForm(forms.Form):
    pdb = forms.CharField(label=False)

class FileForm(forms.Form):
    file = forms.FileField(label=False)

    
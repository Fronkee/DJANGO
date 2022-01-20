from dataclasses import field
from django import forms
from .models import SubCategory,Category

class CatForm(forms.ModelForm):
    class Meta:
        model= Category
        fields = '__all__'
        labels ={
            'name':'Choose Name',
            'image' :'Choose Image'
        }
    
    def __init__(self,*args,**kwargs):
        super(CatForm,self).__init__(*args,**kwargs)
        self.fields['name'].required = False
        
class SubCatFrom(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = '__all__'
        labels ={
            'name':'Category Name',
            'image':'Choose Image',
            'parent':'Category'
        }
    def __init__(self,*args,**kwagrs):
        super(SubCatFrom,self).__init__(*args,**kwagrs)
        self.fields['name'].required = False    
        self.fields['image'].required = False    
        self.fields['parent'].required = False    
        self.fields['parent'].empty_label= 'Select'    
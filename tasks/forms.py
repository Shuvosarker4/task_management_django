from django import forms
from tasks.models import Task,TaskDetail

class StyleFormMixin:
    default_classes ="border-2 my-2 w-full p-3 rounded-lg shadow-sm "
    def apply_style_widgets(self):
        for field_name,field in self.fields.items():
            if isinstance(field.widget,forms.TextInput):
                field.widget.attrs.update({
                    'class':self.default_classes,
                    'placeholder':f"Enter {field.label.lower()}"
                })
            elif isinstance(field.widget,forms.Textarea):
                field.widget.attrs.update({
                    'class':self.default_classes,
                    'placeholder':f"Enter {field.label.lower()}"
                })
            elif isinstance(field.widget, forms.SelectDateWidget):
                field.widget.attrs.update({
                    'class': "border-2 my-2 border-gray-300 p-3 rounded-lg shadow-sm focus:outline-none focus:border-rose-500 focus:ring-rose-500"
                })
            elif isinstance(field.widget, forms.CheckboxSelectMultiple):
                field.widget.attrs.update({
                    'class': "space-y-4"
                })


class TaskModelForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model= Task
        fields= ['title','description','project','due_date','assigned_to']
        widgets ={
            'due_date':forms.SelectDateWidget(),
            'assigned_to':forms.CheckboxSelectMultiple(),
            'project':forms.RadioSelect()
        }
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.apply_style_widgets()

class TaskDetailModelForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = TaskDetail
        fields = ['priority', 'notes']

    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        self.apply_style_widgets()

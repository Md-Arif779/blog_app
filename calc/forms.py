from django import forms
from .models import Post,Category,Comment

choice = Category.objects.all().values_list('name','name')
choice_list= []
for item in choice:
   choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
      model = Post
      fields = ['title','category', 'body','post_image']

   #  widgets = {
   #      'title': forms.TextInput(attrs={'class': 'form-control', 'placehoder': 'This is Title writte'}),
   #      'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
   #      'body': forms.Textarea(attrs={'class': 'form-control'})
   #            }

class UpdateForm(forms.ModelForm):
   class Meta:
      model = Post
      fields = ['author','title', 'body']


class CommentForm(forms.ModelForm):
   class Meta:
      model = Comment
      fields = ['name', 'body']      
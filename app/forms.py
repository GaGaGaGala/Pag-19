from django import forms
class PostForm(forms.ModelForm):
    title = forms.ModelChoiceField(queryset=Post.objects.all())
    content = forms.ModelTextField(queryset=Post.objects.all())
    created_at = forms.ModelDateTimeField(auto_now_add=True, queryset=Post.objects.all())

    class Meta:
        model = Post
        fields = ['title', 'content', 'created_at']
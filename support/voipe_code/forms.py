from django import forms


roles = [('admin','مدیر کل'),('supoort','پشتیبان')]


class add_user(forms.Form):

    username=forms.CharField(widget=forms.TextInput(
        attrs={'placeholder':'نام کاربری','class':'form-control'}),
        label='نام کاربری '
    )

    firstname=forms.CharField(widget=forms.TextInput(
        attrs={'placeholder':'نام و نام خانوادگی','class':'form-control'}),
        label=' نام و نام خانوادگی'
    )
    voipe_code=forms.IntegerField(widget=forms.TextInput(
        attrs={'placeholder':'داخلی','class':'form-control'}),
        label='داخلی'
    )

    password=forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder':'رمز عبور را وارد کنید','class':'form-control'}),
        label='رمز عبور'
    )

    user_role = forms.ChoiceField(
        required=False,
        widget=forms.Select(attrs={'class':'form-control'}),
        choices=roles,label='نقش کاربری'
    )







class edit_user(forms.Form):

    username=forms.CharField(widget=forms.TextInput(
        attrs={'placeholder':'نام کاربری','class':'form-control'}),
        label='نام کاربری '
    )

    firstname=forms.CharField(widget=forms.TextInput(
        attrs={'placeholder':'نام و نام خانوادگی','class':'form-control'}),
        label=' نام و نام خانوادگی'
    )
    voipe_code=forms.IntegerField(widget=forms.TextInput(
        attrs={'placeholder':'داخلی','class':'form-control'}),
        label='داخلی'
    )

    user_role = forms.ChoiceField(
        required=False,
        widget=forms.Select(attrs={'class':'form-control'}),
        choices=roles,label='نقش کاربری'
    )
    
    
    
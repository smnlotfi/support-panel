from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class user_voipecode(models.Model):

    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    voipe_code=models.CharField(max_length=50)
    is_admin=models.BooleanField(default=False)

    def __str__(self):
        return self.voipe_code
    
    class Meta:
        verbose_name="کد تلفن"
        verbose_name_plural="کد های تلفن"
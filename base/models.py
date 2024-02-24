from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()


class History(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.CharField(max_length=1000,blank=True,null=True)
    flipkart=models.TextField(max_length=20000)
    amazon=models.TextField(max_length=20000)
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.product
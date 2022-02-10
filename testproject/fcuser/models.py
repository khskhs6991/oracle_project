from django.db import models
# Create your models here.

class Fcuser(models.Model):
#    username = models.CharField(max_length = 64,
#                                verbose_name='사용자명')
#    useremail = models.EmailField(max_length = 128,
#                                verbose_name='사용자이메일')
#    password = models.CharField(max_length = 64,
#                                verbose_name = '비밀번호')
#    registered_dttm = models.DateTimeField(auto_now_add=True,
#                                            verbose_name='등록시간')

    name = models.CharField(max_length = 64,
                                verbose_name='사용자명')
    phonenumber = models.IntegerField(verbose_name='사용자번호')
    password = models.CharField(max_length = 128,
                                verbose_name = '비밀번호')
    re_password = models.CharField(max_length = 128, verbose_name='비밀번호확인')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='가입 시간')
    def __str__(self):
        return self.name


    class Meta:
        db_table = 'Test_fcuser'
        verbose_name = '디잔고 사용자'
        verbose_name_plural = '디잔고 사용자'





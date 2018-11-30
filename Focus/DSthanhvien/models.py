from django.db import models

# Create your models here.

class Danhsach(models.Model):
    Name = models.CharField(max_length=250)
    Mssv = models.CharField(max_length=300)
    Class = models.CharField(max_length=250)
    
    def __str__(self):
        return self.Mssv + ' - ' + self.Name

class Thongtin(models.Model):
    danhsach = models.ForeignKey(Danhsach, on_delete=models.CASCADE)
    Ngaysinh = models.CharField(max_length=250)
    Sothich = models.CharField(max_length=250)
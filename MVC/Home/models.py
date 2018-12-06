from django.db import models

class Danhsach_CoTruong(models.Model):
    Name = models.CharField(max_length=250)
    Specialized = models.CharField(max_length=300)
    Level = models.CharField(max_length=250)


    def __str__(self):
        return self.Specialized + ' - ' + self.Name

class Thongtin(models.Model):
    danhsach = models.ForeignKey(Danhsach_CoTruong, on_delete=models.CASCADE)
    Ngaysinh = models.CharField(max_length=250)
    Sothich = models.CharField(max_length=250)
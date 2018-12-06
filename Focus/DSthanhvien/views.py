from django.shortcuts import render
from DSthanhvien.models import Danhsach
# Create your views here.
def list(request):
    name = {Danhsachs = 'Danhsach.objects.all()'}
    return(render(request,'DSthanhvien/DSthanhvien.html',name))

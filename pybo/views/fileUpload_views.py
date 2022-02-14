#----------------------------------- 신규 업로드 파일 
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect

from ..forms import FileUploadForm
from ..models import FileUpload

@login_required(login_url='common:login')

def fileUpload(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        img = request.FILES["imgfile"]
        fileupload = FileUpload(
            title=title,
            content=content,
            imgfile=img,
        )
        fileupload.save()
        return redirect('fileupload')
    else:
        fileuploadForm = FileUploadForm
        context = {
            'fileuploadForm': fileuploadForm,
        }
        return render(request, 'question_form.html', context)
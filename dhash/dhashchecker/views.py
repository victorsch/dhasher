from django.shortcuts import render
from dhashchecker.models import File
from urllib import parse
from django.views.decorators.csrf import csrf_exempt

totalFilesList = File.objects.all()

# Create your views here.
@csrf_exempt
def index(request):
    if(request.method == "POST"):
        form_data = parse.urlsplit(request.body.decode('utf-8')).path
        file_hash = parse.parse_qs(form_data)['file_hash'][0]

        file_query = File.objects.filter(file_hash=file_hash)

        for file in file_query:
            print(file.file_name)


    return render(request, 'index.html', {

    })

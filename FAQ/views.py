from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.shortcuts import redirect
import time



# <----> require no privileged

def addQuestionPage(request):
    qtn_list=Question.objects.all().order_by('-created_at')
    context={'st_question':None,'qtn_list':qtn_list}
    return render(request,'add_question.html',context)

@csrf_exempt
def addQestion(request):
    qtn=Question(
        question=request.POST.get('question'),
        answer=request.POST.get('answer'),
        parent=request.POST.get('parent'),
        created_at=datetime.now())
    qtn.save()
    qtn_list=Question.objects.all().order_by('-created_at')
    context={'st_question':qtn,'qtn_list':qtn_list}
    return render(request,'add_question.html',context)


def detailOnQestion(request,qt_id):
    context={
        'st_qt':Question.objects.get(id=qt_id),
        'qtn_list':Question.objects.all().order_by('-created_at'),
        'related_qt':Question.objects.filter(parent=Question.objects.get(id=qt_id).question),
        }
    return render(request,'add_question.html',context)



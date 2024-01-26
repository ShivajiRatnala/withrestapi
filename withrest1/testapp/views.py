import io

from django.shortcuts import render
import json
from django.views.generic import View
from testapp.models import Student
from testapp.serializers import StudentSerializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
# Create your views here.

class StudentData1(View):
    def get(self,request,*args,**kwargs):
        data = request.body
        steam = io.BytesIO(data)
        pdict = JSONParser().parse(steam)
        id = pdict.get('id',None)
        if id is not None:
            emp = Student.objects.get(id=id)
            serializer = StudentSerializers(emp)
            new_data = JSONRenderer().render(serializer.data)
            return HttpResponse(new_data,content_type='application/json')
        emp = Student.objects.all()
        serializer = StudentSerializers(emp,many=True)
        new_data = JSONRenderer().render(serializer.data)
        return HttpResponse(new_data, content_type='application/json')



from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
@method_decorator(csrf_exempt,name='dispatch')
class StudentData2(View):
    def delete(self,request,*args,**kwargs):
        data = request.body
        steam = io.BytesIO(data)
        pdict = JSONParser().parse(steam)
        id = pdict.get('id')
        emp = Student.objects.get(id=id)
        emp.delete()
        msg = {'msg': 'resourced deleted successfully'}
        json_data = JSONRenderer().render(msg)
        return HttpResponse(json_data, content_type='application/json')

    def put(self,request,*args,**kwargs):
        data = request.body
        steam = io.BytesIO(data)
        pdict = JSONParser().parse(steam)
        id= pdict.get('id')
        emp = Student.objects.get(id=id)
        serializer = StudentSerializers(emp,data=pdict,partial = True)
        if serializer.is_valid():
            serializer.save()
            msg = {'msg':'resourced updated successfully'}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    def post(self,request,*args,**kwargs):
        data = request.body
        steam = io.BytesIO(data)
        pdict = JSONParser().parse(steam)
        serializer =  StudentSerializers(data=pdict)
        if serializer.is_valid():
            serializer.save()
            msg = {"msg":'data added in records successfully'}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json',status=400)




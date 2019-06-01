#coding=utf8
from django.http import HttpResponse
from django.shortcuts import render
from FoodModel.models import Food
from django.views.decorators.csrf import csrf_exempt,csrf_protect
import json
import time

@csrf_exempt
def uploadfile(request):
    fileobj = request.FILES.get('foodimg')
    print(fileobj)
    if fileobj:
        rootpath = 'E:/pywww/dinner'
        filepath = '/static/'+str(time.time())+'.jpg'
        with open(rootpath + filepath,'w+',encoding='gbk') as newfile:
            for chunk in fileobj.chunks():
                newfile.write(chunk)
            return HttpResponse(json.dumps({'success':True,'path':filepath}))
    return HttpResponse(json.dumps({'success':False,'path':'上传失败'}))

def add(request):
    return render(request,'add.html')

@csrf_protect
def create(request):
    request.encoding='utf-8'
    input_data = request.POST
    if 'foodname' in input_data:
        food = Food.objects.filter(foodname=input_data['foodname'])
        if len(food) > 0:
            return HttpResponse(json.dumps({'success':False,'msg':'菜式已存在'}))
        food = Food(foodname=input_data['foodname'])
        food.save()

        return HttpResponse(json.dumps({'success': True, 'msg': '添加成功'}))
    else:
        return HttpResponse(json.dumps({'success':False,'msg':'value error'}))

def home(request):
    context = {}
    context['username'] = 'liu'
    foodlist = []
    foods = Food.objects.all()
    for food in foods:
        foodlist.append(food.foodname)
    context['foodlist'] = foodlist
    return render(request,'index.html',context)

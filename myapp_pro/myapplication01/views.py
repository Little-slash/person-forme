import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
from myapplication01 import models
from django.core import serializers

def get_award(request):
    data = {}
    data_set = models.award.objects.all()    # 查询ji
    data['data'] = json.loads(serializers.serialize("json", data_set))
    # index = new_.my_edu_name
    return JsonResponse(data)
    # return JsonResponse({"name":entry_list[1].my_edu_name, "index":entry_list[1].my_edu_index, "date":data_set[1].my_edu_date, "major":data_set[1].my_edu_major, "degree":data_set[1].my_edu_degree})

def get_edu(request):
    data = {}
    data_set = models.edu.objects.all()    # 查询ji
    data['data'] = json.loads(serializers.serialize("json", data_set))
    # index = new_.my_edu_name
    return JsonResponse(data)
    # index = new_.my_edu_name


def get_pub(request):
    data = {}
    data_set = models.Articles.objects.all()    # 查询ji
    data['data'] = json.loads(serializers.serialize("json", data_set))
    # index = new_.my_edu_name
    return JsonResponse(data)
    # index = new_.my_edu_name
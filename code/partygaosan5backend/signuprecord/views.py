# -*- coding: utf-8 -*-
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response

from .serializers import NameSerializer
from .models import PartyName

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from rest_framework.parsers import JSONParser
# Create your views here.

class NameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    """
    list:
       GET url: /name/   分类列表数据
    creat:
       POST url: /name/  创建姓名详情
    retrieve:
       GET url: /name/1/  获取姓名详情
    update:
       PUT url: /name/1/  修改姓名详情
    delete:
       DELETE url: /category/1/  删除分类详情
    """
    parser_classes = [JSONParser]


    # list
   # queryset = PartyName.objects.all().order_by('name')
    queryset = PartyName.objects.all()
    serializer_class = NameSerializer
    lookup_field = "id"


    # create basic authorization string to database authtoken table
    for user in User.objects.all():
        Token.objects.get_or_create(user=user)

        '''
                serializer = NameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'password set'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        '''


    @action(detail=False, methods=['post'])
    def submitmsg(self, request):
            serializer = NameSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg': '信息提交成功'})
            else:
                return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        #return Response({'received data': request.data})
            #print(request.body)
            #receive_data = json.loads(request.body.decode())

            #return Response({'status': 'password set','object': str })



'''

    @api_view(['GET'])
    @action(detail=True)
    def addName(self, request, pk=None):

      if  request.method == 'get':
        serializer = NameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
                    user = self.get_object()
        serializer = NameSerializer(data=request.data)
        if serializer.is_valid():
            user.save()
            return JsonResponse({'msg':'123'},  json_dumps_params={'ensure_ascii':False}, charset='utf-8')
            #return Response("提交成功")
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
'''









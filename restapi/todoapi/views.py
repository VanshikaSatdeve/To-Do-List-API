from django.shortcuts import render
from .serializers import ToDoSerializer
from . models import TodoList
from rest_framework.viewsets import ModelViewSet
from rest_framework import status, parsers
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import action
# Create your views here.


class TodoListViewSet(ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = ToDoSerializer
    parser_classes = (parsers.FormParser,parsers.MultiPartParser, parsers.FileUploadParser)
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]


    def get_serializer_class(self):
        # if self.action == 'list':
        #     return ToDoSerializer
        # if self.action == 'create':
        #     return ToDoSerializer
        return self.serializer_class

   

    #get all todo
    def list(self,request):
        try:
            todo_objs = TodoList.objects.all()
            serializer = self.get_serializer(todo_objs, many = True)

            return Response({
                'status':status.HTTP_200_OK,
                'data': serializer.data
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status': APIException.status_code
            })

    #add todo
    def create(self,request):
        try:
            serializer = self.get_serializer(data=request.data)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({
                    'status':status.HTTP_400_BAD_REQUEST,
                    'data': serializer.errors,
                    'message':'Invalid data'
                })
            serializer.save()

            return Response({
                'status':status.HTTP_201_CREATED,
                'data': serializer.data,
                'messaage':'Todo added successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status': APIException.status_code
            })

    # get single todo
    def retrieve(self,request,pk=None):
        try:
            id = pk
            if id is not None:

                #author_objs = Author.objects.all()
                todo_objs = self.get_object()
                serializer = self.get_serializer(todo_objs)

            return Response({
                'status':status.HTTP_200_OK,
                'data': serializer.data
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status': APIException.status_code
            })

    #update all fields of todolist
    def update(self,request, pk=None):
        try:
            
            todo_objs = self.get_object()
            serializer = self.get_serializer(todo_objs,data=request.data, partial=False)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({
                    'status':status.HTTP_400_BAD_REQUEST,
                    'data': serializer.errors,
                    'message':'Invalid data'
                })
            serializer.save()

            return Response({
                'status':status.HTTP_200_OK,
                'data': serializer.data,
                'messaage':'todo updated successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status': APIException.status_code
            })

    #update specific fields
    def partial_update(self,request, pk=None):
        try:
           
            todo_objs = self.get_object()
            serializer = self.get_serializer(todo_objs,data=request.data,partial = True)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({
                    'status':status.HTTP_400_BAD_REQUEST,
                    'data': serializer.errors,
                    'message':'Invalid data'
                })
            serializer.save()

            return Response({
                'status':status.HTTP_200_OK,
                'data': serializer.data,
                'messaage':'todo updated successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status': APIException.status_code
            })

    # delete specific todolist
    def destroy(self, request,pk):
        try:
            id=pk
            todo_obj = self.get_object()
            todo_obj.delete()
            return Response({
                'status':status.HTTP_200_OK,
                'messaage':'todo deleted successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status': APIException.status_code
            })





from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models, serializers


class ListCreateCourse(APIView):
    def get(self, request, format=None):
        courses = models.Course.objects.all()
        serializer = serializers.CourseSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # accept the requested data to post and serialize it through COurseSerializer
        serializer = serializers.CourseSerializer(data=request.data)

        # check if serialize data is valid to save on database or not
        serializer.is_valid(raise_exception=True)

        # if data is valid save it othervise raise exception
        serializer.save()

        # return a drf Response with status code
        return Response(serializer.data, status=status.HTTP_201_CREATED)

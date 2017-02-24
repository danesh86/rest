from rest_framework import serializers
from .models import Course, Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id',
                  'course',
                  'name',
                  'email',
                  'comment',
                  'rating',
                  'created_at')
        extra_kwargs = {
            'email': {'write_only': True}
        }


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id',
                  'title',
                  'url')

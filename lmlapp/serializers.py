# from django.contrib.auth.models import User
# from rest_framework import serializers
#
# #
# # User Serializer
# from lmlappadmin.models import Message
#
#
# class UserSerializer(serializers.ModelSerializer):
#     """For Serializing User"""
#     password = serializers.CharField(write_only=True)
#     class Meta:
#         model = User
#         fields = ['username', 'password']
# #
# # Message Serializer
# class MessageSerializer(serializers.ModelSerializer):
#     """For Serializing Message"""
#     sender = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
#     receiver = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
#     class Meta:
#         model = Message
#         fields = ['sender', 'receiver', 'message', 'created_at']
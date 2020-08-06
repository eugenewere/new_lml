# # chat/consumers.py
# import json
# from asgiref.sync import async_to_sync
# from channels.consumer import AsyncConsumer
# from channels.generic.websocket import WebsocketConsumer
# from django.contrib.auth.models import User
#
# from lmlappadmin.models import Message
# from humanize import naturaltime
#
#
# class ChatConsumer(WebsocketConsumer):
#
#     def fetch_messages(self, data):
#         messages = Message.last_15_messages()
#         content ={
#             'messages': self.messages_to_json(messages)
#         }
#         self.send_message(content)
#
#     def messages_to_json(self, messages):
#         results = []
#         for message in messages:
#             results.append(self.message_to_json(message))
#
#     def message_to_json(self, message):
#         return {
#             'sender': message.sender,
#             'reciever': message.reciever,
#             'status': message.status,
#             'time': naturaltime(message.created_at),
#             'message':message.msg_content,
#         }
#
#     def new_messages(self, data):
#         print(data)
#
#         sender = data['sender']
#         reciever = data['reciever']
#         messagee = data['message']
#         room = data['room']
#         author_sender = User.objects.filter(id=sender).first()
#         author_reciever = User.objects.filter(id=reciever).first()
#         message = Message.objects.create(
#             msg_content=messagee,
#             sender=author_sender,
#             room=room,
#             reciever=author_reciever
#
#         )
#         content={
#             'command': 'new_message',
#             'message': self.message_to_json(message)
#         }
#         return self.send_chat_message(content)
#
#
#
#
#
#     async def connect(self):
#         self.room_name = self.scope['url_route']['kwargs']['room_name']
#         self.room_group_name = 'chat_%s' % self.room_name
#         await self.channel_layer.group_add(
#             self.room_group_name,
#             self.channel_name
#         )
#         # await self.accept()
#         await self.send({
#             "type": "websocket.accept"
#         })
#
#     async def disconnect(self, close_code):
#         await self.channel_layer.group_discard(
#             self.room_group_name,
#             self.channel_name
#         )
#
#     async def receive(self, text_data):
#         data = json.loads(text_data)
#         print(data)
#         await self.commands[data['command']](self, data)
#
#     async def send_chat_message(self, message):
#         # message = data['message']
#         await self.channel_layer.group_send(
#             self.room_group_name,
#             {
#                 'type': 'chat_message',
#                 'message': message
#             }
#         )
#
#     async def send_message(self, message):
#         await self.send(text_data=json.dumps(message))
#
#     async def chat_message(self, event):
#         message = event['message']
#
#         await self.send(text_data=json.dumps(message))
#
#     commands = {
#         'fetch_messages': fetch_messages,
#         'new_messages': new_messages,
#
#     }


from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer
import json
from asgiref.sync import async_to_sync
from lmlappadmin.models import *
from django.db.models import Q
import humanize
from django.contrib.humanize.templatetags.humanize import naturalday, naturaltime


class ChatConsumer(WebsocketConsumer):


    def fetch_messages(self, data):
        # print(data)
        s1 = json.dumps(data)
        data = json.loads(s1)
        d = data['text']
        e = json.loads(d)
        messages = Message.objects.order_by('created_at')
        content={
            'command': 'messages',
            'messages': self.messages_to_json(messages)
        }
        self.send_message(content)

    def messages_to_json(self, messages):
        results = []
        for message in messages:
            results.append(self.message_to_json(message))
        return results


    def message_to_json(self, message):
        # suser = User.objects.filter(id=message.sender.id).first()
        # ruser = User.objects.filter(id=message.reciever.id).first()
        # company = Company.objects.filter(user_ptr_id=suser.id).first()
        # reciever = Customer.objects.filter(user_ptr_id=ruser.id).first()

        return {
            'sender': message.sender.id,
            'receiver': message.reciever.id,
            'message': message.msg_content,
            'created_at': naturaltime(message.created_at),
            'room': message.room,
        }



    def send_message(self, message):
        self.send(text_data=json.dumps(message))

    def new_messages(self, data):
        # print(data)

        s1 = json.dumps(data)
        datay = json.loads(s1)
        d = data['text']
        e = json.loads(d)
        sender = e['sender']
        receiver = e['receiver']
        message_content = e['message']
        room = e['room']
        # print(sender,receiver,message_content)
        sender_user = User.objects.filter(username=sender).first()
        receiver_user = User.objects.filter(username=receiver).first()
        message = Message.objects.create(
            sender=sender_user,
            reciever=receiver_user,
            msg_content=message_content,
            room=room,
        )
        content ={
            'command':'new_messages',
            'message' :self.message_to_json(message)
        }
        return self.send_chat_message(content)

    def send_chat_message(self, message):
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

        # Receive message from room group

    def chat_message(self, event):
        message = event['message']
        # Send message to WebSocket
        self.send(text_data=json.dumps(message))

    commands = {

        'fetch_messages': fetch_messages,
        'new_messages': new_messages,
    }




    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            # self.room_name
            self.channel_name
        )
    # Receive message from WebSocket
    def websocket_receive(self, text_data):
        s1 = json.dumps(text_data)
        data = json.loads(s1)
        d = data['text']
        e =json.loads(d)


        self.commands[e['command']](self, data)






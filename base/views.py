from django.shortcuts import render
from django.http import JsonResponse
from agora_token_builder import RtcTokenBuilder
import random,time,json
from .models import RoomMember
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def getToken(request):
    appId = 'efe6eb040e754398a63bc0197e5620c3'
    appCertificate = '24f990e8d7d443cf9a66f5f6581a74d6'
    channelName = request.GET.get('channel')
    uid = random.randint(1,200)
    expirationTimeinSeconds = 3600 * 24
    currentTimeStamp = time.time()
    privilegeExpiredTs = currentTimeStamp + expirationTimeinSeconds
    role = 1

    token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, role, privilegeExpiredTs)
    return JsonResponse({'token':token,'uid':uid},safe=False)
def lobby(request):
    return render(request,'lobby.html')

def rooms(request):
    return render(request,'room.html')

@csrf_exempt
def createUser(request):
    data = json.loads(request.body)
    member,created = RoomMember.objects.get_or_create(
        name = data['name'],
        uid = data['UID'],
        room_name = data['room_name']
    )
    return JsonResponse({'name':data['name']},safe=False)

def getMember(request):
    uid = request.GET.get('uid')
    room_name = request.GET.get('room_name')

    member = RoomMember.objects.get(
        uid = uid,
        room_name = room_name
    )

    name = member.name
    return JsonResponse({'name':member.name},safe=False)


@csrf_exempt
def deleteUser(request):
    data = json.loads(request.body)


    member = RoomMember.objects.get(
        name = data['name'],
        uid = data['uid'],
        room_name = data['room_name']
    )
    member.delete()
    return JsonResponse('Member was deleted',safe=False)

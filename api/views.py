from rest_framework.decorators import api_view
from rest_framework.views import Response
from .serializers import DojoSerializer, MemberSerializer
from chexo_app.models import DojoList, MemberList


@api_view(['GET'])
def getRoutes(requests):
    routes = [
        {
            'url': 'dojos/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of dojo'
        },
        {
            'url': 'dojos/<int:dojo_id>/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of single dojo'
        },
        {
            'url': 'dojos/add/',
            'method': 'POST',
            'body': {
                "dojo_name": ""
            },
            'description': 'Creates a dojo'
        },
        {
            'url': 'dojos/<int:pk>/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes a dojo'
        },
        {
            'url': 'dojos/<int:pk>/update/',
            'method': 'PUT',
            'body': {
                'dojo_name': ''
            },
            'description': 'Updates a dojo name'
        },
        {
            'url': 'dojos/<int:dojo_id>/add/',
            'method': 'POST',
            'body': {
                'dojo_id': '',
                'name': '',
                'date_birth': '',
                'kyu': '',
            },
            'description': 'Creates a member of a dojo'
        },
        {
            'url': 'dojos/<int:dojo_id>/members/<int:pk>/',
            'method': 'PUT',
            'body': {
                'dojo': '',
                'name': '',
                'date_birth': '',
                'kyu': '',
            },
            'description': 'Updates a member of a dojo'
        },
        {
            'url': 'dojos/<int:dojo_id>/members/<int:pk>/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes a member of a dojo'
        },
    ]

    return Response(routes)


@api_view(['GET'])
def getDojos(request):
    dojos = DojoList.objects.all()
    serializer = DojoSerializer(dojos, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getDojo(request, dojo_id):
    dojo = DojoList.objects.get(id=dojo_id)
    serializer = DojoSerializer(dojo)
    return Response(serializer.data)


@api_view(['POST'])
def createDojo(request):
    data = request.data
    dojo = DojoList.objects.create(dojo_name=data['dojo_name'])
    serializer = DojoSerializer(dojo)
    return Response(serializer.data)

@api_view(['GET'])
def getDojoMembers(request, dojo_id):
    members = MemberList.objects.filter(dojo_id=dojo_id)
    serializer = MemberSerializer(members, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getMember(request,id):
    member = MemberList.objects.get(id=id)
    serializer = MemberSerializer(member)
    return Response(serializer.data)

@api_view(['POST'])
def addMember(request, dojo_id):
    data = request.data
    member = MemberList.objects.create(
        dojo_id=dojo_id,
        name=data['name'],
        birth_date=data['birth_date'],
        kyu=data['kyu']
        )
    serializer = MemberSerializer(member)
    return Response(serializer.data)

@api_view(['PUT'])
def updateDojo(request, pk):
    data = request.data
    dojo = DojoList.objects.get(pk=pk)
    serializer = DojoSerializer(dojo, data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['PUT'])
def updateMember(request,dojo_id, pk):
    data = request.data
    member = MemberList.objects.get(dojo_id=dojo_id, pk=pk)
    serializer = MemberSerializer(member, data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteDojo(request,dojo_id):
    dojo = DojoList.objects.get(id=dojo_id)
    dojo.delete()

    return Response("Dojo deleted")


@api_view(['DELETE'])
def deleteMember(request, dojo_id, pk):
    member = MemberList.objects.get(dojo_id=dojo_id, pk=pk)
    member.delete()

    return Response("Member deleted")
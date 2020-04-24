from guardian.shortcuts import assign_perm
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from permissions.services import APIPermissionClassFactory
from babies.models import Baby
from events.models import Event
from babies.serializer import BabySerializer
from events.serializer import EventSerializer

def evaluate(user, obj, request):
    return user.first_name == obj.parent.name

class BabyViewSet(viewsets.ModelViewSet):
    queryset = Baby.objects.all()
    serializer_class = BabySerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='EventPermission',
            permission_configuration={
                'base': {
                    'create': True,
                    'list': True,
                },
                'instance': {
                    'retrieve': 'babies.view_baby',
                    'destroy': False,
                    'update': True,
                    'partial_update': 'babies.change_baby',
                }
            }
        ),
    )

    def perform_create(self, serializer):
        baby = serializer.save()
        user = self.request.user
        assign_perm('babies.view_baby', user, baby)
        assign_perm('babies.change_baby', user, baby)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def events(self, request, pk=None):
        baby = self.get_object()
        events_baby=[]
        for event in Event.objects.filter(baby=baby):
            events_baby.append(BabySerializer(event).data)
        return Response(events_baby)



    """@action(detail=True, methods=['get'])
    def babies(self, request, pk=None):
        parent = self.get_object()
        babies_user = []
        for baby in Baby.objects.filter(parent=parent):
            babies_user.append(BabySerializer(baby).data)
        return Response(babies_user)"""

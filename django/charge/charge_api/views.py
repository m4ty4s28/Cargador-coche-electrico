from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import ChargePoint
from .serializers import ChargePointSerializer
from django.utils import timezone
from django.shortcuts import render
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.contrib.auth.decorators import login_required


@login_required(login_url='/')
def dashboard_status(request):
    return render(request, 'dashboard.html')

def send_change_charge(data_to_send):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "general",
        {
            'type': 'receive',
            'data': data_to_send
        }
    )

class ChargePointListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the ChargePoint
        '''

        all_chargepoints = ChargePoint.objects.filter(deleted_at=None).all()
        serializer = ChargePointSerializer(all_chargepoints, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the ChargePoint with given json data
        '''

        data = {
            'name': request.data.get('name'),
            'created_at': timezone.now(),
        }

        serializer = ChargePointSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ChargePointDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, chargepoint_id):
        '''
        Helper method to get the object with given chargepoint_id
        '''

        try:

            return ChargePoint.objects.get(id=chargepoint_id)
            
        except ChargePoint.DoesNotExist:

            return None

    # 3. Retrieve
    def get(self, request, chargepoint_id, *args, **kwargs):
        '''
        Retrieves the ChargePoint with given chargepoint_id
        '''

        instance = self.get_object(chargepoint_id)

        if not instance:

            return Response(
                {"res": "Object with id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = ChargePointSerializer(instance)

        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, chargepoint_id, *args, **kwargs):
        '''
        Updates the status field with given chargepoint_id if exists
        '''

        instance = self.get_object(chargepoint_id)

        if not instance:

            return Response(
                {"res": "Object with chargepoint_id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        data = {
            'status': request.data.get('status')
        }

        serializer = ChargePointSerializer(instance = instance, data=data, partial = True)

        if serializer.is_valid():

            if instance.status != data["status"]:
                # send change status of charge by websocket
                data_to_send = "the charge {} with id {} change status from {} -> {}".format(instance.name, instance.id, instance.status, data["status"])
                send_change_charge(data_to_send)

            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, chargepoint_id, *args, **kwargs):
        '''
        Deletes the ChargePoint item with given chargepoint_id if exists
        '''

        instance = self.get_object(chargepoint_id)

        if not instance:
            return Response(
                {"res": "Object with id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        #instance.delete()

        data = {
            'deleted_at': timezone.now()
        }

        serializer = ChargePointSerializer(instance = instance, data=data, partial = True)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {"res": "Object deleted!"},
                status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
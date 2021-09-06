from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, filters, mixins, viewsets
from rest_framework.response import Response
from base.helpers import CustomPagination
from room.models import Room
from .serializers import RoomSerializer


class RoomViewset(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = Room.objects.filter()
    serializer_class = RoomSerializer
    pagination_class = CustomPagination
    lookup_field = 'pk'
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['-created_at']
    permission_classes = [permissions.IsAuthenticated, ]
    # permission_classes = [permissions.AllowAny, ]

    filterset_fields = [
        'room_no', 'floor_no', 'capacity'
    ]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user.email)

    def list(self, request, *args, **kwargs):
        return super(RoomViewset, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.object.save()
            return Response('Updated successfully', status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


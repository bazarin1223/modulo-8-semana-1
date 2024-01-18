
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from reserva.models import reserva,petshop
from rest_api.serializers import agendamentoserializer2,agendamentomodelserializer1
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated



class petshopmodelviewset(ReadOnlyModelViewSet):
    queryset = reserva.objects.all()
    serializer_class = agendamentoserializer2
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


@api_view(['GET','POST'])
def hello_word(request):
    consulta = reserva.objects.all()
    serializer = agendamentomodelserializer1 (instance = consulta,many = True)
    return Response(serializer.data)
    


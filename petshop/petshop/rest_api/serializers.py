from rest_framework.serializers import ModelSerializer,HyperlinkedRelatedField,PrimaryKeyRelatedField

from reserva.models import petshop,reserva


class petshopnestedmodelserializer(ModelSerializer):
    reservas = HyperlinkedRelatedField(
        many = True,
        read_only = True,
        view_name='api : reserva-detail'
    )
    class Meta:
        model = petshop
        fields = '__all__'

class agendamentomodelserializer1(ModelSerializer):
    petshop = petshopnestedmodelserializer(read_only = True)


    class Meta:
        model = reserva
        fields = '__all__'

class PetShopRelatedFieldCustomSerializer(PrimaryKeyRelatedField):
    def __init__(self,**kwargs):
        self.serializer = petshopnestedmodelserializer
        super().__init__(**kwargs)

    def use_pk_only_optimization(self):
        return False
    def to_representation(self,value):
        return self.serializer(value,context=self.context).data
    
class agendamentoserializer2(ModelSerializer):
    petshop = PetShopRelatedFieldCustomSerializer(
        queryset = petshop.objects.all(),
        read_only=False
        )

    class Meta:
        model = reserva
        fields = '__all__'
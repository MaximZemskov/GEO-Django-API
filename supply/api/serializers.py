from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField,
    StringRelatedField,
)

from rest_framework_gis.serializers import GeoFeatureModelSerializer

from supply.models import (
    Supplier,
    ServiceArea,
    Service,
)


class SupplierCreateSerializer(ModelSerializer):
    class Meta:
        model = Supplier
        fields = [
            'title',
            'email',
            'phone_number',
        ]


class SupplierDetailSerializer(ModelSerializer):
    class Meta:
        model = Supplier
        fields = [
            'title',
            'email',
            'phone_number',
        ]


class SupplierListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='api-supply:detail',
        lookup_field='pk',
    )

    # areas = SerializerMethodField()

    class Meta:
        model = Supplier
        fields = [
            'url',
            'title',
            'email',
            'phone_number',
        ]

    # def get_areas(self, obj):
    #     obj.serviceareas


# SERVICE

class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = ('title', 'price',)


class ServiceAreaSerializer(GeoFeatureModelSerializer):
    services = ServiceSerializer(many=True)

    class Meta:
        model = ServiceArea
        geo_field = 'poly'
        fields = [
            'id',
            'title',
            'services',
        ]


from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
)

from rest_framework_gis.serializers import GeoFeatureModelSerializer

from supply.models import (
    Supplier,
    ServiceArea,
    Service,
)


class SupplierDetailSerializer(ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'


class SupplierListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='api-supply:suppliers-detail',
        lookup_field='pk',
    )

    class Meta:
        model = Supplier
        fields = [
            'id',
            'url',
            'title',
            'email',
            'phone_number',
            'address',
        ]


# SERVICE

class ServiceSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='api-supply:service-detail',
        lookup_field='pk',
    )

    class Meta:
        model = Service
        fields = '__all__'


# SERVICE AREA

class ServiceAreaSerializer(GeoFeatureModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='api-supply:service-area-detail',
        lookup_field='pk',
    )
    services = ServiceSerializer(many=True)

    class Meta:
        model = ServiceArea
        geo_field = 'poly'
        fields = '__all__'

    def create(self, validated_data):
        services_data = validated_data.pop('services')
        service_area = ServiceArea.objects.create(**validated_data)

        for service in services_data:
            service, created = Service.objects.get_or_create(title=service['title'], price=service['price'],
                                                             service_area=service_area)
            service_area.services.add(service)
        return service_area

    def update(self, instance, validated_data):
        services_data = validated_data.pop('services')
        instance.title = validated_data.get('title', instance.title)
        instance.poly = validated_data.get('poly', instance.poly)

        services_list = []

        for service in services_data:
            service, created = Service.objects.get_or_create(title=service["title"], price=service['price'],
                                                             service_area=instance)
            services_list.append(service)

        instance.services.set(services_list)
        instance.save()
        return instance


# SUPPLIER SELECTION

class ServiceSelectionSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = (
            'title',
            'price',
        )


class ServiceAreaSelectionSerializer(GeoFeatureModelSerializer):
    services = ServiceSelectionSerializer(many=True)

    class Meta:
        model = ServiceArea
        geo_field = 'poly'
        fields = (
            'title',
            'services',
        )


class SupplierSelectionSerializer(ModelSerializer):
    areas = ServiceAreaSelectionSerializer(many=True)

    class Meta:
        model = Supplier
        fields = (
            'title',
            'areas'
        )




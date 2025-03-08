from rest_framework import serializers
from users.models.profile import Profile

class ProfileGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['id', 'image_url', 'description']

    # def to_representation(self, instance):
    #     # Llama al método base para obtener la representación inicial
    #     representation = super().to_representation(instance)
        
    #     print(instance)

#     #     # Validaciones personalizadas
#     #     for field, value in representation.items():
#     #         if value is None:
#     #             print(f"El campo '{field}' tiene un valor de None")
#     #         else:
#     #             print(f"El campo '{field}' tiene el valor: {value}")

#     #     # Puedes modificar la representación si es necesario
#     #     if not representation.get('image_url'):
#     #         representation['image_url'] = "https://example.com/default-image.jpg"

#     #     return representation

from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'

class DonoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dono
        fields = '__all__'

class DonoSerializerValidate(serializers.ModelSerializer):
    class Meta:
        model = Dono
        fields = ["cpf"]

class AnimalSerializer(serializers.ModelSerializer):
    tutor = DonoSerializer()

    class Meta:
        model = Animal
        fields = '__all__'

class EspecialidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidade
        fields = '__all__'

class VeterinariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veterinaria
        fields = '__all__'

class VeterinarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veterinario
        fields = '__all__'
        
class VeterinarioSerializerValidate(serializers.ModelSerializer):
    class Meta:
        model = Veterinario
        fields = ["registro_crmv", "especialidade", "veterinaria"]

class ProntuarioSerializer(serializers.ModelSerializer):
    animal = AnimalSerializer()

    class Meta:
        model = Prontuario
        fields = '__all__'

class RegistroSaudeSerializer(serializers.ModelSerializer):
    prontuario = ProntuarioSerializer()

    class Meta:
        model = RegistroSaude
        fields = '__all__'

class VacinaSerializer(serializers.ModelSerializer):
    animal = AnimalSerializer()
    veterinario = VeterinarioSerializer()

    class Meta:
        model = Vacina
        fields = '__all__'

class ExameSerializer(serializers.ModelSerializer):
    animal = AnimalSerializer()
    veterinario = VeterinarioSerializer()

    class Meta:
        model = Exame
        fields = '__all__'

class AlergiaSerializer(serializers.ModelSerializer):
    animal = AnimalSerializer()
    veterinario = VeterinarioSerializer()

    class Meta:
        model = Alergia
        fields = '__all__'

class CirurgiaSerializer(serializers.ModelSerializer):
    animal = AnimalSerializer()
    veterinario = VeterinarioSerializer()

    class Meta:
        model = Cirurgia
        fields = '__all__'

class DocumentoSerializer(serializers.ModelSerializer):
    animal = AnimalSerializer()

    class Meta:
        model = Documento
        fields = '__all__'

class AtestadoSaudeSerializer(serializers.ModelSerializer):
    animal = AnimalSerializer()
    veterinario = VeterinarioSerializer()

    class Meta:
        model = AtestadoSaude
        fields = '__all__'

class CarteiraVacinacaoSerializer(serializers.ModelSerializer):
    animal = AnimalSerializer()

    class Meta:
        model = CarteiraVacinacao
        fields = '__all__'

class FichaClinicaSerializer(serializers.ModelSerializer):
    animal = AnimalSerializer()
    tutor = DonoSerializer()
    veterinario = VeterinarioSerializer()

    class Meta:
        model = FichaClinica
        fields = '__all__'

class ReceituarioSerializer(serializers.ModelSerializer):
    animal = AnimalSerializer()
    tutor = DonoSerializer()
    veterinario = VeterinarioSerializer()

    class Meta:
        model = Receituario
        fields = '__all__'

class TermoConsentimentoSerializer(serializers.ModelSerializer):
    animal = AnimalSerializer()
    tutor = DonoSerializer()
    veterinario = VeterinarioSerializer()

    class Meta:
        model = TermoConsentimento
        fields = '__all__'

class AtestadoObitoSerializer(serializers.ModelSerializer):
    animal = AnimalSerializer()
    tutor = DonoSerializer()
    veterinario = VeterinarioSerializer()

    class Meta:
        model = AtestadoObito
        fields = '__all__'

class ProcedimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procedimento
        fields = '__all__'
        
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        # Cria o usuário com o método `create_user` para garantir o hash da senha
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user


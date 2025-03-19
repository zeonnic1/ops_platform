from .models import HostsCategory, Hosts
from rest_framework import serializers


class HostCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = HostsCategory
        fields = ["id", "name"]

    def validate(self, data):
        try:
            name = data.get("name")
            if name == "":
                raise serializers.ValidationError("不能为空")
        except:
            raise serializers.ValidationError("不能为空")
        return data


class HostsSerializers(serializers.ModelSerializer):
    category_name = serializers.SlugRelatedField(source="category", read_only=True, slug_field='name')

    password = serializers.CharField(max_length=100, write_only=True, label="登录密码")

    class Meta:
        model = Hosts
        fields = ['id',  'category', 'category_name', 'host_name', 'ip_addr', 'port', 'username', 'password']

    # todo 验证主机登录密码
    def validate(self, data):
        print(data)
        return data

    def create(self, validated_data):
        validated_data.pop("password")
        instance = Hosts.objects.create(**validated_data)
        return instance

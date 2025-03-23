from .models import HostsCategory, Hosts
from rest_framework import serializers

from ops_platform.utils.ssh import SSH
from .tasks import check_host_status


class HostCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = HostsCategory
        fields = ["id", "name"]

    def validate(self, attr):
        try:
            name = attr.get("name")
            if name == "":
                raise serializers.ValidationError("不能为空")
        except:
            raise serializers.ValidationError("不能为空")
        return attr


class HostsSerializers(serializers.ModelSerializer):
    category_name = serializers.SlugRelatedField(source="category", read_only=True, slug_field='name')

    password = serializers.CharField(max_length=100, write_only=True, label="登录密码")

    # status = serializers.SerializerMethodField()

    class Meta:
        model = Hosts
        fields = ['id', 'category', 'category_name', 'name', 'host_name', 'port', 'username', 'password'
                  ]

    # def get_status(self, obj):
    #
    #     client = check_host_status(obj) or False
    #
    #     return client

    # def get_status(self, obj):
    #
    #
    #     client = SSH(obj.host_name, obj.port, obj.username)
    #     if client.ping():
    #         return True
    #     return False

    # todo 验证主机登录密码
    def validate(self, attr):
        hostname = attr.get("host_name")
        port = attr.get("port")
        username = attr.get("username")
        password = attr.get("password")
        client = SSH(hostname, port, username, password)

        if client.ping():
            return attr
        raise serializers.ValidationError("用户认证失败")

    def create(self, validated_data):
        hostname = validated_data.get("host_name")
        port = validated_data.get("port")
        username = validated_data.get("username")
        password = validated_data.get("password")
        client = SSH(hostname, port, username, password)
        if not client.set_rsa():
            raise serializers.ValidationError("远程免密失败")
        validated_data.pop("password")
        if Hosts.objects.filter(host_name=hostname, port=port).exists():
            raise serializers.ValidationError("主机名和端口组合已存在。")
        instance = Hosts.objects.create(**validated_data)
        return instance

from django.contrib.auth.models import AbstractUser
from django.db.models import Model


class Repository(object):
    def __init__(self, model: Model or AbstractUser):
        self.model = model

    def list(self):
        return self.model.objects.all()

    def retrieve(self, _id: int):
        return self.model.objects.get(id=_id)

    def put(self, _id: int, data: dict):
        _object = self.model.objects.get(id=_id)
        if _object is None:
            return Exception('object not found')
        else:
            for i in data:
                if hasattr(_object, i) and getattr(_object, i) != data[i]:
                    setattr(_object, i, data[i])
            if data.get('password') is not None and isinstance(_object, AbstractUser) or \
                    issubclass(_object.__class__, AbstractUser):
                _object.set_password(data.get('password'))
            else:
                raise AttributeError("password only allowed for abstract users or their childs class")
            _object.save()
        return _object

    def create(self, data: dict):
        return self.model.objects.create(**data)

    def delete(self, _id):
        return self.model.objects.get(pk=_id).delete()

    def filter_by(self, data: dict):
        print(data)
        return self.model.objects.filter(**data)

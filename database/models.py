from tortoise import fields, models

class User(models.Model):
    id = fields.IntField(pk=True)
    telegram_id = fields.BigIntField(unique=True)
    phone = fields.TextField()
    name = fields.TextField()

    def __str__(self):
        return f"{self.id}:{self.telegram_id}"

class Record(models.Model):
    id = fields.IntField(pk=True)
    user = fields.BigIntField()
    name = fields.TextField()
    kidname = fields.TextField()
    society = fields.TextField()

    def __str__(self):
        return f"{self.id}:{self.user.telegram_id}:{self.name}:{self.kidname}:{self.society}"
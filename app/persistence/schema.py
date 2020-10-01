from marshmallow import Schema, fields


class ItemSchema(Schema):
    _id = fields.Str(required=True)
    name = fields.Str()
    price = fields.Float()

from marshmallow import Schema, fields, validate


class RuleSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    action = fields.Str(validate=validate.OneOf(['allow', 'deny']), required=True)
    source_ip = fields.Str(allow_none=True)
    destination_ip = fields.Str(allow_none=True)


rule_schema = RuleSchema()

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.policy import Policy
from app.schemas.rule_schema import RuleSchema
from app import ma


class PolicySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Policy
        include_relationships = True

    rules = ma.Nested(RuleSchema, many=True)


policy_schema = PolicySchema()
policies_schema = PolicySchema(many=True)

from app import db
from app.models.rule import Rule
from app.schemas.rule_schema import RuleSchema
from app.models.policy import Policy

rule_schema = RuleSchema()
rules_schema = RuleSchema(many=True)


def create_rule(data):
    name = data.get('name')
    action = data.get('action')
    source_ip = data.get('source_ip')
    destination_ip = data.get('destination_ip')

    if action not in ['allow', 'deny']:
        raise ValueError("Action must be either 'allow' or 'deny'.")

    new_rule = Rule(name=name, action=action, source_ip=source_ip, destination_ip=destination_ip)

    db.session.add(new_rule)
    db.session.commit()

    return rule_schema.dump(new_rule)


def get_rule_by_id(rule_id):
    return Rule.query.get(rule_id)


def get_rules():
    rules = Rule.query.all()
    return rules_schema.dump(rules)


def delete_rule(rule_id):
    rule = Rule.query.get(rule_id)
    if rule:
        db.session.delete(rule)
        db.session.commit()
        return {"message": f"Rule with id {rule_id} deleted successfully"}
    else:
        return {"message": f"Rule with id {rule_id} not found"}, 404



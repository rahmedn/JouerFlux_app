from app import db
from app.models.policy import Policy
from app.models.rule import Rule


def create_policy(data):
    new_policy = Policy(name=data['name'])
    db.session.add(new_policy)
    db.session.commit()
    return new_policy


def get_policy_by_id(policy_id):
    return Policy.query.get(policy_id)


def update_policy(policy, data):
    policy.name = data.get('name', policy.name)
    policy.firewall_id = data.get('firewall_id', policy.firewall_id)

    db.session.commit()

    return policy


def delete_policy(policy):
    db.session.delete(policy)
    db.session.commit()


def add_rule_to_policy(policy_id, rule_id):
    # Récupérer la règle et la politique concernées
    rule = Rule.query.get(rule_id)
    policy = Policy.query.get(policy_id)

    if not rule:
        raise Exception(f"Rule with ID {rule_id} not found")
    if not policy:
        raise Exception(f"Policy with ID {policy_id} not found")

    # Vérifier si la règle est déjà associée à la politique
    if rule in policy.rules:
        raise Exception(f"Rule with ID {rule_id} is already associated with Policy ID {policy_id}")

    policy.rules.append(rule)

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e
    finally:
        db.session.close()

    return {"message": f"Rule with ID {rule_id} added to Policy with ID {policy_id} successfully"}


def delete_rule_from_policy(policy_id, rule_id):
    policy = Policy.query.get(policy_id)
    if not policy:
        raise Exception(f"Policy with ID {policy_id} not found")

    rule = Rule.query.get(rule_id)
    if not rule:
        raise Exception(f"Rule with ID {rule_id} not found")

    if rule not in policy.rules:
        raise Exception(f"Rule with ID {rule_id} is not associated with Policy ID {policy_id}")

    policy.rules.remove(rule)
    db.session.commit()

    return {"message": f"Rule with ID {rule_id} removed from Policy with ID {policy_id} successfully"}


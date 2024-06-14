from flask import Blueprint, jsonify, request
from app.services.policy_service import create_policy, get_policy_by_id, update_policy, delete_policy
from app.services.policy_service import add_rule_to_policy, delete_rule_from_policy
from app.schemas.policy_schema import policy_schema, policies_schema
from app.models.policy import Policy
from flask import current_app as app


policy_blueprint = Blueprint('policy', __name__)


@policy_blueprint.route('/policies', methods=['POST'])
def create_policy_route():
    data = request.get_json()
    existing_policy = Policy.query.filter_by(name=data['name']).first()
    if existing_policy:
        return jsonify({"error": f"A policy with the name {data['name']} already exists"}), 400

    try:
        new_policy = create_policy(data)
        app.logger.info(f"Policy '{new_policy.name}' created with ID: {new_policy.id}")
        return policy_schema.dump(new_policy), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@policy_blueprint.route('/policies', methods=['GET'])
def get_all_policies_route():
    policies = Policy.query.all()
    return policies_schema.dump(policies, many=True)


@policy_blueprint.route('/policies/<int:policy_id>', methods=['GET'])
def get_policy_by_id_route(policy_id):
    policy = get_policy_by_id(policy_id)
    if policy:
        return policy_schema.dump(policy)
    return {'message': f'Policy with ID {policy_id} not found'}, 404


@policy_blueprint.route('/policies/<int:policy_id>', methods=['PUT'])
def update_policy_route(policy_id):
    data = request.get_json()
    policy = get_policy_by_id(policy_id)
    if policy:
        updated_policy = update_policy(policy, data)
        app.logger.info(f"Policy with ID {policy_id} updated")
        return policy_schema.dump(updated_policy)
    return {'message': f'Policy with ID {policy_id} not found'}, 404


@policy_blueprint.route('/policies/<int:policy_id>', methods=['DELETE'])
def delete_policy_route(policy_id):
    policy = get_policy_by_id(policy_id)
    if policy:
        delete_policy(policy)
        app.logger.info(f"Policy with ID {policy_id} deleted")
        return '', 204
    return {'message': f'Policy with ID {policy_id} not found'}, 404


@policy_blueprint.route('/policies/<int:policy_id>/rules/<int:rule_id>', methods=['POST'])
def add_rule_to_policy_route(policy_id, rule_id):

    try:
        result = add_rule_to_policy(policy_id, rule_id)
        app.logger.info(f"Rule with ID {rule_id} added to Policy with ID {policy_id}")
        return jsonify(result), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@policy_blueprint.route('/policies/<int:policy_id>/rules', methods=['GET'])
def get_rules_for_policy(policy_id):
    try:
        policy = Policy.query.get(policy_id)
        if not policy:
            return jsonify({"error": f"Policy with ID {policy_id} not found"}), 404

        rules = policy.rules

        rules_list = []
        for rule in rules:
            rules_list.append({
                "id": rule.id,
                "name": rule.name,
                "action": rule.action,
                "source_ip": rule.source_ip,
                "destination_ip": rule.destination_ip
            })

        return jsonify(rules_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@policy_blueprint.route('/policies/<int:policy_id>/rules/<int:rule_id>', methods=['DELETE'])
def delete_rule_from_policy_route(policy_id, rule_id):
    try:
        result = delete_rule_from_policy(policy_id, rule_id)
        app.logger.info(f"Retrieved rules for policy with ID {policy_id}")
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

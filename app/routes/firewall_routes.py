from flask import Blueprint, jsonify, request
from app.services.firewall_service import create_firewall, get_firewall_by_id, update_firewall, delete_firewall, get_all_firewalls, add_policy_to_firewall, get_firewall_policies, remove_policy_from_firewall
from app.services.firewall_service import activate_firewall, deactivate_firewall
from app.schemas.firewall_schema import FirewallSchema
from flask import current_app as app

firewall_blueprint = Blueprint('firewall', __name__)
firewall_schema = FirewallSchema()
firewalls_schema = FirewallSchema(many=True)


@firewall_blueprint.route('/firewalls', methods=['POST'])
def create_firewall_route():
    data = request.get_json()
    try:
        new_firewall = create_firewall(data)
        app.logger.info(f"Firewall '{new_firewall.name}' created with ID: {new_firewall.id}")
        return firewall_schema.dump(new_firewall), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@firewall_blueprint.route('/firewalls', methods=['GET'])
def get_all_firewalls_route():
    firewalls = get_all_firewalls()
    return firewall_schema.dump(firewalls, many=True)


@firewall_blueprint.route('/firewalls/<int:firewall_id>', methods=['GET'])
def get_firewall_by_id_route(firewall_id):
    firewall = get_firewall_by_id(firewall_id)
    if firewall:
        return firewall_schema.dump(firewall)
    return {'message': f'Firewall with ID {firewall_id} not found'}, 404


@firewall_blueprint.route('/firewalls/<int:firewall_id>', methods=['PUT'])
def update_firewall_route(firewall_id):
    data = request.get_json()
    firewall = get_firewall_by_id(firewall_id)
    if firewall:
        updated_firewall = update_firewall(firewall, data)
        app.logger.info(f"Firewall with ID {firewall_id} updated")
        return firewall_schema.dump(updated_firewall)
    return {'message': f'Firewall with ID {firewall_id} not found'}, 404


@firewall_blueprint.route('/firewalls/<int:firewall_id>', methods=['DELETE'])
def delete_firewall_route(firewall_id):
    firewall = get_firewall_by_id(firewall_id)
    if firewall:
        delete_firewall(firewall)
        app.logger.info(f"Firewall with ID {firewall_id} deleted")
        return '', 204
    return {'message': f'Firewall with ID {firewall_id} not found'}, 404


@firewall_blueprint.route('/firewalls/<int:firewall_id>/activate', methods=['PUT'])
def activate_firewall_route(firewall_id):
    try:
        result = activate_firewall(firewall_id)
        app.logger.info(f"Firewall with ID {firewall_id} activated")
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@firewall_blueprint.route('/firewalls/<int:firewall_id>/deactivate', methods=['PUT'])
def deactivate_firewall_route(firewall_id):
    try:
        result = deactivate_firewall(firewall_id)
        app.logger.info(f"Firewall with ID {firewall_id} deactivated")
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@firewall_blueprint.route('/firewalls/<int:firewall_id>/policies', methods=['POST'])
def add_policy_to_firewall_route(firewall_id):
    data = request.get_json()
    policy_id = data.get('policy_id')

    if not policy_id:
        return jsonify({"message": "Missing 'policy_id' field in request body"}), 400

    try:
        add_policy_to_firewall(policy_id, firewall_id)
        app.logger.info(f"Policy with ID {policy_id} added to Firewall with ID {firewall_id}")
        return jsonify({"message": f"Policy with ID {policy_id} added to Firewall with ID {firewall_id}"}), 201
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@firewall_blueprint.route('/firewalls/<int:firewall_id>/policies', methods=['GET'])
def get_firewall_policies_route(firewall_id):
    try:
        policies = get_firewall_policies(firewall_id)
        policy_list = [{"id": policy.id, "name": policy.name} for policy in policies]
        return jsonify({"policies": policy_list}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@firewall_blueprint.route('/firewalls/<int:firewall_id>/policies/<int:policy_id>', methods=['DELETE'])
def remove_policy_from_firewall_route(firewall_id, policy_id):
    try:
        remove_policy_from_firewall(policy_id, firewall_id)
        app.logger.info(f"Policy with ID {policy_id} removed from Firewall with ID {firewall_id}")
        return jsonify({"message": f"Policy with ID {policy_id} removed from Firewall with ID {firewall_id}"}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500

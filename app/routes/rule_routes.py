from flask import Blueprint, jsonify, request
from app.services.rule_service import create_rule, get_rules, delete_rule, get_rule_by_id
from app.schemas.rule_schema import rule_schema
from flask import current_app as app
rule_blueprint = Blueprint('rule_bp', __name__, url_prefix='/api/rules')


@rule_blueprint.route('/rules', methods=['POST'])
def create_rule_route():
    data = request.json
    try:
        new_rule = create_rule(data)
        app.logger.info(f"Rule '{new_rule['name']}' created with ID: {new_rule['id']}")
        return jsonify(new_rule), 201
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@rule_blueprint.route('/rules/<int:rule_id>', methods=['GET'])
def get_rule_by_id_route(rule_id):
    rule = get_rule_by_id(rule_id)
    if rule:
        return rule_schema.dump(rule)
    return {'message': f'Rule with ID {rule_id} not found'}, 404


@rule_blueprint.route('/rules', methods=['GET'])
def get_rules_route():
    rules = get_rules()
    return jsonify(rules), 200


@rule_blueprint.route('/rules/<int:rule_id>', methods=['DELETE'])
def delete_rule_route(rule_id):
    result = delete_rule(rule_id)
    app.logger.info(f"Rule with ID {rule_id} deleted")
    return jsonify(result), 200 if 'message' in result else 404




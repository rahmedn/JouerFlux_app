from app import db
from app.models.firewall import Firewall
from app.models.policy import Policy
from app.schemas.firewall_schema import FirewallSchema

firewall_schema = FirewallSchema()


def create_firewall(data):
    """
    Create a new firewall.

    Args:
        data (dict): Data containing the 'name' of the new firewall.

    Returns:
        Firewall: The newly created firewall instance.
    """

    new_firewall = Firewall(name=data['name'])
    db.session.add(new_firewall)
    db.session.commit()
    return new_firewall


def get_firewall_by_id(firewall_id):
    """
    Retrieve a firewall by its ID.

    Args:
        firewall_id (int): ID of the firewall to retrieve.

    Returns:
        Firewall: The firewall instance with the specified ID, or None if not found.
    """
    return Firewall.query.get(firewall_id)


def update_firewall(firewall, data):
    """
    Update an existing firewall.

    Args:
        firewall (Firewall): The firewall instance to update.
        data (dict): Data containing the updated 'name' of the firewall.

    Returns:
        Firewall: The updated firewall instance.
    """

    firewall.name = data['name']
    db.session.commit()
    return firewall


def delete_firewall(firewall):
    """
    Delete a firewall.

    Args:
        firewall (Firewall): The firewall instance to delete.
    """

    db.session.delete(firewall)
    db.session.commit()


def get_all_firewalls():
    """
    Retrieve all firewalls.

    Returns:
        list: A list of all firewall instances.
    """

    return Firewall.query.all()


def add_policy_to_firewall(policy_id, firewall_id):
    """
    Add a policy to a firewall.

    Args:
        policy_id (int): ID of the policy to add.
        firewall_id (int): ID of the firewall to add the policy to.
    """

    policy = Policy.query.get(policy_id)
    firewall = Firewall.query.get(firewall_id)

    if not policy:
        raise Exception(f"Policy with ID {policy_id} does not exist.")
    if not firewall:
        raise Exception(f"Firewall with ID {firewall_id} does not exist.")

    firewall.policies.append(policy)

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e
    finally:
        db.session.close()


def get_firewall_policies(firewall_id):
    """
    Retrieve all policies associated with a firewall.

    Args:
        firewall_id (int): ID of the firewall to retrieve policies for.

    Returns:
        list: A list of policies associated with the specified firewall.
    """

    firewall = Firewall.query.get(firewall_id)

    if not firewall:
        raise Exception(f"Firewall with ID {firewall_id} does not exist.")

    return firewall.policies


def remove_policy_from_firewall(policy_id, firewall_id):
    """
    Remove a policy from a firewall.

    Args:
        policy_id (int): ID of the policy to remove.
        firewall_id (int): ID of the firewall to remove the policy from.
    """

    policy = Policy.query.get(policy_id)
    firewall = Firewall.query.get(firewall_id)

    if not policy:
        raise Exception(f"Policy with ID {policy_id} does not exist.")
    if not firewall:
        raise Exception(f"Firewall with ID {firewall_id} does not exist.")

    firewall.policies.remove(policy)

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e
    finally:
        db.session.close()


def deactivate_firewall(firewall_id):
    """
    Deactivate a firewall.

    Args:
        firewall_id (int): ID of the firewall to deactivate.
    """

    firewall = Firewall.query.get(firewall_id)
    if not firewall:
        raise Exception(f"Firewall with ID {firewall_id} not found")

    firewall.activated = False
    db.session.commit()
    return {"message": f"Firewall with ID {firewall_id} deactivated successfully"}


def activate_firewall(firewall_id):
    """
    Activate a firewall.

    Args:
        firewall_id (int): ID of the firewall to activate.
    """

    firewall = Firewall.query.get(firewall_id)
    if not firewall:
        raise Exception(f"Firewall with ID {firewall_id} not found")

    firewall.activated = True
    db.session.commit()

    return {"message": f"Firewall with ID {firewall_id} activated successfully"}


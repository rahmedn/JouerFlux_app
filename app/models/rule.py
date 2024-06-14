from app import db


class Rule(db.Model):
    """
    Model representing a Rule.

    Attributes:
        id (int): Unique identifier for the rule.
        name (str): Name of the rule, must be unique and cannot be null.
        action (str): Action to be taken by the rule, either 'allow' or 'deny'. Cannot be null.
        source_ip (str, optional): Source IP address associated with the rule. Can be null.
        destination_ip (str, optional): Destination IP address associated with the rule. Can be null.
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    action = db.Column(db.String(10), nullable=False)  # 'allow' or 'deny'
    source_ip = db.Column(db.String(100), nullable=True)
    destination_ip = db.Column(db.String(100), nullable=True)

    def __init__(self, name, action, source_ip=None, destination_ip=None):
        self.name = name
        self.action = action
        self.source_ip = source_ip
        self.destination_ip = destination_ip

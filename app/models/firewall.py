from app import db
from app.models.policy import Policy


firewall_policy = db.Table('firewall_policy',
    db.Column('firewall_id', db.Integer, db.ForeignKey('firewall.id'), primary_key=True),
    db.Column('policy_id', db.Integer, db.ForeignKey('policy.id'), primary_key=True)
)


class Firewall(db.Model):
    """
    Model representing a Firewall.

    Attributes:
        id (int): Unique identifier for the firewall.
        name (str): Name of the firewall, must be unique and cannot be null.
        activated (bool): Activation status of the firewall, defaults to True.
        policies (relationship): Many-to-many relationship with the Policy model via the firewall_policy association table.
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    activated = db.Column(db.Boolean, default=True)
    policies = db.relationship(
        'Policy',
        secondary=firewall_policy,
        backref=db.backref('firewalls', lazy='dynamic')
    )


from app.models.rule import Rule
from app import db

policy_rule = db.Table(
    'policy_rule',
    db.Column('policy_id', db.Integer, db.ForeignKey('policy.id'), primary_key=True),
    db.Column('rule_id', db.Integer, db.ForeignKey('rule.id'), primary_key=True),
    extend_existing=True
)


class Policy(db.Model):
    """
    Model representing a Policy.

    Attributes:
        id (int): Unique identifier for the policy.
        name (str): Name of the policy, must be unique and cannot be null.
        rules (relationship): Many-to-many relationship with the Rule model via the policy_rule association table.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    rules = db.relationship(
        'Rule',
        secondary=policy_rule,
        backref=db.backref('policies', lazy='dynamic')
    )

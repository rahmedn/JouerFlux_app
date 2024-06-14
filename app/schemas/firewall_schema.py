from app import ma
from app.models.firewall import Firewall


class FirewallSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Firewall
        include_relationships = True


firewall_schema = FirewallSchema()
firewalls_schema = FirewallSchema(many=True)

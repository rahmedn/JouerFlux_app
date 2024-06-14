from faker import Faker
from app import create_app, db
from app.models.firewall import Firewall
from app.models.policy import Policy
from app.models.rule import Rule
import random

faker = Faker()


def create_fake_data():
    app = create_app()
    app.app_context().push()

    firewall_counter = 1
    policy_counter = 1
    rule_counter = 1

    for _ in range(10):
        firewall = Firewall(
            name=f"firewall{firewall_counter}",
            activated=True,
            policies=[]
        )
        db.session.add(firewall)

        for _ in range(random.randint(1, 5)):
            policy = Policy(
                name=f"policy{policy_counter}",
                rules=[]
            )
            firewall.policies.append(policy)
            db.session.add(policy)
            policy_counter += 1

            rule_names = set()
            while len(rule_names) < random.randint(1, 10):
                rule_name = f"rule{rule_counter}"
                rule_names.add(rule_name)
                rule_counter += 1

            for name in rule_names:
                rule = Rule(
                    name=name,
                    action=random.choice(['allow', 'deny']),
                    source_ip=faker.ipv4(),
                    destination_ip=faker.ipv4()
                )
                policy.rules.append(rule)
                db.session.add(rule)

        firewall_counter += 1

    try:
        db.session.commit()
        print("Fake data has been successfully generated.")
    except Exception as e:
        print(f"Error occurred during data generation: {str(e)}")
        db.session.rollback()


if __name__ == "__main__":
    create_fake_data()

from typing import List
from polaris.integrations import RailsIntegration
from polaris.models import Transaction, Asset
from django.db.models import QuerySet

class MyRailsIntegration(RailsIntegration):
    def poll_pending_deposits(self, pending_deposits: QuerySet) -> List[Transaction]:
        return list(pending_deposits)

    def execute_outgoing_transaction(self, transaction: Transaction):
        transaction.amount_fee = 1
        transaction.status = Transaction.STATUS.completed
        transaction.save()

def toml():
    asset = Asset.objects.first()
    return{
        "DOCUMENTATION":{
            "ORG_NAME": "Stellar Development Foundation",
            "ORG_URL": "https://stellar.org"
        },
        "PRINCIPALS":[
            {
                "name": "Besnard HOUNWANOU"
            }
        ],
        "CURRENCIES":[
            {
                "code": asset.code,
                "issuer": asset.issuer,
                "status": "test",
                "display_decimals": 2,
                "name": "stellar reference token",
                "desc": "A fake asset on testnet for demonstration",
            }
        ]
    }
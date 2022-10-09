from dataclasses import dataclass
from Code.client.models.payment import Payment


@dataclass
class Order:
    description: str
    payment: Payment

from abc import ABC, abstractmethod
from Code.client.models.payment import Payment


class IPaymentService(ABC):
    @abstractmethod
    def pay(self, payment: Payment):
        pass

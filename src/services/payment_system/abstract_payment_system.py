from uuid import UUID

from abc import ABC, abstractmethod


class AbstractPaymentSystemService(ABC):
    PAYMENT_SYSTEM_NAME: str

    @classmethod
    @abstractmethod
    async def create_payment(
            cls,
    ):
        pass

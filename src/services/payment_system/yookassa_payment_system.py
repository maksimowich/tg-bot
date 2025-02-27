# from uuid import UUID, uuid4
#
# from yookassa import Configuration, Payment, Refund
#
# from .abstract_payment_system import AbstractPaymentSystemService
#
#
# class YookassaPaymentSystemService(AbstractPaymentSystemService):
#     PAYMENT_SYSTEM_NAME = "yookassa"
#
#     Configuration.account_id = app_settings.yookassa.account_id
#     Configuration.secret_key = app_settings.yookassa.secret_key
#
#     @classmethod
#     async def create_payment(
#             cls,
#     ):
#         payment = Payment.create({
#             "amount": {
#                 "value": str(subscription_type.cost),
#                 "currency": "RUB"
#             },
#             "payment_method_data": {
#                 "type": "bank_card"
#             },
#             "confirmation": {
#                 "type": "redirect",
#                 "return_url": "http://localhost:8013/api/docs",
#             },
#             "description": f"Payment for subscription {subscription_type.name}",
#             "metadata": {
#                 "subscription_id": str(subscription_id),
#                 "control_string": control_string,
#             },
#             "capture": False,
#             "test": True,
#         }, idempotence_key)
#
#         return SubscriptionPaymentResponse(
#             payment_id=payment.id,
#             payment_system_name=cls.PAYMENT_SYSTEM_NAME,
#             subscription_id=subscription_id,
#             confirmation_url=payment.confirmation.confirmation_url,
#         )

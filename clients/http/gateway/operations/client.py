from httpx import Response, QueryParams
from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client
from clients.http.gateway.operations.schema import *


class OperationsGatewayHTTPClient(HTTPClient):
    """Клиент для взаимодействия с /api/v1/operations сервиса http-gateway."""

    def get_operation_api(self, operation_id: str) -> Response:
        """
        Получить информацию об операции.

        :param operation_id: Идентификатор операции.
        :return: Объект httpx.Response с информацией по операции.
        """
        return self.get(f"/api/v1/operations/{operation_id}")

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Получить чек по операции.

        :param operation_id: Идентификатор операции.
        :return: Объект httpx.Response с данными о чеке по операции.
        """
        return self.get(f"/api/v1/operations/operation-receipt/{operation_id}")

    def get_operations_api(self, query: GetOperationsQuerySchema) -> Response:
        """
        Получить список операций по счету.

        :param query: Pydantic-модель с параметрами запроса, например: {"accountId": "123"}.
        :return: Объект httpx.Response с данными об операциях по счету.
        """
        return self.get("/api/v1/operations",
                        params=QueryParams(query.model_dump(by_alias=True)))

    def get_operations_summary_api(self, query: GetOperationsQuerySchema) -> Response:
        """
        Получить статистику по операциям по счету.

        :param query: Pydantic-модель с параметрами запроса, например: {"accountId": "123"}.
        :return: Объект httpx.Response со статистики по операциям по счету.
        """
        return self.get("/api/v1/operations/operations-summary",
                        params=QueryParams(query.model_dump(by_alias=True)))

    def make_fee_operation_api(self, request: MakeOperationRequestSchema) -> Response:
        """
        Создать операцию комиссии.

        :param request: Pydantic-модель с данными по операции, например:
        {"status": "COMPLETED", "amount": 1.5, "cardId": "123", "accountId": "456"}.
        :return: Объект httpx.Response с данными созданной операции.
        """
        return self.post("/api/v1/operations/make-fee-operation",
                         json=request.model_dump(by_alias=True))

    def make_top_up_operation_api(self, request: MakeOperationRequestSchema) -> Response:
        """
        Создать операцию пополнения.

        :param request: Pydantic-модель с данными по операции, например:
        {"status": "COMPLETED", "amount": 100, "cardId": "123", "accountId": "456"}.
        :return: Объект httpx.Response с данными созданной операции.
        """
        return self.post("/api/v1/operations/make-top-up-operation",
                         json=request.model_dump(by_alias=True))

    def make_cashback_operation_api(self, request: MakeOperationRequestSchema) -> Response:
        """
        Создать операцию кэшбэка.

        :param request: Pydantic-модель с данными по операции, например:
        {"status": "COMPLETED", "amount": 100, "cardId": "123", "accountId": "456"}.
        :return: Объект httpx.Response с данными созданной операции.
        """
        return self.post("/api/v1/operations/make-cashback-operation",
                         json=request.model_dump(by_alias=True))

    def make_transfer_operation_api(self, request: MakeOperationRequestSchema) -> Response:
        """
        Создать операцию перевода.

        :param request: Pydantic-модель с данными по операции, например:
        {"status": "COMPLETED", "amount": 100, "cardId": "123", "accountId": "456"}.
        :return: Объект httpx.Response с данными созданной операции.
        """
        return self.post("/api/v1/operations/make-transfer-operation",
                         json=request.model_dump(by_alias=True))

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestSchema) -> Response:
        """
        Создать операцию покупки.

        :param request: Pydantic-модель с данными по операции, например:
        {"status": "COMPLETED", "amount": 100, "cardId": "123", "accountId": "456", "category": "toys"}.
        :return: Объект httpx.Response с данными созданной операции.
        """
        return self.post("/api/v1/operations/make-purchase-operation",
                         json=request.model_dump(by_alias=True))

    def make_bill_payment_operation_api(self, request: MakeOperationRequestSchema) -> Response:
        """
        Создать операцию оплаты по счету.

        :param request: Pydantic-модель с данными по операции, например:
        {"status": "COMPLETED", "amount": 1.5, "cardId": "123", "accountId": "456"}.
        :return: Объект httpx.Response с данными созданной операции.
        """
        return self.post("/api/v1/operations/make-bill-payment-operation",
                         json=request.model_dump(by_alias=True))

    def make_cash_withdrawal_operation_api(self, request: MakeOperationRequestSchema) -> Response:
        """
        Создать операцию снятия наличных.

        :param request: Pydantic-модель с данными по операции, например:
        {"status": "COMPLETED", "amount": 1.5, "cardId": "123", "accountId": "456"}.
        :return: Объект httpx.Response с данными созданной операции.
        """
        return self.post("/api/v1/operations/make-cash-withdrawal-operation",
                         json=request.model_dump(by_alias=True))

    def get_operation(self, operation_id: str) -> GetOperationResponseSchema:
        """
        Получить информацию об операции.

        :param operation_id: Идентификатор операции.
        :return: Объект GetOperationResponseSchema с информацией по операции.
        """
        response = self.get_operation_api(operation_id=operation_id)
        return GetOperationResponseSchema.model_validate_json(response.text)

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponseSchema:
        """
        Получить чек по операции.

        :param operation_id: Идентификатор операции.
        :return: Объект GetOperationReceiptResponseSchema с данными о чеке по операции.
        """
        response = self.get_operation_receipt_api(operation_id=operation_id)
        return GetOperationReceiptResponseSchema.model_validate_json(response.text)

    def get_operations(self, account_id: str) -> GetOperationsResponseSchema:
        """
        Получить список операций по счету.

        :param account_id: Идентификатор счета.
        :return: Объект GetOperationsResponseSchema с данными об операциях по счету.
        """
        query = GetOperationsQuerySchema(accountId=account_id)
        response = self.get_operations_api(query)
        return GetOperationsResponseSchema.model_validate_json(response.text)

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponseSchema:
        """
        Получить статистику по операциям по счету.

        :param account_id: Идентификатор счета.
        :return: Объект GetOperationsSummaryResponseSchema со статистики по операциям по счету.
        """
        query = GetOperationsQuerySchema(accountId=account_id)
        response = self.get_operations_summary_api(query=query)
        return GetOperationsSummaryResponseSchema.model_validate_json(response.text)

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeFeeOperationResponseSchema:
        """
        Создать операцию комиссии.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Объект MakeFeeOperationResponseSchema созданной операции.
        """
        request = MakeOperationRequestSchema(
            status="COMPLETED",
            amount=55.77,
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_fee_operation_api(request=request)
        return MakeFeeOperationResponseSchema.model_validate_json(response.text)

    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeTopOperationResponseSchema:
        """
        Создать операцию пополнения.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Объект MakeTopOperationResponseSchema созданной операции.
        """
        request = MakeOperationRequestSchema(
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_top_up_operation_api(request=request)
        return MakeTopOperationResponseSchema.model_validate_json(response.text)

    def make_cashback_operation(self, card_id: str, account_id: str) -> MakeCashbackOperationResponseSchema:
        """
        Создать операцию кэшбэка.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Объект MakeCashbackOperationResponseSchema созданной операции.
        """
        request = MakeOperationRequestSchema(
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_cashback_operation_api(request=request)
        return MakeCashbackOperationResponseSchema.model_validate_json(response.text)

    def make_transfer_operation(self, card_id: str, account_id: str) -> MakeTransferOperationResponseSchema:
        """
        Создать операцию перевода.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Объект MakeTransferOperationResponseSchema созданной операции.
        """
        request = MakeOperationRequestSchema(
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_transfer_operation_api(request=request)
        return MakeTransferOperationResponseSchema.model_validate_json(response.text)

    def make_purchase_operation(self, card_id: str, account_id: str) -> MakePurchaseOperationResponseSchema:
        """
        Создать операцию покупки.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Объект MakePurchaseOperationResponseSchema созданной операции.
        """
        request = MakePurchaseOperationRequestSchema(
            card_id=card_id,
            account_id=account_id,
        )
        response = self.make_purchase_operation_api(request=request)
        return MakePurchaseOperationResponseSchema.model_validate_json(response.text)

    def make_bill_payment_operation(self, card_id: str, account_id: str) -> MakeBillPaymentOperationResponseSchema:
        """
        Создать операцию оплаты по счету.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Объект MakeBillPaymentOperationResponseSchema созданной операции.
        """
        request = MakeOperationRequestSchema(
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_bill_payment_operation_api(request=request)
        return MakeBillPaymentOperationResponseSchema.model_validate_json(response.text)

    def make_cash_withdrawal_operation(self, card_id: str,
                                       account_id: str) -> MakeCashWithdrawalOperationResponseSchema:
        """
        Создать операцию по снятию наличных.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Объект MakeCashWithdrawalOperationResponseSchema созданной операции.
        """
        request = MakeOperationRequestSchema(
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_cash_withdrawal_operation_api(request=request)
        return MakeCashWithdrawalOperationResponseSchema.model_validate_json(response.text)


def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Функция создаёт экземпляр OperationsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию OperationsGatewayHTTPClient
    """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())

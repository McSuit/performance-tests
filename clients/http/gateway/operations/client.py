from typing import TypedDict
from httpx import Response, QueryParams
from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client


class GetOperationsQueryDict(TypedDict):
    """Структура данных для получения списка операций и статистики операций по счету."""

    accountId: str


class MakeOperationRequestDict(TypedDict):
    """Структура данных для общих полей в POST-запросах."""

    status: str
    amount: float
    cardId: str
    accountId: str


class MakePurchaseOperationRequestDict(MakeOperationRequestDict):
    """Структура данных для POST-запроса на создание операции покупки."""

    category: str


class OperationDict(TypedDict):
    """ Структура операции."""

    id: str
    type: str
    status: str
    amount: float
    cardId: str
    category: str
    createdAt: str
    accountId: str


class OperationReceiptDict(TypedDict):
    """Структура чека."""

    url: str
    document: str


class OperationsSummaryDict(TypedDict):
    """Структура статистики."""

    spentAmount: float
    receivedAmount: float
    cashbackAmount: float


class GetOperationReceiptResponseDict(TypedDict):
    """Структура ответа получения чека по операции."""

    receipt: OperationReceiptDict


class GetOperationResponseDict(TypedDict):
    """Структура ответа получения списка операций по счету."""

    operation: OperationDict


class GetOperationsResponseDict(TypedDict):
    """Структура ответа получения информации об операции."""

    operations: list[OperationDict]


class GetOperationsSummaryResponseDict(TypedDict):
    """Структура ответа получения статистики по операциям по счету."""

    summary: OperationsSummaryDict


class MakeOperationResponseDict(TypedDict):
    """Структура ответа для создания операции."""

    operation: OperationDict


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

    def get_operations_api(self, query: GetOperationsQueryDict) -> Response:
        """
        Получить список операций по счету.

        :param query: Словарь с параметрами запроса, например: {"accountId": "123"}.
        :return: Объект httpx.Response с данными об операциях по счету.
        """
        return self.get("/api/v1/operations", params=QueryParams(**query))

    def get_operations_summary_api(self, query: GetOperationsQueryDict) -> Response:
        """
        Получить статистику по операциям по счету.

        :param query: Словарь с параметрами запроса, например: {"accountId": "123"}.
        :return: Объект httpx.Response со статистики по операциям по счету.
        """
        return self.get("/api/v1/operations/operations-summary", params=QueryParams(**query))

    def make_fee_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """
        Создать операцию комиссии.

        :param request: Словарь с данными по операции, например:
        {"status": "COMPLETED", "amount": 1.5, "cardId": "123", "accountId": "456"}.
        :return: Объект httpx.Response с данными созданной операции.
        """
        return self.post("/api/v1/operations/make-fee-operation", json=request)

    def make_top_up_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """
        Создать операцию пополнения.

        :param request: Словарь с данными по операции, например:
        {"status": "COMPLETED", "amount": 100, "cardId": "123", "accountId": "456"}.
        :return: Объект httpx.Response с данными созданной операции.
        """
        return self.post("/api/v1/operations/make-top-up-operation", json=request)

    def make_cashback_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """
        Создать операцию кэшбэка.

        :param request: Словарь с данными по операции, например:
        {"status": "COMPLETED", "amount": 100, "cardId": "123", "accountId": "456"}.
        :return: Объект httpx.Response с данными созданной операции.
        """
        return self.post("/api/v1/operations/make-cashback-operation", json=request)

    def make_transfer_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """
        Создать операцию перевода.

        :param request: Словарь с данными по операции, например:
        {"status": "COMPLETED", "amount": 100, "cardId": "123", "accountId": "456"}.
        :return: Объект httpx.Response с данными созданной операции.
        """
        return self.post("/api/v1/operations/make-transfer-operation", json=request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestDict) -> Response:
        """
        Создать операцию покупки.

        :param request: Словарь с данными по операции, например:
        {"status": "COMPLETED", "amount": 100, "cardId": "123", "accountId": "456", "category": "toys"}.
        :return: Объект httpx.Response с данными созданной операции.
        """
        return self.post("/api/v1/operations/make-purchase-operation", json=request)

    def make_bill_payment_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """
        Создать операцию оплаты по счету.

        :param request: Словарь с данными по операции, например:
        {"status": "COMPLETED", "amount": 1.5, "cardId": "123", "accountId": "456"}.
        :return: Объект httpx.Response с данными созданной операции.
        """
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request)

    def make_cash_withdrawal_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """
        Создать операцию снятия наличных.

        :param request: Словарь с данными по операции, например:
        {"status": "COMPLETED", "amount": 1.5, "cardId": "123", "accountId": "456"}.
        :return: Объект httpx.Response с данными созданной операции.
        """
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=request)

    def get_operation(self, operation_id: str) -> GetOperationResponseDict:
        """
        Получить информацию об операции.

        :param operation_id: Идентификатор операции.
        :return: Объект GetOperationResponseDict с информацией по операции.
        """
        response = self.get_operation_api(operation_id=operation_id)
        return response.json()

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponseDict:
        """
        Получить чек по операции.

        :param operation_id: Идентификатор операции.
        :return: Объект GetOperationReceiptResponseDict с данными о чеке по операции.
        """
        response = self.get_operation_receipt_api(operation_id=operation_id)
        return response.json()

    def get_operations(self, account_id: str) -> GetOperationsResponseDict:
        """
        Получить список операций по счету.

        :param account_id: Идентификатор счета.
        :return: Объект GetOperationsResponseDict с данными об операциях по счету.
        """
        query = GetOperationsQueryDict(accountId=account_id)
        response = self.get_operations_api(query)
        return response.json()

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponseDict:
        """
        Получить статистику по операциям по счету.

        :param account_id: Идентификатор счета.
        :return: Объект GetOperationsSummaryResponseDict со статистики по операциям по счету.
        """
        query = GetOperationsQueryDict(accountId=account_id)
        response = self.get_operations_summary_api(query=query)
        return response.json()

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeOperationResponseDict:
        """
        Создать операцию комиссии.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Объект MakeOperationResponseDict созданной операции.
        """
        request = MakeOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_fee_operation_api(request=request)
        return response.json()

    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeOperationResponseDict:
        """
        Создать операцию пополнения.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Объект MakeOperationResponseDict созданной операции.
        """
        request = MakeOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_top_up_operation_api(request=request)
        return response.json()

    def make_cashback_operation(self, card_id: str, account_id: str) -> MakeOperationResponseDict:
        """
        Создать операцию кэшбэка.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Объект MakeOperationResponseDict созданной операции.
        """
        request = MakeOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_cashback_operation_api(request=request)
        return response.json()

    def make_transfer_operation(self, card_id: str, account_id: str) -> MakeOperationResponseDict:
        """
        Создать операцию перевода.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Объект MakeOperationResponseDict созданной операции.
        """
        request = MakeOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_transfer_operation_api(request=request)
        return response.json()

    def make_purchase_operation(self, card_id: str, account_id: str) -> MakeOperationResponseDict:
        """
        Создать операцию покупки.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Объект MakeOperationResponseDict созданной операции.
        """
        request = MakePurchaseOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id,
            category="electronics"
        )
        response = self.make_purchase_operation_api(request=request)
        return response.json()

    def make_bill_payment_operation(self, card_id: str, account_id: str) -> MakeOperationResponseDict:
        """
        Создать операцию оплаты по счету.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Объект MakeOperationResponseDict созданной операции.
        """
        request = MakeOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_bill_payment_operation_api(request=request)
        return response.json()

    def make_cash_withdrawal_operation(self, card_id: str, account_id: str) -> MakeOperationResponseDict:
        """
        Создать операцию по снятию наличных.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Объект MakeOperationResponseDict созданной операции.
        """
        request = MakeOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_cash_withdrawal_operation_api(request=request)
        return response.json()


def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Функция создаёт экземпляр OperationsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию OperationsGatewayHTTPClient
    """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())

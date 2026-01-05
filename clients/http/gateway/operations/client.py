from typing import TypedDict
from httpx import Response, QueryParams
from clients.http.client import HTTPClient


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

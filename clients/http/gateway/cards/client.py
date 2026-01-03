from typing import TypedDict
from httpx import Response
from clients.http.client import HTTPClient


class IssueCardRequestDict(TypedDict):
    """Структура данных для выпуска новой карты."""

    userId: str
    accountId: str


class CardsGatewayHTTPClient(HTTPClient):
    """Клиент для взаимодействия с /api/v1/cards сервиса http-gateway."""

    def issue_virtual_card_api(self, request: IssueCardRequestDict) -> Response:
        """
        Выпусти новую виртуальную карту.

        :param request: Словарь с данными новой карты.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/cards/issue-virtual-card", json=request)

    def issue_physical_card_api(self, request: IssueCardRequestDict) -> Response:
        """
        Выпусти новую физическую карту.

        :param request: Словарь с данными новой карты.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/cards/issue-physical-card", json=request)
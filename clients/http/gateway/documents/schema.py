from pydantic import BaseModel, HttpUrl


class DocumentSchema(BaseModel):
    """Структуры документа."""

    url: HttpUrl
    document: str


class GetTariffDocumentResponseSchema(BaseModel):
    """Структура ответа для получения тарифа по счету."""

    tariff: DocumentSchema


class GetContractDocumentResponseSchema(BaseModel):
    """Структура ответа для получения контракта по счету."""

    contract: DocumentSchema

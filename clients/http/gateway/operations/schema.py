from pydantic import BaseModel, Field, ConfigDict, HttpUrl
from enum import StrEnum
from datetime import datetime
from tools.fakers import fake


class OperationType(StrEnum):
    FEE = "FEE"
    TOP_UP = "TOP_UP"
    PURCHASE = "PURCHASE"
    CASHBACK = "CASHBACK"
    TRANSFER = "TRANSFER"
    BILL_PAYMENT = "BILL_PAYMENT"
    CASH_WITHDRAWAL = "CASH_WITHDRAWAL"


class OperationStatus(StrEnum):
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
    IN_PROGRESS = "IN_PROGRESS"
    UNSPECIFIED = "UNSPECIFIED"


class GetOperationsQuerySchema(BaseModel):
    """Структура данных для получения списка операций и статистики операций по счету."""
    model_config = ConfigDict(populate_by_name=True)
    account_id: str = Field(alias="accountId")


class MakeOperationRequestSchema(BaseModel):
    """Структура данных для общих полей в POST-запросах."""
    model_config = ConfigDict(populate_by_name=True)
    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.amount)
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakePurchaseOperationRequestSchema(MakeOperationRequestSchema):
    """Структура данных для POST-запроса на создание операции покупки."""

    category: str = Field(default_factory=fake.category)


class OperationSchema(BaseModel):
    """ Структура операции."""

    id: str
    type: OperationType
    status: OperationStatus
    amount: float
    cardId: str = Field(alias="cardId")
    category: str
    created_at: datetime = Field(alias="createdAt")
    account_id: str = Field(alias="accountId")


class OperationReceiptSchema(BaseModel):
    """Структура чека."""

    url: HttpUrl
    document: str


class OperationsSummarySchema(BaseModel):
    """Структура статистики."""

    spent_amount: float = Field(alias="spentAmount")
    received_amount: float = Field(alias="receivedAmount")
    cashback_amount: float = Field(alias="cashbackAmount")


class GetOperationReceiptResponseSchema(BaseModel):
    """Структура ответа получения чека по операции."""

    receipt: OperationReceiptSchema


class GetOperationResponseSchema(BaseModel):
    """Структура ответа получения списка операций по счету."""

    operation: OperationSchema


class GetOperationsResponseSchema(BaseModel):
    """Структура ответа получения информации об операции."""

    operations: list[OperationSchema]


class GetOperationsSummaryResponseSchema(BaseModel):
    """Структура ответа получения статистики по операциям по счету."""

    summary: OperationsSummarySchema


class MakeFeeOperationResponseSchema(BaseModel):
    """Структура ответа для создания операции комиссии."""

    operation: OperationSchema


class MakeTopOperationResponseSchema(BaseModel):
    """Структура ответа для создания операции пополнения."""

    operation: OperationSchema


class MakeCashbackOperationResponseSchema(BaseModel):
    """Структура ответа для создания операции кэшбэка."""

    operation: OperationSchema


class MakeTransferOperationResponseSchema(BaseModel):
    """Структура ответа для создания операции перевода."""

    operation: OperationSchema


class MakePurchaseOperationResponseSchema(BaseModel):
    """Структура ответа для создания операции покупки."""

    operation: OperationSchema


class MakeBillPaymentOperationResponseSchema(BaseModel):
    """Структура ответа для создания операции оплаты по счету."""

    operation: OperationSchema


class MakeCashWithdrawalOperationResponseSchema(BaseModel):
    """Структура ответа для создания операции по снятию наличных."""

    operation: OperationSchema

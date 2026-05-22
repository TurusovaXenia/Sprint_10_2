from enum import StrEnum


class ExpectedMessage(StrEnum):
    USER_ALREADY_EXISTS = "Почта уже используется"
    AD_NOT_FOUND_OR_FORBIDDEN = "Оффер не найден или у вас нет прав на его редактирование"
    AD_DELETED_SUCCESS = "Объявление удалено успешно"

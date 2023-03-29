class BaseError(Exception):
    message = NotImplemented


class LogisticError(BaseError):
    message = NotImplemented


class RequestError(BaseError):
    message = NotImplemented


class NotEnoughSpace(LogisticError):
    message = "Недостаточно места на складе"


class NotEnoughProduct(LogisticError):
    message = "Недостаточно товара на складе"


class TooManyDifferentProducts(LogisticError):
    message = "Слишком много разных товаров на складе"


class InvalidRequest(RequestError):
    message = "Не правильные формат запроса"


class InvalidStorageName(RequestError):
    message = "Неизвестное место отправления или назначения"

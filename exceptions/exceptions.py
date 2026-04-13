class ExamException(Exception):
    """Базовое исключение для системы скачек"""
    pass


class DeliveryNotFoundException(ExamException):
    """Доставка не найдена"""
    pass


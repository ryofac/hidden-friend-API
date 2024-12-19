from presentation.exceptions.base_exceptions import AppError


class UserNotFoundException(AppError):
    def __init__(self, message):
        super().__init__(message)


class CredentialsException(AppError):
    def __init__(self, message):
        super().__init__(message)


class PasswordsDoesNotMatchException(AppError):
    def __init__(self, message):
        super().__init__(message)

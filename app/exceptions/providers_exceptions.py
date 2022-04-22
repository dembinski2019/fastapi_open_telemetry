
class APIException(Exception):
    message: str

    def __init__(self):
        super(APIException, self).__init__(self.message)


class CoinNotFound(APIException):
    message = 'Not Found infos'

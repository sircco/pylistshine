logger = logging.getLogger(__name__)


class ListShineException(Exception):
    pass


class ListShineAPIKeyException(ListShineException):
    def __str__(self):
        return 'LISTSHINE_API_KEY not defined'



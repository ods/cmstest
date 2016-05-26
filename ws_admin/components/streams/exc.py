from ikcms.ws_apps.composite.exc import (
    BaseError,
    MessageError,
)


class StreamBaseError(BaseError):
    pass


class StreamNotFound(StreamBaseError):
    message = 'Stream not found'

    def __init__(self, stream_name):
        self.stream_name = stream_name

    def __str__(self):
        return '{}: stream_name={}'.format(
            self.message,
            self.stream_name,
        )


class ActionNotFound(StreamBaseError):
    message = 'Action not found'

    def __init__(self, stream, action_name):
        self.stream = stream
        self.action_name = action_name

    def __str__(self):
        return '{}: stream_name={}, action_name={}'.format(
            self.message,
            self.stream.name,
            self.action_name,
        )


class StreamFieldNotFound(StreamBaseError):

    message = 'Field not found'

    def __init__(self, stream, field_name):
        self.stream = stream
        self.field_name = field_name

    def __str__(self):
        return '{}: stream={}, field_name={}'.format(
            self.message,
            self.stream.name,
            self.field_name,
        )


class StreamLimitError(StreamBaseError):

    message = 'Stream limit error'

    def __init__(self, stream):
        self.stream = stream

    def __str__(self):
        return '{}: stream_name={}, allowed_limits=1-{}'.format(
            self.message,
            self.stream.name,
            self.stream.limits,
        )


class StreamItemNotFound(StreamBaseError):

    message = 'Item not found'

    def __init__(self, stream, item_id):
        self.stream = stream
        self.item_id = item_id

    def __str__(self):
        return '{}: stream={}, item_id={}'.format(
            self.message,
            self.stream.name,
            self.item_id,
    )


class StreamItemAlreadyExists(StreamBaseError):

    message = 'Item already exists'

    def __init__(self, stream, item_id):
        self.stream = stream
        self.item_id = item_id

    def __str__(self):
        return '{}: stream={}, item_id={}'.format(
            self.message,
            self.stream.name,
            self.item_id,
    )


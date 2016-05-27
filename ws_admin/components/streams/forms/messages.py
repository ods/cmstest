from ikcms.ws_apps.base.messages import MessageForm
from ikcms.forms import fields, validators, convs


class mf_item_id(fields.IntField):
    name = 'item_id'
    label = 'Идентификатор документа'


class mf_filters(fields.RawDictField):
    name = 'filters'
    label = 'Словарь фильтров'


class mf_page(fields.IntField):
    name = 'page'
    label = 'Номер страницы'


class mf_page_size(fields.IntField):
    name = 'page_size'
    label = 'Размер страницы'
    validators = (validators.required,)


class OrderByConv(convs.Str):
    validators = (
        validators.required,
        validators.match(
            regex = '[+\-]{1}',
            message = 'Order value must startswith "+" or "-"',
        )
    )


class mf_order(fields.ListField):
    name = 'order'
    label = 'Сортировка'
    conv = convs.List(OrderByConv())


from ikcms.forms import fields


__all__ = (
    'item_id',
    'filters',
    'page',
    'page_size',
    'order',
    'kwargs',
    'values',
)


class item_id(fields.Int):
    name = 'item_id'
    label = 'Идентификатор документа'
    raw_required = True
    required = True


class filters(fields.RawDict):
    name = 'filters'
    label = 'Словарь фильтров'
    to_python_default = {}


class page(fields.Int):
    name = 'page'
    label = 'Номер страницы'
    to_python_default = 1
    min_value = 1


class page_size(fields.Int):
    name = 'page_size'
    label = 'Размер страницы'
    to_python_default = 1
    min_value = 1


class order(fields.String):
    name = 'order'
    label = 'Сортировка'
    to_python_default = '+id'
    required = True
    regex = r'[+\-]{1}'
    regex_error = 'Order value must startswith "+" or "-"',


class kwargs(fields.RawDict):
    name = 'kwargs'
    label = 'Ключевые аргументы'
    to_python_default = {}


class values(fields.RawDict):
    name = 'values'
    label = 'Значения'
    raw_required = True

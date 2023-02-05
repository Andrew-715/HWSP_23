from typing import Optional

from functions import filter_query, limit_query, \
    map_query, sort_query, unique_query


CMD_TO_FUNCTIONS = {
    'filter': filter_query,
    'unique': unique_query,
    'limit': limit_query,
    'map': map_query,
    'sort': sort_query
}

def read_file(filename: str):
    with open(filename) as file:
        for line in file:
            '''
            Чтение файла по строчке вместо полной обработки.
            '''
            yield line

'''
Преобразование запроса пользователя в запрос файла. 
'''
def convert_query(cmd: str, value: str, filename: str, data: Optional[list[str]]):
    if data is None:
        prepared_data = read_file(filename)
    else:
        prepared_data = data
    '''
    cmd - получаемые данные от пользователя.
    (value=value, data=prepared_data) - конструкция для вызова функций из словаря.
    '''
    return list(CMD_TO_FUNCTIONS[cmd](value=value, data=prepared_data))

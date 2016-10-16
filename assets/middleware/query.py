from django.db import connection
from django.utils.deprecation import MiddlewareMixin


class QueriesLog(MiddlewareMixin):
    @staticmethod
    def process_response(request, response):
        green_color, red_color, default_color = '\033[32m', '\033[31m', '\033[30m'
        color_change_string = '{}{}' + default_color

        queries_len = len(connection.queries)
        queries_time = 0

        for query in connection.queries:
            queries_time += float(query.get('time', query.get('duration', 0) / 1000))

        print('{}Queries from "{method} {path}": {queries_len} in {queries_time}.'.format(
            default_color,
            method=request.method,
            path=request.path,
            queries_len=color_change_string.format(red_color, str(queries_len)),
            queries_time=color_change_string.format(green_color, str(queries_time))
        ))
        return response
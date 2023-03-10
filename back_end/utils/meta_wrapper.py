import json
import time
import functools
import re
from datetime import datetime

from django.http import JsonResponse, HttpResponse
from colorama import Fore, Back

from pprint import pprint, pformat

DEBUG = True

HOST_IP = 'localhost'

CLS_PARSE_REG = re.compile(r"['](.*?)[']", re.S)

KB = 1 << 10
MB = KB * KB
GB = KB * MB

TIME_FMT = '%Y-%m-%d %H:%M:%S'

ROOT_SUFFIX = ''  # '\'s root'


def JSR(*keys):
    def decorator(req_func):
        @functools.wraps(req_func)
        def wrapper(*args, **kw):
            req_type, func_name = '', ''
            debug = DEBUG and len(args) == 2
            # user.UnreadCount.GET
            self, request = args
            req_type = req_func.__name__.upper()
            # req_type = 'POST' if hasattr(request, 'body') and len(request.body) > 0 else 'GET'
            func_name: str = CLS_PARSE_REG.findall(str(type(self)))[0].replace(".views.", ".")
            func_name = '' if len(func_name) < 2 else func_name
            func_name += f'.{req_type}'
            # func_name += f'.{req_type} ({random.choice(ascii_uppercase) + random.choice(ascii_uppercase)})'
            # func_name += '.' + req_type.lower()

            # print(Fore.BLUE + f'[{req_type}] called: {func_name}')
            if req_type == 'POST':
                try:
                    inputs = pformat(json.loads(request.body))
                except:
                    inputs = '[cannot preview body]'
            else:  # req_type == 'GET':
                inputs = f'session: {pformat(dict(request.session))}'
                if len(dict(request.GET).keys()):
                    inputs += f', GET: {pformat(dict(request.GET))}'

            prev_time = time.time()
            try:
                values = req_func(*args, **kw)
            except Exception as e:
                time_cost = time.time() - prev_time
                time.sleep(0.2)
                print(
                    Fore.MAGENTA + f'[{func_name}] ====! FATAL ERR !==== : {e}, {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
                                   f'\n input: {inputs}, time: {time_cost:.2f}s')
                time.sleep(0.2)
                # traceback.print_exc()
                raise e
            else:
                time_cost = time.time() - prev_time
                #print type of values
                values = list(values) if isinstance(values, tuple) else [values]
                # values = list(map(lambda x: x.strftime('%Y-%m-%d %H:%M:%S') if isinstance(x, datetime) else x,
                # values))
                [values.append('') for _ in range(len(keys) - len(values))]
                ret_dict = dict(zip(keys, values))

                if debug and func_name not in ['user.UnreadCount.GET', 'chat.ChatCount.GET',
                                               'entity.DocumentOnline.GET']:
                    c = Fore.RED if ret_dict.get('status', 0) else Fore.GREEN
                    cur_dt = datetime.now()
                    dt_str = cur_dt.strftime("%H:%M:%S.") + f'{float(cur_dt.strftime("0.%f")):.2f}'[-2:]
                    print(
                        c + f'[{func_name}] input: {inputs}\n ret: {pformat(ret_dict)}, time: {time_cost:.2f}s, at [{dt_str}]')

                return HttpResponse(json.dumps(ret_dict, ensure_ascii=False))

        return wrapper

    return decorator

import re
import datetime

import math
from django.utils.html import strip_tags


def count_words(html_string):
    '''count html_string
    html_string = <h1>This is a title</h1>

    :param html_string:
    :return: int
    '''
    word_string = strip_tags(html_string)
    count = len(re.findall(r"\w+", word_string))
    return count


def get_read_time(html_string):
    count = count_words(html_string)
    read_time_min = math.ceil(count / 200.0)  # 200 wpm
    # read_time_sec = read_time_min * 60
    read_time = datetime.timedelta(minutes=read_time_min)
    return str(read_time)

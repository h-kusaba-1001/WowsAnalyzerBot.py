import config
import datetime

class _util(object):

    """
    Calculate percentage(float 2)
    result = molecule * 100 / denominator
    """
    @staticmethod
    def calc_rate(molecule: int , denominator: int):
        return round( (molecule * 100) / denominator, 2)

    
    """
    UNIX timestamp format
    """
    @staticmethod
    def timestamp_format(_timestamp: int):
        _datetime = datetime.datetime.fromtimestamp(_timestamp, config.TIME_ZONE_OBJECT)
        return _datetime.strftime('%Y-%m-%d %H:%M:%S  ') + config.TIMEZONE_STR

import sys
sys.modules[__name__]= _util()
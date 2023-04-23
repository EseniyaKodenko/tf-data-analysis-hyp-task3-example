import pandas as pd
import numpy as np
from statsmodels.stats.weightstats import ztest


chat_id = 1019285902 # Ваш chat ID, не меняйте название переменной

def solution(dt) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    pvalue = ztest(dt, value = 300, alternative="smaller")[1]
    ans = True if pvalue < 0.1 else False
    return ans # Ваш ответ, True или False


import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp


chat_id = 1019285902 # Ваш chat ID, не меняйте название переменной

def solution(dt) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    pvalue = ttest_1samp(dt, popmean = 300)[1]
    ans = True if pvalue < 0.1 else False
    return ans # Ваш ответ, True или False

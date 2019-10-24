import requests
import re
import time
import numpy as np
import matplotlib.pyplot as plt

text2=requests.get('http://www.whalebj.com/xzjc/default.aspx')
pattern=re.compile('场内待运车辆数为：([0-9]*)\s辆.*?；<br />&nbsp;<br />前半小时进场车辆数为：([0-9]*)\s辆；<br />&nbsp;<br />前半小时离场车辆数为：([0-9]*)\s辆；',re.S)
tmp=text2.text
print(tmp)
result=pattern.findall(tmp)
print(result[1])
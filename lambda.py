salaries={
    'egon':3000,
    'alex':100000000,
    'wupeiqi':10000,
    'yuanhao':2000
}
def get(k):
    return salaries[k]

print(max(salaries,key=get)) #'alex'

info = [
    {'name': 'egon', 'age': '18', 'salary': '3000'},
    {'name': 'wxx', 'age': '28', 'salary': '1000'},
    {'name': 'lxx', 'age': '38', 'salary': '2000'}
]
print(max(info, key=lambda dic: int(dic['salary'])))
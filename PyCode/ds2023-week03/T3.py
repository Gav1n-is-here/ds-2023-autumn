import re
def is_id_number(id_number):
    if len(id_number) != 18:
        print('身份证号码长度错误')
        return False
    regularExpression = "(^[1-9]\\d{5}(18|19|20)\\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\\d{3}[0-9Xx]$)|"
    #M0D11-2
    if re.match(regularExpression, id_number):
        
        n = id_number.upper()
        # 加权因子
        var = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
        #与12差值模11可能的结果表
        var_id = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
        
        sum = 0
        for i in range(0, 17):
            sum += int(n[i]) * var[i]
        sum %= 11
        if (var_id[sum]) != str(n[17]):
            return False
        return True
    else:
        return False
n=(input('Please input id:'))
result = is_id_number(n)
print(result)
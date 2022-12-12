all = 0.0
alladd = 0.0
indig = ''


def add(addin, data):  # 累加两个数
    addone = 0
    addone = addin + data
    return addone


def is_number(s):  # 判断数字是否为浮点数
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


while True:
    indig = input('输入：').strip('')
    if indig == 'q' or indig == 'Q':
        break
    elif is_number(indig) == True:
        alladd = add(float(all), float(indig))  # 调用数字累加器
        all = format(alladd, '.2f')
        print(all)
    else:
        print("输入了非数字，请重新输入！！")

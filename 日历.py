while True:
    try:
        from calendar import month, isleap
        year = int(input("年份："))
        mon = input("月份：")
        if isleap(year):
            if mon == '':
                for i in range(1, 13):
                    print()
                    print(f"{year}年是闰年")
                    print(month(year, i))
            else:
                mon = int(mon)
                print()
                print(f"{year}年是闰年")
                print(month(year, mon))
        else:
            if mon == '':
                for i in range(1, 13):
                    print()
                    print(f"{year}年是平年")
                    print(month(year, i))
            else:
                mon = int(mon)
                print()
                print(f"{year}年是平年")
                print(month(year, mon))
    except (ValueError, EOFError, IndexError):
        print("输入错误！\a")

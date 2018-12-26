import csv
from matplotlib import pyplot as plt
from datetime import datetime

# filename = 'sitka_weather_07-2014.csv'
#要读取的文件
filename = 'weather.csv'

#打开文件并将文件结果对象存储到f中
with open(filename) as f:
    #创建一个与该文件相关联的阅读器(reader)对象，reader处理文件中以逗号分隔每一行的数据
    reader = csv.reader(f)
    #模块csv包含函数next()，将阅读器对象传递给它将返回文件的下一行
    headr_row = next(reader)

    dates,highs,lows = [],[],[]
    for row in reader:
        #datetime.strptime()设置时间日期
        current_date = datetime.strptime(row[0],"%Y/%m/%d")
        dates.append(current_date)

        high = int(row[1])
        highs.append(high)

        low = int(row[2])
        lows.append(low)

    # 数据可视化
    fig = plt.figure(dpi=128,figsize=(10,6))
    #红色显示最高气温，蓝色显示最低气温
    plt.plot(dates,highs,c='red')
    plt.plot(dates,lows,c = 'blue')
    #向fill_between()函数传递一个x值：dates 两个y值：highs,lows 中间填充色:blue 透明度:0.5
    plt.fill_between(dates,highs,lows,facecolor = 'blue',alpha=0.5)

    #设置图形的格式
    plt.title("Nanjing weather conditions in the next seven days",fontsize=10)
    plt.xlabel('',fontsize=5)
    #来绘制斜的日期标签
    fig.autofmt_xdate()
    plt.ylabel("Temperature(F)",fontsize = 10)
    plt.tick_params(axis='both',which='major',labelsize = 10)
    plt.show()

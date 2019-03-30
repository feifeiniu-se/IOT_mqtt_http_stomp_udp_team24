import datetime
import time


def load_data(name):
    filename = "database/"+name+".txt"
    f = open(filename)
    values = []
    times = []
    line = f.readline()
    while line:
        words = line.strip().split(",")
        values.append(int(words[0]))
        time = timestamp2string(int(words[1].split(".")[0]))
        # print(time)

        # print(time)
        times.append(time)
        # times += words[1] + ", "
        line = f.readline()
    f.close()
    # print(times)
    # times = times[:-2]
    # times.strip().strip(",")
    # print(times)
    data = [values, times]
    # print(data[1])
    return data

def timestamp2string(timeStamp):
    try:
        d = datetime.datetime.fromtimestamp(timeStamp)
        # print("d: ", type(d))
        str1 = d.strftime("%Y-%m-%d %H:%M:%S.%f")
        # print("str1: ", type(str1))
        # 2015-08-28 16:43:37.283000'
        return str1
    except Exception as e:
        print(e)
        return ''

data_light = load_data('light')
print(data_light[1])

# print(datetime(2018-02-1 16:23:22).strftime("%Y-%m-%d %H:%M:%S"))
# print(datetime.strptime('2019-03-23 22:24:54.119974'))
# print(time.time())
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(time.time()))))
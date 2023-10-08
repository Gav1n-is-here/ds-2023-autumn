import time


time_start = time.perf_counter()  # 开始
# function()
muti=1
for i in range(10**7):
    muti*=i


time_end = time.perf_counter()  # 结束
time_sum = time_end - time_start  
print(time_sum,'秒')
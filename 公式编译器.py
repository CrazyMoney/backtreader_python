# import time
# import asyncio
#
# now = lambda : time.time()
#
# async def do_some_work(x):
#     print('Waiting: ', x)
#
# start = now()
#
# coroutine = do_some_work(2)
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(coroutine)
#
# print('TIME: ', now() - start)
import  numpy  as np

#最小二乘多项式拟合曲线
def gms(x,y,n:int ,A):
    try:
        P= np.polyfit(x,y,n)
    except Exception as e :
        res = '参数有误: {}'.format(e)
        return res
    ans = 0
    for i in range(n):
        pi  = i + 1
        print(P)
        ans = ans +  P[pi]* A**(n-i)
    return ans

x = [1,2,3]
y = [2,4,9]
x = np.array(x)
y= np.array(y)
res  = gms(x,y,2,4)
print(res)

import threading

def fuc(a):

    print('线程id为{}输出a:{}'.format(threading.current_thread(),a))

def run():
    for i in range(10):
        thr = threading.Thread(target= fuc,args=(i,),name= str(i))
        thr.start()


if __name__ == '__main__':

    run()
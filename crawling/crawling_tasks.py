from background_task import background
import time

def task_hello(schedule=1, repeat =2):
    time_tuple = time.localtime()
    time_str = time.strftime("%m/%d/%Ym, %H:%M:%S",time_tuple)
    print("task .... Hello World!",time_str)

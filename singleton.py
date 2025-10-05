import time


# class Database:
#     _instances={}
    
#     # works well for signle thread
#     def __new__(cls):
#         if cls not in cls._instances:
#             time.sleep(2)
#             cls._instances[cls]=super().__new__(cls)
#         return cls._instances[cls]
    

# if __name__=="__main__":
#     obj1=Database()
#     print(obj1)
#     obj2=Database()
#     print(obj2)

# <__main__.Database object at 0x000001AEAF386F90>
# <__main__.Database object at 0x000001AEAF386F90>

# for multi threading



        
from threading import Thread
import time

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        # intentionally slow down to trigger race
        time.sleep(0.5)
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=SingletonMeta):
    pass


def create_instance():
    obj = Database()
    print(f"Created instance id: {id(obj)}")


# Two threads try to create instance at same time
t1 = Thread(target=create_instance)
t2 = Thread(target=create_instance)

t1.start()
t2.start()
# t1.join()
# t2.join()

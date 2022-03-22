from ClassicSingleton import ClassicSingleton
import threading


def get_singleton_instance(dummy_var):
    s1 = ClassicSingleton.get_instance(dummy_var)

    print('s1: ', s1)
    print('s1.dummy_var', s1.dummy_var)


if __name__ == '__main__':

   thread1 = threading.Thread(target=get_singleton_instance, args=('FOO',))
   thread2 = threading.Thread(target=get_singleton_instance, args=('BAR',))

   thread1.start()
   thread2.start()

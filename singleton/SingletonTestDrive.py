from ClassicSingleton import ClassicSingleton


if __name__ == '__main__':

    dummy_var1 = 'dummy parameter 1'
    dummy_var2 = 'dummy parameter 2'
    dummy_var3 = 'dummy parameter 3'
    dummy_var4 = 'dummy parameter 4'

    s1 = ClassicSingleton.get_instance(dummy_var1)
    # s2 = Singleton()  # Throws an Exception
    s3 = ClassicSingleton.get_instance(dummy_var2)

    print('s1: ', s1)
    print('s3: ', s3)
    print('ClassicSingleton.get_instance(dummy_var3): ', ClassicSingleton.get_instance(dummy_var3))
    print('s1 == s3 == ClassicSingleton.get_instance(): ', s1 == s3 == ClassicSingleton.get_instance(dummy_var3))

    s1.get_description()
    s3.get_description()
    ClassicSingleton.get_description()
    ClassicSingleton.get_instance(dummy_var4).get_description()

    print('s1.dummy_var: ', s1.dummy_var)
    print('s3.dummy_var: ', s3.dummy_var)

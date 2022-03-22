

class ClassicSingleton:
    __instance = None   # Class attribute containing the reference to the instantiated Object

    @staticmethod
    def get_instance(dummy_var):
        if ClassicSingleton.__instance is None:
            ClassicSingleton(dummy_var)     # Instantiates the Singleton (calls __init__)

        return ClassicSingleton.__instance

    def __init__(self, dummy_var):
        if ClassicSingleton.__instance is None:
            ClassicSingleton.__instance = self
        else:   # If __init__ it tried called when the __instance already exists, throw an exception.
            raise Exception('This class is a singleton and it is already instantiated. '
                  'Use Singleton.get_instance() to get the instance')

        self.dummy_var = dummy_var  # Some singleton parameter

    @staticmethod
    def get_description():
        print('I am a classic Singleton!')



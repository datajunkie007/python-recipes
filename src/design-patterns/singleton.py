# Hello World of design pattern - Singelton. 
# Example for singleton design pattern.

class Singleton:
    # storage for the instance reference
    __instance = None

    """ A python singleton """

    class __impl:
        """ Implementation of the singleton interface """

        def get_id(self):
            """ Test method, return singleton id """
            return id(self)


    def __init__(self):
        """ Create singleton instance """
        # Check whether we already have an instance
        if Singleton.__instance is None:
            # Create and remember instance
            Singleton.__instance = Singleton.__impl()

        # Store instance reference as the only member in the handle
        self.__dict__['_Singleton__instance'] = Singleton.__instance

    def __getattr__(self, attr):
        """ Delegate access to implementation """
        return getattr(self.__instance, attr)

    def __setattr__(self, attr, value):
        """ Delegate access to implementation """
        return setattr(self.__instance, attr, value)


# Test it
s1 = Singleton()
print id(s1), s1.get_id()

s2 = Singleton()
print id(s2), s2.get_id()
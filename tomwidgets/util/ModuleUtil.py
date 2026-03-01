class ModuleUtil:
    @staticmethod
    def getName(module):
        return module.__name__

    @staticmethod
    def getCallable(module):
        results = {}
        for name in dir(module):
            attr = getattr(module, name)
            if callable(attr):
                results[name] = attr

        return results
    
    @staticmethod
    def getClasses(module):
        results = {}
        for name in dir(module):
            attr = getattr(module, name)
            if isinstance(attr, type):
                results[name] = attr

        return results

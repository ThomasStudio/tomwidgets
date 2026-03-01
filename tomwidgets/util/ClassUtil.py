import threading
from typing import TypeVar, Type, Optional, Any

T = TypeVar('T')


class SingletonMeta(type):
    """
    A thread-safe singleton metaclass.
    
    This metaclass ensures that only one instance of a class exists
    and provides thread-safe instantiation.
    """
    
    _instances: dict = {}
    _locks: dict = {}
    
    def __call__(cls: Type[T], *args: Any, **kwargs: Any) -> T:
        """
        Create or return the singleton instance.
        
        Args:
            *args: Positional arguments for the class constructor
            **kwargs: Keyword arguments for the class constructor
            
        Returns:
            T: The singleton instance
        """
        if cls not in cls._instances:
            if cls not in cls._locks:
                cls._locks[cls] = threading.Lock()
            
            with cls._locks[cls]:
                if cls not in cls._instances:
                    cls._instances[cls] = super().__call__(*args, **kwargs)
        
        return cls._instances[cls]


class SingletonBase(metaclass=SingletonMeta):
    """
    Base class for singleton classes.
    
    Inherit from this class to create a singleton.
    The class will automatically ensure only one instance exists.
    """
    
    def __init__(self) -> None:
        """
        Initialize the singleton instance.
        
        Override this method in subclasses to add custom initialization.
        """
        pass
    
    @classmethod
    def getInstance(cls: Type[T]) -> T:
        """
        Get the singleton instance.
        
        Returns:
            T: The singleton instance
        """
        return cls()
    
    @classmethod
    def resetInstance(cls) -> None:
        """
        Reset the singleton instance.
        
        This allows creating a new instance for testing or reinitialization.
        """
        if cls in cls._instances:
            del cls._instances[cls]


class ClassUtil:
    @staticmethod
    def getAll(cls) -> dict:
        return {k: v for k, v in cls.__dict__.items() if not k.startswith('_')}

    @staticmethod
    def getValues(cls) -> dict:
        dc = ClassUtil.getAll(cls)
        return {k: v for k, v in dc.items() if not callable(v)}

    @staticmethod
    def getMethods(cls) -> dict:
        dc = ClassUtil.getAll(cls)
        return {k: v for k, v in dc.items() if callable(v)}
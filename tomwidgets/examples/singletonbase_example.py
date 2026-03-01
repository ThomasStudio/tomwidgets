import threading
import time
from tomwidgets.util import SingletonBase, SingletonMeta


class SimpleSingleton(SingletonBase):
    """A simple singleton class using SingletonBase."""
    
    def __init__(self) -> None:
        super().__init__()
        self.counter = 0
        self.name = "SimpleSingleton"
    
    def increment(self) -> int:
        """Increment the counter and return the new value."""
        self.counter += 1
        return self.counter
    
    def getName(self) -> str:
        """Get the name of this singleton."""
        return self.name


class ConfigManager(SingletonBase):
    """A configuration manager singleton."""
    
    def __init__(self) -> None:
        super().__init__()
        self.settings = {
            "theme": "dark",
            "language": "en",
            "autoSave": True,
            "maxHistory": 100
        }
    
    def getSetting(self, key: str) -> str:
        """Get a setting value."""
        return self.settings.get(key, "")
    
    def setSetting(self, key: str, value: str) -> None:
        """Set a setting value."""
        self.settings[key] = value
    
    def getAllSettings(self) -> dict:
        """Get all settings."""
        return self.settings.copy()


class ThreadSafeCounter(SingletonBase):
    """A thread-safe counter singleton for testing concurrency."""
    
    def __init__(self) -> None:
        super().__init__()
        self._counter = 0
        self._lock = threading.Lock()
    
    def increment(self) -> int:
        """Thread-safe increment operation."""
        with self._lock:
            self._counter += 1
            return self._counter
    
    def getValue(self) -> int:
        """Get the current counter value."""
        return self._counter


def demonstrateBasicSingleton():
    """Demonstrate basic singleton functionality."""
    print("=== Basic Singleton Demonstration ===")
    
    # Create first instance
    singleton1 = SimpleSingleton()
    print(f"Singleton1 ID: {id(singleton1)}")
    print(f"Singleton1 name: {singleton1.getName()}")
    
    # Create second instance - should be the same object
    singleton2 = SimpleSingleton()
    print(f"Singleton2 ID: {id(singleton2)}")
    print(f"Are they the same object? {singleton1 is singleton2}")
    
    # Use getInstance method
    singleton3 = SimpleSingleton.getInstance()
    print(f"Singleton3 ID: {id(singleton3)}")
    print(f"All instances are the same? {singleton1 is singleton2 and singleton2 is singleton3}")
    
    # Test counter functionality
    print(f"Initial counter: {singleton1.counter}")
    singleton1.increment()
    print(f"After increment on singleton1: {singleton1.counter}")
    print(f"Counter on singleton2: {singleton2.counter}")
    print()


def demonstrateConfigManager():
    """Demonstrate configuration manager singleton."""
    print("=== Configuration Manager Demonstration ===")
    
    # Get config manager instance
    config1 = ConfigManager()
    print("Initial settings:")
    for key, value in config1.getAllSettings().items():
        print(f"  {key}: {value}")
    
    # Modify settings through first instance
    config1.setSetting("theme", "light")
    config1.setSetting("language", "fr")
    
    # Get second instance and verify changes
    config2 = ConfigManager()
    print("Settings after modification:")
    for key, value in config2.getAllSettings().items():
        print(f"  {key}: {value}")
    
    print(f"Are config managers the same object? {config1 is config2}")
    print()


def demonstrateThreadSafety():
    """Demonstrate thread safety of singleton pattern."""
    print("=== Thread Safety Demonstration ===")
    
    results = []
    
    def incrementCounter(threadId: int) -> None:
        """Thread function to increment counter."""
        counter = ThreadSafeCounter()
        for _ in range(100):
            value = counter.increment()
            results.append((threadId, value))
        
    # Create multiple threads
    threads = []
    for i in range(5):
        thread = threading.Thread(target=incrementCounter, args=(i,))
        threads.append(thread)
    
    # Start threads
    for thread in threads:
        thread.start()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    
    # Verify final counter value
    finalCounter = ThreadSafeCounter()
    print(f"Final counter value: {finalCounter.getValue()}")
    print(f"Expected value (5 threads * 100 increments): 500")
    print(f"Test passed: {finalCounter.getValue() == 500}")
    print()


def demonstrateResetFunctionality():
    """Demonstrate reset functionality for testing."""
    print("=== Reset Functionality Demonstration ===")
    
    # Create and use a singleton
    singleton = SimpleSingleton()
    singleton.increment()
    singleton.increment()
    print(f"Counter before reset: {singleton.counter}")
    
    # Reset the singleton
    SimpleSingleton.resetInstance()
    
    # Create new instance
    newSingleton = SimpleSingleton()
    print(f"Counter after reset: {newSingleton.counter}")
    print(f"Are they the same object? {singleton is newSingleton}")
    print()


def demonstrateMetaclassUsage():
    """Demonstrate using SingletonMeta directly."""
    print("=== Metaclass Usage Demonstration ===")
    
    class CustomSingleton(metaclass=SingletonMeta):
        """A custom singleton using the metaclass directly."""
        
        def __init__(self, customName: str = "Default") -> None:
            self.customName = customName
            self.createdAt = time.time()
    
    # Create instances with different parameters
    # Note: With singleton pattern, only the first initialization parameters are used
    instance1 = CustomSingleton("First")
    instance2 = CustomSingleton("Second")  # This will use the same instance
    
    print(f"Instance1 customName: {instance1.customName}")
    print(f"Instance2 customName: {instance2.customName}")
    print(f"Are they the same? {instance1 is instance2}")
    print()


def demonstrateMultipleSingletons():
    """Demonstrate that different singleton classes are separate."""
    print("=== Multiple Singletons Demonstration ===")
    
    # Create instances of different singleton classes
    simple = SimpleSingleton()
    config = ConfigManager()
    counter = ThreadSafeCounter()
    
    print(f"SimpleSingleton ID: {id(simple)}")
    print(f"ConfigManager ID: {id(config)}")
    print(f"ThreadSafeCounter ID: {id(counter)}")
    
    # Verify they are different objects
    print(f"All are different objects: {simple is not config and config is not counter and counter is not simple}")
    
    # Verify each maintains its own state
    simple.increment()
    config.setSetting("test", "value")
    counter.increment()
    
    # Get second instances
    simple2 = SimpleSingleton()
    config2 = ConfigManager()
    counter2 = ThreadSafeCounter()
    
    print(f"SimpleSingleton state preserved: {simple.counter == simple2.counter}")
    print(f"ConfigManager state preserved: {config.getSetting('test') == config2.getSetting('test')}")
    print(f"ThreadSafeCounter state preserved: {counter.getValue() == counter2.getValue()}")
    print()


def main():
    """Run all demonstration functions."""
    print("SingletonBase Example - Reusable Singleton Pattern")
    print("=" * 60)
    print()
    
    # Run all demonstrations
    demonstrateBasicSingleton()
    demonstrateConfigManager()
    demonstrateThreadSafety()
    demonstrateResetFunctionality()
    demonstrateMetaclassUsage()
    demonstrateMultipleSingletons()
    
    print("=" * 60)
    print("Example completed successfully!")
    print()
    print("Key Features Demonstrated:")
    print("✓ Singleton pattern with thread safety")
    print("✓ Reusable base class (SingletonBase)")
    print("✓ Reusable metaclass (SingletonMeta)")
    print("✓ Instance reset for testing")
    print("✓ Multiple singleton classes coexist")
    print("✓ getInstance() convenience method")


if __name__ == "__main__":
    main()
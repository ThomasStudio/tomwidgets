import sys
import os

# Add the parent directory to the path to import tomwidgets
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tomwidgets.util import EventBus


def demonstrateBasicEventBus():
    """Demonstrate basic EventBus functionality."""
    print("=== Basic EventBus Demonstration ===")
    
    # Create an EventBus instance
    eventBus = EventBus()
    
    # Define some event handlers that accept keyword arguments
    def onUserLogin(**kwargs):
        print(f"User logged in: {kwargs.get('username', 'Unknown')}")
    
    def onUserLogout(**kwargs):
        print(f"User logged out: {kwargs.get('username', 'Unknown')}")
    
    def onDataUpdated(**kwargs):
        print(f"Data updated: {kwargs.get('type', 'Unknown')} - {kwargs.get('count', 0)} items")
    
    # Bind events to handlers
    eventBus.bindEvent(onUserLogin, "userLogin")
    eventBus.bindEvent(onUserLogout, "userLogout")
    eventBus.bindEvent(onDataUpdated, "dataUpdated")
    
    # Generate events
    print("\nGenerating events:")
    eventBus.generateEvent("userLogin", username="john_doe", timestamp="2024-01-15 10:30:00")
    eventBus.generateEvent("dataUpdated", type="users", count=150)
    eventBus.generateEvent("userLogout", username="john_doe", timestamp="2024-01-15 11:30:00")
    
    print(f"\nHandler counts:")
    print(f"userLogin handlers: {eventBus.getHandlerCount('userLogin')}")
    print(f"userLogout handlers: {eventBus.getHandlerCount('userLogout')}")
    print(f"dataUpdated handlers: {eventBus.getHandlerCount('dataUpdated')}")
    
    print()


def demonstrateMultipleHandlers():
    """Demonstrate multiple handlers for the same event."""
    print("=== Multiple Handlers Demonstration ===")
    
    eventBus = EventBus()
    
    # Define multiple handlers for the same event
    def logMessage(**kwargs):
        print(f"[LOG] Message: {kwargs.get('text', 'No text')}")
    
    def notifyUser(**kwargs):
        print(f"[NOTIFICATION] New message: {kwargs.get('text', 'No text')}")
    
    def updateUI(**kwargs):
        print(f"[UI] Updating display with: {kwargs.get('text', 'No text')}")
    
    # Bind all handlers to the same event
    eventBus.bindEvent(logMessage, "newMessage")
    eventBus.bindEvent(notifyUser, "newMessage")
    eventBus.bindEvent(updateUI, "newMessage")
    
    print(f"Number of handlers for 'newMessage': {eventBus.getHandlerCount('newMessage')}")
    
    # Generate the event - all handlers should be called
    print("\nGenerating newMessage event:")
    eventBus.generateEvent("newMessage", text="Hello, World!", sender="system")
    
    print()


def demonstrateErrorHandling():
    """Demonstrate error handling in event handlers."""
    print("=== Error Handling Demonstration ===")
    
    eventBus = EventBus()
    
    def goodHandler(**kwargs):
        print(f"Good handler received: {kwargs.get('value', 'No value')}")
    
    def badHandler(**kwargs):
        raise ValueError("This handler always fails!")
    
    def anotherGoodHandler(**kwargs):
        print(f"Another good handler received: {kwargs.get('value', 'No value')}")
    
    # Bind handlers
    eventBus.bindEvent(goodHandler, "testEvent")
    eventBus.bindEvent(badHandler, "testEvent")
    eventBus.bindEvent(anotherGoodHandler, "testEvent")
    
    # Generate event - bad handler should fail but others should still work
    print("Generating testEvent (one handler will fail):")
    eventBus.generateEvent("testEvent", value=42)
    
    print()


def demonstrateUnbinding():
    """Demonstrate unbinding event handlers."""
    print("=== Unbinding Demonstration ===")
    
    eventBus = EventBus()
    
    def handler1(**kwargs):
        print("Handler 1 called")
    
    def handler2(**kwargs):
        print("Handler 2 called")
    
    def handler3(**kwargs):
        print("Handler 3 called")
    
    # Bind all handlers
    eventBus.bindEvent(handler1, "myEvent")
    eventBus.bindEvent(handler2, "myEvent")
    eventBus.bindEvent(handler3, "myEvent")
    
    print(f"Initial handler count: {eventBus.getHandlerCount('myEvent')}")
    
    # Generate event with all handlers
    print("\nGenerating event with all handlers:")
    eventBus.generateEvent("myEvent")
    
    # Unbind one specific handler
    eventBus.unbindEvent(handler2, "myEvent")
    print(f"\nAfter unbinding handler2: {eventBus.getHandlerCount('myEvent')}")
    
    # Generate event again
    print("Generating event after unbinding handler2:")
    eventBus.generateEvent("myEvent")
    
    # Unbind all handlers for the event
    eventBus.unbindEvent(eventName="myEvent")
    print(f"\nAfter unbinding all handlers: {eventBus.getHandlerCount('myEvent')}")
    
    # Generate event - no handlers should be called
    print("Generating event with no handlers:")
    eventBus.generateEvent("myEvent")
    
    print()


def demonstrateDefaultEvent():
    """Demonstrate default event functionality."""
    print("=== Default Event Demonstration ===")
    
    # Create EventBus with custom default event
    eventBus = EventBus(defaultEvent="systemEvent")
    
    def defaultHandler(**kwargs):
        print(f"Default handler received: {kwargs.get('message', 'No message')}")
    
    def specificHandler(**kwargs):
        print(f"Specific handler received: {kwargs.get('message', 'No message')}")
    
    # Bind to default event (no event name specified)
    eventBus.bindEvent(defaultHandler)
    
    # Bind to specific event
    eventBus.bindEvent(specificHandler, "customEvent")
    
    print("\nGenerating default event (no event name):")
    eventBus.generateEvent(message="This goes to default event handlers")
    
    print("\nGenerating specific event:")
    eventBus.generateEvent("customEvent", message="This goes to custom event handlers")
    
    print(f"\nDefault event handler count: {eventBus.getHandlerCount()}")
    print(f"Custom event handler count: {eventBus.getHandlerCount('customEvent')}")
    
    print()


def demonstrateEventChecking():
    """Demonstrate checking if events have handlers."""
    print("=== Event Checking Demonstration ===")
    
    eventBus = EventBus()
    
    def sampleHandler(**kwargs):
        print("Sample handler called")
    
    # Check events before binding
    print("Before binding:")
    print(f"Has 'event1' handlers: {eventBus.hasEvent('event1')}")
    print(f"Has 'event2' handlers: {eventBus.hasEvent('event2')}")
    
    # Bind handler to event1
    eventBus.bindEvent(sampleHandler, "event1")
    
    print("\nAfter binding to 'event1':")
    print(f"Has 'event1' handlers: {eventBus.hasEvent('event1')}")
    print(f"Has 'event2' handlers: {eventBus.hasEvent('event2')}")
    
    print()


def main():
    """Run all EventBus demonstrations."""
    print("EventBus Example - Simple Event System")
    print("=" * 50)
    print()
    
    # Run all demonstrations
    demonstrateBasicEventBus()
    demonstrateMultipleHandlers()
    demonstrateErrorHandling()
    demonstrateUnbinding()
    demonstrateDefaultEvent()
    demonstrateEventChecking()
    
    print("=" * 50)
    print("EventBus example completed successfully!")


if __name__ == "__main__":
    main()
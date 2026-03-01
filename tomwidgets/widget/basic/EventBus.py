from typing import Callable, Dict, List


class EventBus:
    def __init__(self, defaultEvent: str = 'defaultEvent') -> None:
        self.defaultEvent: str = defaultEvent
        self._eventHandlers: Dict[str, List[Callable]] = {}

    def eventName(self, event: str = None) -> str:
        return event if event is not None else self.defaultEvent

    def bindEvent(self, handler: Callable, eventName: str = None) -> None:
        eventName = self.eventName(eventName)

        if eventName not in self._eventHandlers:
            self._eventHandlers[eventName] = []
        self._eventHandlers[eventName].append(handler)

    def generateEvent(self, eventName: str = None, **kwargs) -> None:
        eventName = self.eventName(eventName)

        if eventName in self._eventHandlers:
            for handler in self._eventHandlers[eventName]:
                try:
                    handler(**kwargs)
                except Exception as e:
                    print(f"Error in event handler for {eventName}: {e}")

    def unbindEvent(self, handler: Callable = None, eventName: str = None) -> None:
        eventName = self.eventName(eventName)

        if eventName in self._eventHandlers:
            if handler is None:
                self._eventHandlers[eventName].clear()
            else:
                if handler in self._eventHandlers[eventName]:
                    self._eventHandlers[eventName].remove(handler)

    def getHandlerCount(self, eventName: str = None) -> int:
        eventName = self.eventName(eventName)

        if eventName in self._eventHandlers:
            return len(self._eventHandlers[eventName])
        return 0

    def hasEvent(self, eventName: str) -> bool:
        eventName = self.eventName(eventName)
        return eventName in self._eventHandlers and len(self._eventHandlers[eventName]) > 0
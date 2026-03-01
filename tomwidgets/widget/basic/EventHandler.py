"""handle the event of the widget"""


class EventHandler:
    def __init__(self, eventName: str = '<<EventName>>'):
        self.eventName = eventName
        self.panel = None

        if hasattr(self, '_canvas'):
            self.panel = self._canvas
        else:
            self.panel = self

    def generateEvent(self, event: str = None, when: str = 'tail'):
        """Generate an event on the canvas"""
        event = self.formatEvent(event)

        print(f"generateEvent: {event}")
        if self.panel:
            self.panel.event_generate(event, when=when)
        else:
            raise Exception("No canvas found")

    def bindEvent(self, callback, event: str = None, add: bool = True):
        event = self.formatEvent(event)
        print(f"bindEvent: {event}")
        self.bind(event, callback, add=add)

    def formatEvent(self, event: str | None) -> str:
        if event is None:
            event = self.eventName

        if not event.startswith('<'):
            event = f'<<{event}>>'

        return event

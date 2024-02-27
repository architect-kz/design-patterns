from __future__ import annotations

from abc import abstractmethod, ABC


class ISubject(ABC):
    @abstractmethod
    def attach(self, observer: IObserver) -> None:
        pass

    @abstractmethod
    def detach(self, observer: IObserver) -> None:
        pass

    @abstractmethod
    def notify(self, data) -> None:
        pass


class IObserver(ABC):
    @abstractmethod
    def update(self, subject: ISubject) -> None:
        pass


class Subject(ISubject):
    _observers: list = []

    def __init__(self):
        ...

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, data):
        for observer in self._observers:
            observer.update(data)


class EmailNotifier(IObserver):
    def update(self, data):
        print(f"Sending email notification: {data}")


class SMSNotifier(IObserver):
    def update(self, data):
        print(f"Sending SMS notification: {data}")


# Клиентский код
subject = Subject()
email_notifier = EmailNotifier()
sms_notifier = SMSNotifier()

subject.attach(email_notifier)
subject.attach(sms_notifier)

# При изменении состояния субъекта, происходит уведомление всех наблюдателей.
subject.notify("Important update!")

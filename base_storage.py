from abstract_storage import AbstractStorage

from exceptions import NotEnoughSpace, NotEnoughProduct


class BaseStorage(AbstractStorage):
    def __init__(self, items: dict[str, int], capacity: int):
        self.__items = items
        self.__capacity = capacity

    def add(self, name: str, amount: int) -> None:
        if self.get_free_space() < amount:
            raise NotEnoughSpace

        self.get_items()[name] = self.get_items().get(name, 0) + amount

    def remove(self, name: str, amount: int) -> None:
        if name not in self.get_items().keys() and not self.get_items().get(name, 0) > amount:
            raise NotEnoughProduct

        self.get_items()[name] -= amount

        if self.get_items()[name] == 0:
            self.get_items().pop(name)

    def get_free_space(self):
        return self.__capacity - sum(self.get_items().values())

    def get_items(self):
        return self.__items

    def get_unique_items_count(self):
        return len(self.get_items())

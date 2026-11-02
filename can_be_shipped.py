# can_be_shipped.py
# An "interface" made with an abstract base class.
# Any class that can be shipped must promise to write calculate_shipping_cost().

from abc import ABC, abstractmethod


class CanBeShipped(ABC):
    @abstractmethod
    def calculate_shipping_cost(self):
        pass

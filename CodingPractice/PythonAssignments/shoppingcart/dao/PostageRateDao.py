from abc import ABC, abstractmethod


class PostageRateDao(ABC):

    @abstractmethod
    def get_postage_rates(self):
        return

    @abstractmethod
    def get_postage_rates_by_iso_country_code(self, iso_country_code):
        return

    @abstractmethod
    def get_postage_rates_by_weight(self, weight):
        return

    @abstractmethod
    def get_postage_rates_by_postage_class(self, postage_class):
        return

    @abstractmethod
    def get_appropriate_postage_rate(self, iso_country_code, weight, postage_class):
        return

    @abstractmethod
    def create_postage_rate(self, postageDto):
        return

    @staticmethod
    def _convert_weight(w):
        if w <= 1000:
            return 1000
        elif w > 1000:
            return 2000

    @staticmethod
    def delete_postage_rate(self, postageDto):
        return

    @staticmethod
    def update_postage_rate(self, postageDto):
        return

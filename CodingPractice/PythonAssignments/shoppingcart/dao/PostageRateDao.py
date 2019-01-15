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
    def get_postage_rate(self, iso_country_code, weight, postage_class):
        return

    @abstractmethod
    def create_postage_matrix(self, postageDto):
        return

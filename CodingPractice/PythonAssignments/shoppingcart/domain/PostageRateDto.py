
class PostageRateDto:

    def __init__(self, country_iso_code, weight, postage_class, rate):
        self._country_iso_code = country_iso_code
        self._weight = weight
        self._postage_class = postage_class
        self._rate = rate

    def __eq__(self, other):
        return self._country_iso_code == other._country_iso_code and self._weight == other._weight and \
            self._postage_class == other._postage_class and self._rate == other._rate

    def get_country_iso_code(self):
        return self._country_iso_code

    def get_weight(self):
        return self._weight

    def get_postage_class(self):
        return self._postage_class

    def get_rate(self):
        return self._rate

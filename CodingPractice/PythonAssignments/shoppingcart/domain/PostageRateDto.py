
class PostageRateDto:

    def __init__(self, iso_country_code, weight, postage_class, rate):
        self._iso_country_code = iso_country_code
        self._weight = weight
        self._postage_class = postage_class
        self._rate = rate

    def __eq__(self, other):
        return self._iso_country_code == other._iso_country_code and self._weight == other._weight and \
            self._postage_class == other._postage_class and self._rate == other._rate

    def get_iso_country_code(self):
        return self._iso_country_code

    def get_weight(self):
        return self._weight

    def get_postage_class(self):
        return self._postage_class

    def get_rate(self):
        return self._rate

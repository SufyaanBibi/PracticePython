class PostageRateCache:

    def __init__(self):
        self._postage_rate_cache = {}

    def _make_postage_rate_cache(self, postage_rate_dtos):
        for postage_rate_dto in postage_rate_dtos:
            country = postage_rate_dto.get_iso_country_code()
            new_weight = postage_rate_dto.get_weight()
            new_postage_class = postage_rate_dto.get_postage_class()
            rate = postage_rate_dto.get_rate()

            if postage_rate_dto.get_weight() == '1kg':
                new_weight = 1000
            elif postage_rate_dto.get_weight() == '2kg':
                new_weight = 2000

            if postage_rate_dto.get_postage_class() == '1st Class':
                new_postage_class = 1
            elif postage_rate_dto.get_postage_class() == '2nd Class':
                new_postage_class = 2

            t = (country, new_weight, new_postage_class)
            self._postage_rate_cache[t] = rate

    def _clear_cache(self):
        self._postage_rate_cache.clear()

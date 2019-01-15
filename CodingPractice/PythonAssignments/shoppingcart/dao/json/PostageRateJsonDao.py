from CodingPractice.PythonAssignments.shoppingcart.dao.json.JsonFileReader import JsonFileReader
from CodingPractice.PythonAssignments.shoppingcart.dao.PostageRateDao import PostageRateDao
from CodingPractice.PythonAssignments.shoppingcart.domain.PostageRateDto import PostageRateDto


class PostageRateJsonDao(PostageRateDao, JsonFileReader):

    @staticmethod
    def _create_postage_rate_dto(postage_matrix):
        return PostageRateDto(postage_matrix["country_iso_code"], postage_matrix["weight"],
                              postage_matrix["postage_class"], postage_matrix["rate"])

    @staticmethod
    def _make_postage_rate_dtos_from_json(j):
        postage_matrix = []
        for postage in j["postage_matrix"]:
            postage_matrix.append(PostageRateJsonDao._create_postage_rate_dto(postage))
        return postage_matrix

    @staticmethod
    def _make_postage_rate_dict(postage_matrix):
        postage_dict = {}
        for postage_rate_dto in postage_matrix:
            country = postage_rate_dto.get_country_iso_code()
            new_weight = postage_rate_dto.get_weight()
            new_postage_class = postage_rate_dto.get_postage_class()
            rate = postage_rate_dto.get_rate()
            if postage_rate_dto.get_weight() == '1kg' and postage_rate_dto.get_postage_class() == '1st Class':
                new_weight = 1000
                new_postage_class = 1
            elif postage_rate_dto.get_weight() == '1kg' and postage_rate_dto.get_postage_class() == '2nd Class':
                new_weight = 1000
                new_postage_class = 2
            elif postage_rate_dto.get_weight() == '2kg' and postage_rate_dto.get_postage_class() == '1st Class':
                new_weight = 2000
                new_postage_class = 1
            elif postage_rate_dto.get_weight() == '2kg' and postage_rate_dto.get_postage_class() == '2nd Class':
                new_weight = 2000
                new_postage_class = 2
            t = (country, new_weight, new_postage_class)
            postage_dict[t] = rate
        return postage_dict

    def __init__(self, json_file_path):
        self._json_file_path = json_file_path
        self._postage_dict = self._make_postage_rate_dict(self.get_postage_rates())

    def get_postage_rates(self):
        jf = PostageRateJsonDao._get_json(self._json_file_path)
        return self._make_postage_rate_dtos_from_json(jf)

    def get_postage_rates_by_iso_country_code(self, iso_country_code):
        postages_matrix = self.get_postage_rates()
        return [postage for postage in postages_matrix if iso_country_code == postage.get_country_iso_code()]

    def get_postage_rates_by_weight(self, weight):
        postages_matrix = self.get_postage_rates()
        return [postage for postage in postages_matrix if weight == postage.get_weight()]

    def get_postage_rates_by_postage_class(self, postage_class):
        postages_matrix = self.get_postage_rates()
        return [postage for postage in postages_matrix if postage_class == postage.get_postage_class()]

    def get_postage_rate(self, iso_country_code, weight, postage_class):
        if weight < 1000:
            weight = 1000
        elif weight > 1000:
            weight = 2000
        key = (iso_country_code, weight, postage_class)
        return self._postage_dict[key]

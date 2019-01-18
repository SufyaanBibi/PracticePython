from CodingPractice.PythonAssignments.shoppingcart.dao.json.JsonFileReader import JsonFileReader
from CodingPractice.PythonAssignments.shoppingcart.dao.PostageRateCache import PostageRateCache
from CodingPractice.PythonAssignments.shoppingcart.dao.PostageRateDao import PostageRateDao
from CodingPractice.PythonAssignments.shoppingcart.domain.PostageRateDto import PostageRateDto


class MethodNotImplementedException(Exception):
    def __init__(self, message):
        self._message = message


class PostageRateJsonDao(PostageRateDao, JsonFileReader, PostageRateCache):

    @staticmethod
    def _create_postage_rate_dto(postage_matrix):
        return PostageRateDto(postage_matrix["iso_country_code"], postage_matrix["weight"],
                              postage_matrix["postage_class"], postage_matrix["rate"])

    @staticmethod
    def _make_postage_rate_dtos_from_json(j):
        postage_matrix = []
        for postage in j["postage_matrix"]:
            postage_matrix.append(PostageRateJsonDao._create_postage_rate_dto(postage))
        return postage_matrix

    def __init__(self, json_file_path):
        super().__init__()
        self._json_file_path = json_file_path
        self._make_postage_rate_cache(self.get_postage_rates())

    def get_postage_rates(self):
        jf = PostageRateJsonDao._get_json(self._json_file_path)
        return self._make_postage_rate_dtos_from_json(jf)

    def get_postage_rates_by_iso_country_code(self, iso_country_code):
        postages_matrix = self.get_postage_rates()
        return [postage for postage in postages_matrix if iso_country_code == postage.get_iso_country_code()]

    def get_postage_rates_by_weight(self, weight):
        postages_matrix = self.get_postage_rates()
        return [postage for postage in postages_matrix if weight == postage.get_weight()]

    def get_postage_rates_by_postage_class(self, postage_class):
        postages_matrix = self.get_postage_rates()
        return [postage for postage in postages_matrix if postage_class == postage.get_postage_class()]

    def get_postage_rate(self, iso_country_code, weight, postage_class):
        key = (iso_country_code, self._convert_weight(weight), postage_class)
        return self._postage_rate_cache[key]

    def create_postage_rate(self, postageDto):
        raise MethodNotImplementedException('create_postage_rate called on PostageJsonDao')


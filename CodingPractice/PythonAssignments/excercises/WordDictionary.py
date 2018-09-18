from abc import ABC, abstractmethod
import os
import json
import requests


class Dictionary(ABC):

    @abstractmethod
    def look_up(self, word):
        return


class LocalDictionary(Dictionary):

    def __init__(self, file_name):
        self.inner_dict = LocalDictionary.get_dict(file_name)

    @staticmethod
    def get_file_path(file_name):
        return os.path.join(os.path.dirname(__file__), file_name)

    @staticmethod
    def make_list_of_word_definitions(file_name):
        sp = LocalDictionary.get_file_path(file_name)
        with open(sp, 'r') as fh:
            return [word.strip().split(',') for word in fh.readlines()]

    @staticmethod
    def get_dict(file_name):
        words = LocalDictionary.make_list_of_word_definitions(file_name)
        return {word: value for word, value in words}

    def look_up(self, word):
        try:
            return [self.inner_dict[word]]
        except KeyError:
            return [f'{word} not found in LocalDictionary']


class OxfordDictionary(Dictionary):

    @staticmethod
    def get_definitions(json_text):
        list_of_definitions = []
        a = json.loads(json_text)
        for lexicalEntry in a['results'][0]['lexicalEntries']:
            entries = lexicalEntry['entries']
            for entry in entries:
                senses = entry['senses']
                for sense in senses:
                    short_definitions = sense['short_definitions']
                    list_of_definitions.append(short_definitions)

        return [item for sublist in list_of_definitions for item in sublist]

    def look_up(self, word):
        _app_id = '9286dd2e'
        _app_key = '8651b0907938b33bb76e99cb157288d2'
        _language = 'en'

        url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + _language + '/' + word.lower()

        r = requests.get(url, headers={'app_id': _app_id, 'app_key': _app_key})

        return OxfordDictionary.get_definitions(r.text)

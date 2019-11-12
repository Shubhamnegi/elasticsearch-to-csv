from abc import ABC, abstractmethod


class RegexManager(ABC):
    regex = None
    header = None
    search_string = None

    def get_regex(self):
        return self.regex

    def get_header(self):
        return self.header

    def get_search_string(self):
        return self.search_string

    @abstractmethod
    def formatted_csv_line(self, data, body=None):
        pass

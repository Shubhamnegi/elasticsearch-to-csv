from services.regex_manager import RegexManager


class SearchElapsedTime(RegexManager):
    regex = '{\"name\":(?P<module>\"[\w\-]+\"),\"hostname\":(?P<hostname>\"[\w\-]+\"),.+,\"elapsedTime\":(?P<elapsedTime>\d+),\"url\":\"(?P<url>\S+)\",'
    header = "module,hostname,elapsedTime,url\n"
    search_string = 'kubernetes_container_name:order-online-service AND kubernetes_pod_name:order-online-service-6cb8b7b55c-fwlp4 AND elapsedTime'

    def formatted_csv_line(self, data):
        result = f"{data['module']},{data['hostname']},{data['elapsedTime']},{data['url']}\n"
        return result

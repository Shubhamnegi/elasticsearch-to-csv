from services.regex_manager import RegexManager


class LtEndTimeLog(RegexManager):
    regex = '\[(?P<datetime>\d+-\d+-\d+\s\d+:\d+:\d+)\]\s\S+\s\{\\"\w+\\":\\"(?P<requestId>\S+)\\"\,\\"\w+\\":\\"Request Ended for url:\s(?P<url>[\w\d\\\/]+)\sin\s(?P<timeTaken>[\d\.]+)\\"\,\\"timeStamp\\":\\"(?P<microTime>[\d\-T\:\+]+)'
    header = "datetime,requestId,url,timeTaken,microTime\n"
    search_string = '\"Request Ended for url\" AND source:\"/home/logistic/lt_backbone/storage/logs/laravel.log\"'

    def formatted_csv_line(self, data):
        result = f"{data['datetime']},{data['requestId']},{data['url']},{data['timeTaken']},{data['microTime']}\n"
        return result

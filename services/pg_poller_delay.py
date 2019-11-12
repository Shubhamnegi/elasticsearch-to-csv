from services.regex_manager import RegexManager


class PgPollerDelay(RegexManager):
    regex = '\{\\"level\\"\:\d+\,\\"time\\"\:(?P<time>\d+).+Published\sevent\s(?P<orderId>\w+)\s(?P<event>\w+).+publishTimeTaken\:(?P<publishTimeTaken>\d+).+relayDelay:(?P<relayDelay>\d+)'
    header = "time,orderId,event,publishTimeTaken,relayDelay\n"
    search_string = 'kubernetes_container_name:pg-polling-service AND \"publishTimeTaken\"'

    def formatted_csv_line(self, data):
        result = f"{data['time']},{data['orderId']},{data['event']},{data['publishTimeTaken']},{data['relayDelay']}\n"
        return result

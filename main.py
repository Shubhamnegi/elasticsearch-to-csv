from elasticsearch import Elasticsearch
import certifi
import os
import re
from services.lt_end_time_log import LtEndTimeLog
from services.search_elapsed_time import SearchElapsedTime


def query_elastic(host, index, query, start_time, end_time, skip=0, limit=150, sort="asc"):
    print(f"connecting host: {host}")
    es = Elasticsearch(host, use_ssl=True, ca_certs=certifi.where())
    query = {
        "from": skip,
        "size": limit,
        "query": {
            "bool": {
                "must": {
                    "query_string": {
                        "query": query,
                        "allow_leading_wildcard": True
                    }
                },
                "filter": {
                    "bool": {
                        "must": {
                            "range": {
                                "timestamp": {
                                    "from": start_time,
                                    "to": end_time,
                                    "include_lower": True,
                                    "include_upper": True
                                }
                            }
                        }
                    }
                }
            }
        },
        "sort": [
            {
                "timestamp": {
                    "order": "asc"
                }
            }
        ]
    }
    return es.search(index=index, body=query)


def get_result_csv_path():
    dir_path = os.getcwd()
    csv_path = os.path.abspath(dir_path+"/result.csv")
    return csv_path


def delete_csv():
    csv = get_result_csv_path()
    try:
        os.remove(csv)
    except FileNotFoundError as e:
        print(e)


if __name__ == "__main__":
    index = "graylog_681"
    host = ["https://elastic.limetray.com"]
    # delete_csv()

    csvRegexHelper = SearchElapsedTime()

    f = open(get_result_csv_path(), "a+")
    f.write(csvRegexHelper.get_header())
    try:
        skip = 2700
        limit = 150
        start_time = "2019-11-11 18:00:19.881"
        end_time = "2019-11-11 19:28:19.881"
        print(f"Parsing log for {start_time}-{end_time}")
        while(True):
            print(
                f"skip:{skip}, limit:{limit},search: {csvRegexHelper.search_string}")
            response = query_elastic(host=host, index=index, query=csvRegexHelper.search_string, start_time=start_time,
                                     end_time=end_time, skip=skip, limit=limit)
            if "hits" in response and response['hits']['total'] > 0 and len(response['hits']['hits']) > 0:
                for hit in response['hits']['hits']:
                    message = hit['_source']['message']
                    regex = csvRegexHelper.get_regex()
                    m = re.match(regex, message)
                    result = m.groupdict()
                    f.write(csvRegexHelper.formatted_csv_line(result))
            else:
                break
            skip = skip+limit

    except Exception as e:
        print(f"Exception occured: {e}")
    f.close()

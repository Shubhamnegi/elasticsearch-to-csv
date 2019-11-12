from services.regex_manager import RegexManager


class PodThreads(RegexManager):
    regex = '(?P<thread>(nio|http|pool)[\-\w\d]+)'
    header = "timestamp,pod,threadId\n"
    search_string = '(kubernetes_pod_name:ecommerce-service-5c9f9c5857-vlwgz OR kubernetes_pod_name:menu-adapter-service-6fcb8bd966-4q4rh OR kubernetes_pod_name:outlet-service-67cdcb6c7f-kb4pt OR kubernetes_pod_name:pos-processor-service-8657d6b8dd-k8czm OR kubernetes_pod_name:tax-charge-service-666dd9875d-sjg5x OR kubernetes_pod_name:third-party-pos-service-6b5b77db7f-pglfx)'

    def formatted_csv_line(self, data, body=None):
        result = f"{body['@timestamp']},{body['kubernetes_pod_name']},{data['thread']}\n"
        return result

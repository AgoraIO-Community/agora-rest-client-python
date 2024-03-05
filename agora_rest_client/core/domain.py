import operator
import schedule
import socket
import threading
import time
from enum import Enum

# China domain
CHINA_MAINLAND_MAJOR_DOMAIN = 'sd-rtn.com'
# Oversea domain
OVERSEA_MAJOR_DOMAIN = 'agora.io'

# Asia & Pacific
AP_NORTHEAST_ENDPOINT_REGION_DOMAIN_PREFIX = 'api-ap-northeast-1'
AP_SOUTHEAST_ENDPOINT_REGION_DOMAIN_PREFIX = 'api-ap-southeast-1'

# China
CN_EAST_ENDPOINT_REGION_DOMAIN_PREFIX = 'api-cn-east-1'
CN_NORTH_ENDPOINT_REGION_DOMAIN_PREFIX = 'api-cn-north-1'

# European Union
EU_CENTRAL_ENDPOINT_REGION_DOMAIN_PREFIX = 'api-eu-central-1'
EU_WEST_ENDPOINT_REGION_DOMAIN_PREFIX = 'api-eu-west-1'

# United States
US_EAST_ENDPOINT_REGION_DOMAIN_PREFIX = 'api-us-east-1'
US_WEST_ENDPOINT_REGION_DOMAIN_PREFIX = 'api-us-west-1'

# Endpoint region
class EndpointRegion(Enum):
    # United States
    US = 0
    # European Union
    EU = 1
    # Asia & Pacific
    AP = 2
    # China
    CN = 3

# Service region
class ServiceRegion(Enum):
    # North America
    NA = 'na'
    # European Union
    EU = 'eu'
    # Asia & Pacific
    AP = 'ap'
    # China
    CN = 'cn'

# Region domain
ENDPOINT_REGION_DOMAIN = {
    EndpointRegion.US.value: {
        'prefixes': [US_WEST_ENDPOINT_REGION_DOMAIN_PREFIX, US_EAST_ENDPOINT_REGION_DOMAIN_PREFIX],
        'suffixes': [OVERSEA_MAJOR_DOMAIN, CHINA_MAINLAND_MAJOR_DOMAIN],
    },
    EndpointRegion.EU.value: {
        'prefixes': [EU_WEST_ENDPOINT_REGION_DOMAIN_PREFIX, EU_CENTRAL_ENDPOINT_REGION_DOMAIN_PREFIX],
        'suffixes': [OVERSEA_MAJOR_DOMAIN, CHINA_MAINLAND_MAJOR_DOMAIN],
    },
    EndpointRegion.AP.value: {
        'prefixes': [AP_SOUTHEAST_ENDPOINT_REGION_DOMAIN_PREFIX, AP_NORTHEAST_ENDPOINT_REGION_DOMAIN_PREFIX],
        'suffixes': [OVERSEA_MAJOR_DOMAIN, CHINA_MAINLAND_MAJOR_DOMAIN],
    },
    EndpointRegion.CN.value: {
        'prefixes': [CN_EAST_ENDPOINT_REGION_DOMAIN_PREFIX, CN_NORTH_ENDPOINT_REGION_DOMAIN_PREFIX],
        'suffixes': [CHINA_MAINLAND_MAJOR_DOMAIN, OVERSEA_MAJOR_DOMAIN],
    },
}

# Select best domain, interval seconds
SELECT_BEST_DOMAIN_INTERVAL_SECONDS = 30

class Domain(object):
    """
    Domain class
    """

    def __init__(self, endpoint_region, service_region=None):
        """
        :type endpoint_region: int
        :param endpoint_region: endpoint region
        :value endpoint_region: enum of `agora_rest_client.core.domain.EndpointRegion`

        :type service_region: str
        :param service_region: service region
        :value service_region: enum of `agora_rest_client.core.domain.ServiceRegion`
        """
        self._domain_list = []
        self._domain_list_running = []
        self._endpoint_region = endpoint_region
        self._logger = None
        self._service_region = service_region

    def get_domain_list(self):
        return self._domain_list

    def get_endpoint_region(self):
        return self._endpoint_region

    def get_service_region(self):
        return self._service_region

    def job_select_best_domain(self):
        """
        Scheduled job, select best domain
        """
        schedule.every(SELECT_BEST_DOMAIN_INTERVAL_SECONDS).seconds.do(self.select_best_domain)
        while True:
            schedule.run_pending()
            time.sleep(1)

    def resolve_domain(self, host, host_suffix):
        """
        Resolve domain

        :type host: str
        :param host: domain

        :type host_suffix: str
        :param host_suffix: domain suffix

        :return: ip address or None
        """
        try:
            time_start = time.time()
            ip_address = socket.gethostbyname(host)
            duration_ms = (time.time()-time_start)*1000

            self._domain_list_running.append({'host': host, 'host_suffix': host_suffix, 'duration_ms': duration_ms})
            self._logger.debug('resolve domain, host:%s, duration:%0.2fms, ip_address:%s', host, duration_ms, ip_address)

            return ip_address
        except Exception as e:
            self._logger.error('resolve domain failed:%s', e)
            return None

    def run(self, logger):
        """
        Run

        :type logger: object
        :param logger: logger
        """
        # Avoid duplicate run
        if self._logger is not None:
            return

        self.set_logger(logger)
        self.select_best_domain()

        # Start scheduled job
        t = threading.Thread(target=self.job_select_best_domain, args=())
        t.start()

    def select_best_domain(self):
        """
        Select best domain
        """
        threads = []
        self._domain_list_running = []
        self._logger.debug('select best domain start, endpoint_region:%s, domain_list:%s, domain_list_running:%s', self._endpoint_region, self._domain_list, self._domain_list_running)

        for suffix in ENDPOINT_REGION_DOMAIN[self._endpoint_region]['suffixes']:
            host = '%s.%s' % (ENDPOINT_REGION_DOMAIN[self._endpoint_region]['prefixes'][0], suffix)
            t = threading.Thread(target=self.resolve_domain, args=(host, suffix))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        # Check domain
        if len(self._domain_list_running) == 0:
            self._logger.error('select best domain failed, no available domain, endpoint_region:%s, domain_list:%s, domain_list_running:%s', self._endpoint_region, self._domain_list, self._domain_list_running)
            return

        # Sort by duration_ms
        domain_list_running = sorted(self._domain_list_running, key=operator.itemgetter('duration_ms'))
        domain_list = []

        for prefix in ENDPOINT_REGION_DOMAIN[self._endpoint_region]['prefixes']:
            domain_list.append('%s.%s' % (prefix, domain_list_running[0]['host_suffix']))

        self._domain_list = domain_list
        self._logger.debug('select best domain end, region:%s, domain_list:%s, domain_list_running:%s', self._endpoint_region, self._domain_list, self._domain_list_running)

    def set_logger(self, logger):
        self._logger = logger

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
AP_NORTHEAST_REGION_DOMAIN_PREFIX = 'api-ap-northeast-1'
AP_SOUTHEAST_REGION_DOMAIN_PREFIX = 'api-ap-southeast-1'

# China
CN_EAST_REGION_DOMAIN_PREFIX = 'api-cn-east-1'
CN_NORTH_REGION_DOMAIN_PREFIX = 'api-cn-north-1'

# European Union
EU_CENTRAL_REGION_DOMAIN_PREFIX = 'api-eu-central-1'
EU_WEST_REGION_DOMAIN_PREFIX = 'api-eu-west-1'

# United States
US_EAST_REGION_DOMAIN_PREFIX = 'api-us-east-1'
US_WEST_REGION_DOMAIN_PREFIX = 'api-us-west-1'

# Region area
class RegionArea(Enum):
    US = 0
    EU = 1
    AP = 2
    CN = 3

# Region domain
REGION_DOMAIN = {
    RegionArea.US.value: [
        '%s.%s' % (US_WEST_REGION_DOMAIN_PREFIX, OVERSEA_MAJOR_DOMAIN),
        '%s.%s' % (US_EAST_REGION_DOMAIN_PREFIX, OVERSEA_MAJOR_DOMAIN),
        '%s.%s' % (US_WEST_REGION_DOMAIN_PREFIX, CHINA_MAINLAND_MAJOR_DOMAIN),
        '%s.%s' % (US_EAST_REGION_DOMAIN_PREFIX, CHINA_MAINLAND_MAJOR_DOMAIN),
    ],
    RegionArea.EU.value: [
        '%s.%s' % (EU_WEST_REGION_DOMAIN_PREFIX, OVERSEA_MAJOR_DOMAIN),
        '%s.%s' % (EU_CENTRAL_REGION_DOMAIN_PREFIX, OVERSEA_MAJOR_DOMAIN),
        '%s.%s' % (EU_WEST_REGION_DOMAIN_PREFIX, CHINA_MAINLAND_MAJOR_DOMAIN),
        '%s.%s' % (EU_CENTRAL_REGION_DOMAIN_PREFIX, CHINA_MAINLAND_MAJOR_DOMAIN),
    ],
    RegionArea.AP.value: [
        '%s.%s' % (AP_SOUTHEAST_REGION_DOMAIN_PREFIX, OVERSEA_MAJOR_DOMAIN),
        '%s.%s' % (AP_NORTHEAST_REGION_DOMAIN_PREFIX, OVERSEA_MAJOR_DOMAIN),
        '%s.%s' % (AP_SOUTHEAST_REGION_DOMAIN_PREFIX, CHINA_MAINLAND_MAJOR_DOMAIN),
        '%s.%s' % (AP_NORTHEAST_REGION_DOMAIN_PREFIX, CHINA_MAINLAND_MAJOR_DOMAIN),
    ],
    RegionArea.CN.value: [
        '%s.%s' % (CN_EAST_REGION_DOMAIN_PREFIX, CHINA_MAINLAND_MAJOR_DOMAIN),
        '%s.%s' % (CN_NORTH_REGION_DOMAIN_PREFIX, CHINA_MAINLAND_MAJOR_DOMAIN),
        '%s.%s' % (CN_EAST_REGION_DOMAIN_PREFIX, OVERSEA_MAJOR_DOMAIN),
        '%s.%s' % (CN_NORTH_REGION_DOMAIN_PREFIX, OVERSEA_MAJOR_DOMAIN),
    ],
}

# Select best domain, interval seconds
SELECT_BEST_DOMAIN_INTERVAL_SECONDS = 30

class Domain(object):
    """
    Domain class
    """

    def __init__(self):
        self._domain_list = []
        self._domain_list_running = []
        self._logger = None
        self._region = None
        
    def get_domain_list(self):
        return self._domain_list

    def get_region(self):
        return self._region

    def job_select_best_domain(self):
        """
        Scheduled job, select best domain
        """
        schedule.every(SELECT_BEST_DOMAIN_INTERVAL_SECONDS).seconds.do(self.select_best_domain)
        while True:
            schedule.run_pending()
            time.sleep(1)

    def resolve_domain(self, host):
        """
        Resolve domain

        :param host: domain
        :return: ip address or None
        """
        try:
            time_start = time.time()
            ip_address = socket.gethostbyname(host)
            duration_ms = (time.time()-time_start)*1000

            self._domain_list_running.append({'host': host, 'duration_ms': duration_ms})
            self._logger.debug('resolve domain, host:%s, duration:%0.2fms, ip_address:%s', host, duration_ms, ip_address)

            return ip_address
        except Exception as e:
            self._logger.error('resolve domain failed:%s', e)
            return None

    def run(self, logger):
        """
        Run
        
        :param logger: logger
        """
        # Avoid duplicate run
        if self._logger is not None:
            return
        
        self._logger = logger
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
        self._logger.debug('select best domain start, region:%s, domain_list:%s, domain_list_running:%s', self._region, self._domain_list, self._domain_list_running)

        for host in REGION_DOMAIN[self._region]:
            t = threading.Thread(target=self.resolve_domain, args=(host,))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        # Sort by duration_ms
        self._domain_list = sorted(self._domain_list_running, key=operator.itemgetter('duration_ms'))
        self._logger.debug('select best domain end, region:%s, domain_list:%s, domain_list_running:%s', self._region, self._domain_list, self._domain_list_running)

    def set_logger(self, logger):
        self._logger = logger

    def set_region(self, region):
        self._region = region

# Default domain
default_domain = Domain()
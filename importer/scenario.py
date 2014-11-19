__author__ = 'soroosh'
import urllib

urllib.urlencode({'aa': 'aaa'})


class ScenarioGenerator(object):
    request_template = '{"%s","%s"}'
    request_batch_template = 'http.request.batch({%s})'
    template = '''http.request_batch({
            {"GET", "http://test.loadimpact.com"},
            {"GET", "http://test.loadimpact.com/news.php"}
        })
        client.sleep(15)
        http.request_batch({
            {"GET", "http://test.loadimpact.com/flip_coin.php"},
            {"GET", "http://test.loadimpact.com/news.php?bet=tails"}
        })
        '''


    def __init__(self, jmx_info):
        self.jmx_info = jmx_info


    def generate_scenario(self):
        script = ''
        requests = []
        if len(self.jmx_info.urls) == 0:
            raise Exception("At least 1 url is required for generating scenario")
        for jmxurl in self.jmx_info.urls:
            url = jmxurl.url
            if len(jmxurl.parameters) > 0:
                url = url + '?' + urllib.urlencode(jmxurl.parameters)
            request = ScenarioGenerator.request_template % (jmxurl.method, url)
            requests.append(request)
        script = ScenarioGenerator.request_template
        script = script % (','.join(requests))

        return script




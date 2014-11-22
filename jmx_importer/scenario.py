import loadimpact
import settings

__author__ = 'soroosh'
import urllib

__all__ = ['ScenarioGenerator', 'ScenarioUploader']


class ScenarioGenerator(object):
    get_request_temple = '{"%s","%s"}'
    post_request_template = '{"%s","%s",nil,{},"%s"}'
    request_batch_template = 'http.request_batch({%s})'

    def __init__(self, jmx_info):
        self.jmx_info = jmx_info


    def generate_scenario(self):
        requests = []
        if len(self.jmx_info.urls) == 0:
            raise Exception("At least 1 url is required for generating scenario")
        for jmxurl in self.jmx_info.urls:
            url = jmxurl.url
            encoded_params = ""
            if len(jmxurl.parameters) > 0:
                encoded_params = urllib.urlencode(jmxurl.parameters)
            if jmxurl.method == 'GET':
                request = ScenarioGenerator.post_request_template % (jmxurl.method, self.jmx_info.domain + url + '?' + encoded_params)
            else:
                request = ScenarioGenerator.post_request_template % (jmxurl.method, self.jmx_info.domain + url, encoded_params)
            requests.append(request)
        script = ScenarioGenerator.request_batch_template
        script %= ','.join(requests)
        return script


class ScenarioUploader(object):
    client = loadimpact.ApiTokenClient(api_token=settings.loadimpact_api_token)

    @staticmethod
    def upload(name, script):
        scenario = ScenarioUploader.client.create_user_scenario({'name': name, 'load_script': script})
        return scenario




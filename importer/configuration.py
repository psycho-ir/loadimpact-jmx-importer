__author__ = 'SOROOSH'
import loadimpact
import settings

__all__ = ['ConfigurationGenerator', 'ConfigurationUploader']

class ConfigurationGenerator(object):
    def __init__(self, jmx_info):
        self.jmx_info = jmx_info

    def generate_configuration(self, scenario):
        config = {'name': self.jmx_info.test_name,
                  'url': 'http://' + self.jmx_info.domain,
                  'config': {
                      'load_schedule': [
                          {'users': self.jmx_info.num_of_threads, 'duration': self.jmx_info.ramp_time / 60}],
                      'tracks': [{
                                     'clips': [{
                                                   'user_scenario_id': scenario.id, 'percent': 100
                                               }],
                                     'loadzone': settings.TIME_ZONE
                                 }],
                      'user_type': 'sbu'
                  }
        }

        return config


class ConfigurationUploader(object):
    client = loadimpact.ApiTokenClient(api_token=settings.loadimpact_api_token)

    @staticmethod
    def upload(data):
        config = ConfigurationUploader.client.create_test_config(data)
        return config



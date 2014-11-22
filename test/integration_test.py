from jmx_importer import SimpleAPI
import settings

__author__ = 'soroosh'

import unittest
from jmx_importer.jmx_reader import JMXReader
from jmx_importer.scenario import *
from jmx_importer.configuration import *
import loadimpact.clients


class IntegrationTest(unittest.TestCase):
    def setUp(self):
        print "Cleaning..."
        client = loadimpact.ApiTokenClient(api_token=settings.loadimpact_api_token)
        configs = client.list_test_configs()
        map(lambda config: config.delete(), configs)
        scenarios = client.list_user_scenarios()
        for scenario in scenarios:
            scenario.delete()


class ScenarioIntegrationTest(IntegrationTest):
    def test_scenario_creation(self):
        reader = JMXReader('../plans/Jmetertestplan.jmx')
        jmx_info = reader.create_jmx_info()
        print jmx_info
        generator = ScenarioGenerator(jmx_info)
        script = generator.generate_scenario()
        scenario = ScenarioUploader.upload('test3', script)
        print scenario


class ConfigurationIntegrationTest(IntegrationTest):
    def test_configuration_creation(self):
        reader = JMXReader('../plans/Jmetertestplan.jmx')
        jmx_info = reader.create_jmx_info()
        print jmx_info
        generator = ScenarioGenerator(jmx_info)
        script = generator.generate_scenario()
        scenario = ScenarioUploader.upload('test3', script)
        config_generator = ConfigurationGenerator(jmx_info)
        data = config_generator.generate_configuration(scenario)
        print 'Generate data is: %s' % data
        config = ConfigurationUploader.upload(data)
        print config


class SimpleAPITest(IntegrationTest):
    def test_simpleapi_with_one_jmx(self):
        api = SimpleAPI()
        paths = ['../plans/Jmetertestplan.jmx', '../plans/Jmetertestplan.jmx']
        failed_result = api.upload_jmx_files(paths)
        self.assertEqual(0, len(failed_result))

    def test_upload_should_return_one_failed_path(self):
        api = SimpleAPI()
        paths = ['..', '../plans/Jmetertestplan.jmx']
        failed_result = api.upload_jmx_files(paths)
        self.assertEqual(1, len(failed_result))

    def test_upload_should_return_one_failed_when_is_fail_fast_with_more_than_one_error(self):
        api = SimpleAPI()
        paths = ['..', '../plans/Jmetertestplan.jmx', '/', '...']
        failed_result = api.upload_jmx_files(paths)
        self.assertEqual(1, len(failed_result))

    def test_upload_should_return_all_failed_paths_when_is_not_fail_fast(self):
        api = SimpleAPI()
        paths = ['..', '../plans/Jmetertestplan.jmx', '/', '...']
        failed_result = api.upload_jmx_files(paths, fail_fast=False)
        self.assertEqual(3, len(failed_result))

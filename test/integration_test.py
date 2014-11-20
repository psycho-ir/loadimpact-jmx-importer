import settings

__author__ = 'soroosh'

import unittest
from importer.jmx_reader import JMXReader
from importer.scenario import *
from importer.configuration import *
import loadimpact.clients



class ScenarioIntegrationTest(unittest.TestCase):
    def setUp(self):
        client = loadimpact.ApiTokenClient(api_token=settings.loadimpact_api_token)
        configs = client.list_test_configs()
        map(lambda config: config.delete(), configs)
        scenarios = client.list_user_scenarios()
        scenario = filter(lambda s: s.name == 'test3', scenarios)
        if scenario:
            scenario[0].delete()

    def test_scenario_creation(self):
        reader = JMXReader('../plans/Jmetertestplan.jmx')
        jmx_info = reader.create_jmx_info()
        print jmx_info
        generator = ScenarioGenerator(jmx_info)
        script = generator.generate_scenario()
        scenario = ScenarioUploader.upload('test3', script)
        print scenario

    def test_configuration_creation(self):
        reader = JMXReader('../plans/Jmetertestplan.jmx')
        jmx_info = reader.create_jmx_info()
        print jmx_info
        generator = ScenarioGenerator(jmx_info)
        script = generator.generate_scenario()
        scenario = ScenarioUploader.upload('test3', script)
        config_generator = ConfigurationGenerator(jmx_info)
        data = config_generator.generate_configuration(scenario)
        print 'Generate dats is: %s' % data
        config = ConfigurationUploader.upload(data)
        print config
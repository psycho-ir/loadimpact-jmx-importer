import settings

__author__ = 'soroosh'

import unittest
from importer.jmx_reader import JMXReader
from importer.scenario import *
import loadimpact.clients



class ScenarioIntegrationTest(unittest.TestCase):
    def setUp(self):
        client = loadimpact.ApiTokenClient(api_token=settings.loadimpact_api_token)
        scenarios = client.list_user_scenarios()
        scenario = filter(lambda s: s._fields['name'].value == 'test3', scenarios)
        if scenario:
            scenario[0].delete()

    def test_scenario_creation(self):
        reader = JMXReader('../plans/Jmetertestplan.jmx')
        jmx_info = reader.create_jmx_info()
        print jmx_info
        generator = ScenarioGenerator(jmx_info)
        script = generator.generate_scenario()
        uploader = ScenarioUploader.upload('test3', script)
        print uploader

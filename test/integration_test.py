__author__ = 'soroosh'

import unittest
from importer.jmx_reader import JMXReader
from importer.scenario import *



class ScenarioIntegrationTest(unittest.TestCase):
    def test_scenario_creation(self):
        reader = JMXReader('../plans/Jmetertestplan.jmx')
        jmx_info = reader.create_jmx_info()
        print jmx_info
        generator = ScenarioGenerator(jmx_info)
        script = generator.generate_scenario()
        uploader = ScenarioUploader.upload('test1',script)
        print uploader

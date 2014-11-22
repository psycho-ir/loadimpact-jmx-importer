__author__ = 'soroosh'
from jmx_reader import JMXReader
from configuration import *
from scenario import *

__all__ = ['SimpleAPI', 'ScenarioGenerator', 'ScenarioUploader', 'ConfigurationGenerator', 'ConfigurationUploader']


class SimpleAPI(object):
    def upload_jmx_files(self, file_paths, fail_fast=True):
        file_paths = set(file_paths)
        failed_paths = list()
        for file_path in file_paths:
            try:
                reader = JMXReader(file_path)
                jmx_info = reader.create_jmx_info()
                print 'JMX Information has been read. JMX Info: %s' % jmx_info
                generator = ScenarioGenerator(jmx_info)
                script = generator.generate_scenario()
                print 'Created script is: %s' % script
                scenario = ScenarioUploader.upload(jmx_info.test_name, script)
                print 'Scenario uploaded with id:%s' % scenario.id
                config_generator = ConfigurationGenerator(jmx_info)
                data = config_generator.generate_configuration(scenario)
                print 'Created configuration test is: %s' % data
                config = ConfigurationUploader.upload(data)
                print 'Test configuration uploaded with id:%s' % config.id
            except Exception as e:
                print "An error occured on uploading jmx file: %s, Error message: %s" % (file_path, e)
                failed_paths.append((file_path, e))
                if fail_fast:
                    return failed_paths

        return failed_paths



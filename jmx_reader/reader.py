__author__ = 'soroosh'
import os
import xml.etree.ElementTree as ET


class JMXUrl(object):
    def __init__(self, url, method, parameters={}):
        if not url:
            raise Exception("Url is not valid")
        if not method:
            raise Exception("Method is not valid")
        if not isinstance(parameters, dict):
            raise Exception("parameters should be dictionary")
        self.url = url
        self.method = method
        self.parameters = parameters

    def add_parameter(self, name, value):
        self.parameters[name] = value


class JMXInfo(object):
    def __init__(self, test_name, num_of_threads, ramp_time, domain, urls):
        self.test_name = test_name
        self.num_of_threads = num_of_threads
        self.ramp_time = ramp_time
        self.domain = domain
        self.urls = urls


class JMXReader(object):
    def __init__(self, xml_path):
        if xml_path:
            if not os.path.exists(xml_path):
                raise Exception("File path does not exist")
            self._path = xml_path
            with open(self._path, mode='r') as jmx_file:
                self._content = '\n'.join(jmx_file.readlines())
                self._root = ET.fromstring(self._content)
        else:
            raise Exception("xml_path cannot be None")

    def _find_domain(self):
        config_element = self._root.find('hashTree//ConfigTestElement')
        return config_element.find("stringProp/[@name='HTTPSampler.domain']").text

    def _find_test_name(self):
        plan = self._root.find('hashTree//TestPlan')
        return plan.attrib['testname']

    def create_jmx_info(self):
        # domain_name
        info = JMXInfo()




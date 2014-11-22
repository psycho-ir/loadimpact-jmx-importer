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
        self.method = method.upper()
        self.parameters = parameters

    def add_parameter(self, name, value):
        self.parameters[name] = value

    def __repr__(self):
        return '[url:%s, method:%s, parameters:%s]' % (self.url, self.method, self.parameters)

    def __str__(self):
        return '[url:%s, method:%s, parameters:%s]' % (self.url, self.method, self.parameters)

    def __unicode__(self):
        return '[url:%s, method:%s, parameters:%s]' % (self.url, self.method, self.parameters)


class JMXInfo(object):
    def __init__(self, test_name, num_of_threads, ramp_time, domain, urls):
        self.test_name = test_name
        self.num_of_threads = num_of_threads
        self.ramp_time = ramp_time
        self.domain = domain
        self.urls = urls

    def __str__(self):
        return '[test_name:%s, num_of_threads:%s, ramp_time=%s, domain:%s,urls:%s]' % (
            self.test_name,
            self.num_of_threads,
            self.ramp_time,
            self.domain,
            self.urls
        )


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

    def _find_ramp_time(self):
        return int(self._root.find("hashTree//ThreadGroup/stringProp/[@name='ThreadGroup.ramp_time']").text)

    def _find_num_of_threads(self):
        return int(self._root.find("hashTree//ThreadGroup/stringProp/[@name='ThreadGroup.num_threads']").text)

    def _find_urls(self):
        sampler_proxies = self._root.iter('HTTPSamplerProxy')
        urls = []
        for sampler in sampler_proxies:
            url = sampler.find("stringProp/[@name='HTTPSampler.path']").text
            method = sampler.find("stringProp/[@name='HTTPSampler.method']").text
            arguments = sampler.find("elementProp/collectionProp/[@name='Arguments.arguments']")
            parameters = {}
            for argument in arguments.iter('elementProp'):
                name = argument.find("stringProp/[@name='Argument.name']").text
                value = argument.find("stringProp/[@name='Argument.value']").text
                parameters[name] = value
            url = JMXUrl(url, method, parameters)
            urls.append(url)
        return urls

    def create_jmx_info(self):
        test_name = self._find_test_name()
        num_threads = self._find_num_of_threads()
        ramp_time = self._find_ramp_time()
        domain = self._find_domain()
        urls = self._find_urls()

        info = JMXInfo(test_name, num_threads, ramp_time, domain, urls)
        return info




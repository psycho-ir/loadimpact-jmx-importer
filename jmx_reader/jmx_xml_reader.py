__author__ = 'soroosh'
# from lxml import etree
import xml.etree.ElementTree as ET

root = ET.fromstring('\n'.join(open('../plans/Jmetertestplan.xml', mode='r').readlines()))

print "Reading File  %s" % 'file_name.jmx'
print root.tag
print root.attrib

plans = root.iter('TestPlan')
thread_groups = root.iter('ThreadGroup')
sampler_proxies = root.iter('HTTPSamplerProxy')
config_element = root.find('hashTree//ConfigTestElement')

test_plan = {'urls': []}

domain = config_element.find("stringProp/[@name='HTTPSampler.domain']").text
test_plan['domain'] = domain

for plan in plans:
    print plan.tag, plan.attrib
    test_plan['testname'] = plan.attrib['testname']
else:
    print 'These is no test plan'

for thread_group in thread_groups:
    print thread_group.tag, thread_group.attrib
    num_of_threads = thread_group.find("stringProp/[@name='ThreadGroup.num_threads']").text
    ramp_time = thread_group.find("stringProp/[@name='ThreadGroup.ramp_time']").text
    test_plan['num_of_threads'] = num_of_threads
    test_plan['ramp_time'] = ramp_time

for sampler in sampler_proxies:
    url = sampler.find("stringProp/[@name='HTTPSampler.path']").text
    method = sampler.find("stringProp/[@name='HTTPSampler.method']").text
    test_plan['urls'].append((url, method,))

print test_plan




# for child in root:
# if child.tag == 'hashTree':
# for plan in child:
# print plan.tag, plan.attrib
# print child.tag, child.attrib



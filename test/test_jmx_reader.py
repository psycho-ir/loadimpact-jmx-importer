from jmx_reader.reader import JMXReader, JMXUrl

__author__ = 'soroosh'
import unittest


class TestJMXUul(unittest.TestCase):
    def test_jmxurl_should_throw_exception_when_url_is_None(self):
        self.assertRaises(Exception, JMXUrl, None, 'get', {})

    def test_jmxurl_should_throw_exception_when_method_is_None(self):
        self.assertRaises(Exception, JMXUrl, 'url', None, {})

    def test_jmxurl_should_throw_exception_when_parameters_is_None(self):
        self.assertRaises(Exception, JMXUrl, 'url', 'get', None)

    def test_add_parameter_should_add_new_parameter(self):
        url = JMXUrl('url', 'method')
        url.add_parameter('name1', 'value1')
        self.assertIn('name1', url.parameters)
        self.assertEqual(url.parameters['name1'], 'value1')


class TestReader(unittest.TestCase):
    def setUp(self):
        self.reader = JMXReader('../plans/Jmetertestplan.jmx')
        self.actual_domain = 'test.loadimpact.com'

    def test_jmx_reader_should_throw_exception_when_file_is_None(self):
        self.assertRaises(Exception, JMXReader, None)

    def test_jmx_reader_show_throw_exception_when_file_does_not_exist(self):
        self.assertRaises(Exception, JMXReader, 'fake_address')

    def test_jmx_reader_should_set_content_and_root_when_file_exist(self):
        reader = JMXReader('../plans/Jmetertestplan.jmx')
        self.assertIsNotNone(reader._content)
        self.assertIsNotNone(reader._root)

    def test_find_domain(self):
        domain = self.reader._find_domain()
        self.assertEqual(domain, self.actual_domain)

    def test_find_test_name(self):
        test_name = self.reader._find_test_name()
        self.assertEqual(test_name, 'My test plan')

    def test_find_ramp_time(self):
        ramp_time = self.reader._find_ramp_time()
        self.assertEqual(ramp_time, 60)

    def test_find_num_of_threads(self):
        num = self.reader._find_num_of_threads()
        self.assertEqual(num, 50)

    def test_find_urls(self):
        urls = self.reader._find_urls()
        self.assertEqual(len(urls), 5)

    def test_find_urls_last_one_should_have_one_query_parameter(self):
        urls = self.reader._find_urls()
        self.assertEqual(len(urls[-1].parameters), 2)

    def test_create_jmx_info(self):
        jmx_info = self.reader.create_jmx_info()
        self.assertEqual(jmx_info.domain, self.actual_domain)


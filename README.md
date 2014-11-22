loadimpact-jmx-importer
=======================

This project is an easy to use API for converting your Jmeter JMX files to a compatible scenario and configuration for http://loadimpact.com platform.


HOW TO USE
==========

1. First you need to set your API Token in settings.py
2. Select an appropriate TIME_ZONE and USER_TYPE and set them in settings.py
3. import jmx_importer
4. pass jmx file paths to upload_jmx_files method as a list.

import jmx_importer

api = jmx_importer.SimpleAPI()
failed_results = api.upload_jmx_files(['path_to_jmx1','path_to_jmx2'])

map(lambda failed_result: print 'File: %s, Error is:%s' % failed_result ,failed_results)


Note: The result of upload_jmx_files is a list of tuples which contains failed jmx path and its error.
Note: You can pass boolean value for fail_fast parameter. If fail_fast is True then uploading will stop on first failure.

Also you could use jmx_importer to upload just scenario or create just test configuration. For more information please check the tests.





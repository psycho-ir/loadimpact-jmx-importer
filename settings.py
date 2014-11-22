__author__ = 'soroosh'
import os
from loadimpact import LoadZone

loadimpact_api_token = os.environ.get('LOADIMPACT_API_TOKEN', '2e418df2845878f46c9c2189ba93b1164c66a51e4f071fbe98325be0a45980b9')
TIME_ZONE = LoadZone.AMAZON_US_PORTLAND
USER_TYPE = 'sbu'

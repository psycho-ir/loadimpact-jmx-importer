__author__ = 'soroosh'
import settings
import loadimpact

client = loadimpact.ApiTokenClient(api_token=settings.loadimpact_api_token)

print "Reading test configs..."
test_configs = client.list_test_configs()
if len(test_configs) == 0:
    print "You have no test configs"
else:
    print test_configs


# number_of_test_plans = 1
# number_of_vus = 3
# ramp_up_time = 100
# urls = ['http://google.com', 'http://khabar-chin.com']

config = client.create_test_config({'name': 'Created by API',
                                    'url': 'http://test.loadimpact.com',
                                    'config': {
                                        "load_schedule": [{"users": 50, "duration": 1}],
                                        "tracks": [{
                                                       "clips": [{
                                                                     "user_scenario_id": 1912896, "percent": 100
                                                                 }],
                                                       "loadzone": settings.TIME_ZONE
                                                   }],
                                        'user_type': 'sbu',
                                    }})





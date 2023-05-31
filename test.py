import argparse
import unittest
import requests

class ServiceTest(unittest.TestCase):
    url=None
    def setUp(self) -> None:
        pass
    def test_protocol_service(self):
        '''protocol service avialability'''
        service_url=self.url+'?protocol_url=https://mosff.ru/match/34549'
        r=requests.get(service_url)
        self.assertTrue(r.ok,'something bad with protocol service')
    def test_player_service(self):
        '''protocol service avialability'''
        service_url=self.url+'?player_url=https://mosff.ru/player/2050'
        r=requests.get(service_url)
        self.assertTrue(r.ok,'something bad with player service')
    def test_team_service(self):
        '''protocol service avialability'''
        service_url=self.url+'?team_url=https://mosff.ru/team/2051'
        r=requests.get(service_url)
        self.assertTrue(r.ok,'something bad with team service')


        
if __name__ == '__main__':

    parser = argparse.ArgumentParser(
                        prog='Web function tester',
                        description='Tests web function with https requests',
                        epilog='python -m test function_url')

    parser.add_argument('cloud_url')           # positional argument

    args = parser.parse_args()
    ServiceTest.url=args.cloud_url
    

    suite = unittest.defaultTestLoader.loadTestsFromTestCase(ServiceTest)
    unittest.TextTestRunner().run(suite)




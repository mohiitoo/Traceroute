import unittest
import traceroute       

class tracerouteTest(unittest.TestCase):
    def test_run(self):
        a =['traceroute to www.w3schools.com (192.229.133.221), 10 hops max, 60 byte packets',
         ' 1  _gateway (192.168.235.2)  2.360 ms  2.198 ms  2.053 ms', ' 2  * * *', ' 3  * * *',
         ' 4  * * *', ' 5  * * *', ' 6  * * *', ' 7  * * *', ' 8  * * *', ' 9  * * *', '10  * * *',
         ''] 
        self.assertEqual(traceroute.traceroute.run(self)('www.w3schools.com'), a )

if __name__ == '__main__':
    unittest.main()

# run ===> python -m unittest test_traceroute
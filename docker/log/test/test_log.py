
import unittest
from log import log

class TestLog(unittest.TestCase):

    def test_log_SysLog_build_log(self):

        lf = log.Syslog()
        un_log = lf.build_log("Nov 26 00:08:08 Air-de-Serge syslogd[63]: ASL Sender Statistics")
        exp = "Nov 26"
        result = un_log.date
        self.assertEquals(exp, result)

    def test_log_SysLog_fetch_log(self):
        lf = log.Syslog()
        lf.setBehavior("text")
        db = lf.fetch_log()
        self.assertIsNotNone(db)

    def test_log_SysLog_fetch_log_2(self):
        lf = log.Syslog()
        lf.setBehavior("text")
        db = lf.fetch_log()
        exp = {
                "id": 1360031010,
                "logs": [
                    "Oct  3 10:12:04 vertchapeau dnscrypt-proxy[2437]: Wed Oct  3 10:12:04 2018 [INFO] Chosen certificate #1534574301 is valid from [2018-10-03] to [2018-10-04]",
                    "Oct  3 10:12:04 vertchapeau dnscrypt-proxy[2437]: Wed Oct  3 10:12:04 2018 [INFO] Server key fingerprint is DCA8:D3C8:9E5D:8A10:D925:CF1F:D8CE:8FE4:21FB:9574:6189:718D:A05F:7EBE:A7AB:DX6E",
                    "Oct  3 10:12:04 vertchapeau dnscrypt-proxy[2437]: Wed Oct  3 10:12:04 2018 [INFO] Chosen certificate #1534574301 is invalid"
                ]
              }
        result = db["2018-11-03"]
        self.assertEquals(exp, result)


    #def test_log_Factory_Raise(self):
        #lf = log_factory.LogFactory()
        #self.assertRaises(SystemExit, lf.create_log, "nolog")

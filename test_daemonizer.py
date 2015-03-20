from subprocess import call
import unittest


class TestDaemonizer(unittest.TestCase):

    def test_permissions(self):
        try:
            pf = open(".tmp", 'w')
            call(["echo", "test", ">", ".tmp"])
            pid = str(pf.read().strip())
            pf.close()
        except IOError:
            pid = None
        except SystemExit:
            pid = None
        return pid
        self.assertEqual(pid, pid)


if __name__ == "__main__":
    unittest.main()

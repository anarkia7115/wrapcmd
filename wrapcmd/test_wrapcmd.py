import unittest
from wrapcmd import wrapcmd

class TestCmdSession(unittest.TestCase):

    def test_dry_run(self):
        sess = wrapcmd.CmdSession()
        sess.dry_run = True
        out = sess.exec("ls /", get_output=True, default="112233")
        self.assertEqual(out, "112233")

    def test_ls(self):
        sess = wrapcmd.CmdSession()
        out = sess.exec("ls /", get_output=True)
        self.assertTrue(b"bin" in out)

if __name__ == "__main__":
    unittest.main()
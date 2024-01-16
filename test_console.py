import unittest
from io import StringIO
from contextlib import redirect_stdout
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()
        self.console.preloop()

    def test_quit(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('quit')
            self.assertEqual(fake_out.getvalue(), '')

    def test_EOF(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('EOF')
            self.assertEqual(fake_out.getvalue(), '')

    def test_create(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('create BaseModel')
            self.assertNotEqual(fake_out.getvalue(), '')

    def test_show(self):
        self.console.onecmd('create BaseModel')
        obj_id = fake_out.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd(f'show BaseModel.{obj_id}')
            self.assertNotEqual(fake_out.getvalue(), '** no instance found **')

    def test_destroy(self):
        self.console.onecmd('create BaseModel')
        obj_id = fake_out.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd(f'destroy BaseModel.{obj_id}')
            self.assertEqual(fake_out.getvalue(), '')

    def test_all(self):
        self.console.onecmd('create BaseModel')
        self.console.onecmd('create User')
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('all')
            output = fake_out.getvalue()
            self.assertIn('BaseModel', output)
            self.assertIn('User', output)

    def test_count(self):
        self.console.onecmd('create BaseModel')
        self.console.onecmd('create User')
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('count BaseModel')
            self.assertNotEqual(fake_out.getvalue(), '0')

    def test_update(self):
        self.console.onecmd('create BaseModel')
        obj_id = fake_out.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd(f'update BaseModel.{obj_id} name "test"')
            self.assertEqual(fake_out.getvalue(), '')

if __name__ == '__main__':
    unittest.main()

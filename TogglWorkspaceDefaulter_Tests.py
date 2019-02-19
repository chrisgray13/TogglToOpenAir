import unittest
from Mocks.MockTogglWorkspaceApiReader import MockTogglWorkspaceApiReader
from TogglWorkspaceDefaulter import TogglWorkspaceDefaulter


class TogglWorkspaceApiReader_Tests(unittest.TestCase):
    def test_get_with_1_workspace(self):
        self.assertEqual(TogglWorkspaceDefaulter(
            MockTogglWorkspaceApiReader([{"id": 123456}])).get(), 123456)

    def test_get_with_no_workspaces(self):
        with self.assertRaises(Exception):
            TogglWorkspaceDefaulter(MockTogglWorkspaceApiReader([])).get()

    def test_get_with_many_workspaces(self):
        with self.assertRaises(Exception):
            TogglWorkspaceDefaulter(
                MockTogglWorkspaceApiReader([{"id": 123456}, {"id": 234567}, {"id": 345678}])).get()

    def test_get_with_a_default(self):
        self.assertEqual(TogglWorkspaceDefaulter(
            MockTogglWorkspaceApiReader([{"id": 123456}]), 234567).get(), 234567)

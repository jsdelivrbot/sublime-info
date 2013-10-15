from unittest import TestCase
from sublime_info import sublime_info


"""
Sublime Text as subl
    resolved via `get_sublime_path`
        has a path of `/usr/bin/subl`

Sublime Text as sublime_text
    resolved via `get_sublime_path`
        has a path of `/usr/bin/sublime_text`

Sublime Text as sublime_texttt
    specified via SUBLIME_TEXT_PATH
        resolved via `get_sublime_path`
            has a path of `/usr/bin/sublime_texttt`

TODO: What about sublime_text.exe
TODO: What about sublime_text.app
"""


class TestRunFunction(TestCase):
    def test_run_exists(self):
        sublime_info.get_sublime_path()
        # self.assertTrue(sublime_info.run))

# -------------------------------------------------------------------------
#                     The CodeChecker Infrastructure
#   This file is distributed under the University of Illinois Open Source
#   License. See LICENSE.TXT for details.
# -------------------------------------------------------------------------

from codechecker_report_converter.analyzer_result import AnalyzerResult

from .output_parser import PyflakesParser
from ..plist_converter import PlistConverter


class PyflakesAnalyzerResult(AnalyzerResult):
    """ Transform analyzer result of Pyflakes. """

    TOOL_NAME = 'pyflakes'
    NAME = 'Pyflakes'
    URL = 'https://github.com/PyCQA/pyflakes'

    def parse(self, analyzer_result):
        """ Creates plist files from the given analyzer result to the given
        output directory.
        """
        parser = PyflakesParser(analyzer_result)

        content = self._get_analyzer_result_file_content(analyzer_result)
        if not content:
            return

        messages = parser.parse_messages(content)

        plist_converter = PlistConverter(self.TOOL_NAME)
        plist_converter.add_messages(messages)
        return plist_converter.get_plist_results()

from typing import Callable
import language_tool_python


class GrammarCheck:
    def __init__(
        self
    ):
        self.matches = {}
        self.tool = language_tool_python.LanguageTool('en-GB')
        self.content = ""

    def getErrors(self):
        return self.matches

    def getCorrection(self) -> str:
        return self.tool.correct(self.content)

    def setText(self, text: str):
        self.content = text

    def showMatches(self):
        index = 0
        for match in self.matches:
            index = index + 1
            print("Match: {}\n".format(index))
            print("Rule ID: {}\n".format(match.ruleId))
            print("Context: {}\n".format(match.context))
            print("Sentence: {}\n".format(match.sentence))
            print("Category: {}\n".format(match.category))
            print("Rule Issue Type: {}\n".format(match.ruleIssueType))
            print("Replacements: {}\n".format(match.replacements))
            print("Messages: {}\n".format(match.message))
            print("Offset: {}\n".format(match.offsetInContext))
            print("Offset in context: {}\n".format(match.offset))
            print("Error Length: {}\n".format(match.errorLength))

    def checkSection(self):
        if(self.content != ""):
            self.matches = self.tool.check(self.content)
        return self.matches
        # we will now have a set of matches and each of these relates to a section of text in the given text block.
        # We can return these as a collection of corrections
        # The calling program should ideally present these as a correction option when:
        # (a) Someone hovers over that section of text or
        # (b) As a panel of issues which can be corrected by clicking on the relevant issue

    def styler(error):
        html = error.context
        from_ = error.offsetInContext
        to_ = from_ + error.errorLength
        txt = html[from_:to_]
        html = html[:from_] + '<span style="color:red">' + \
            txt + "</span>" + html[to_:]
        print(f"**{html}")
        return html

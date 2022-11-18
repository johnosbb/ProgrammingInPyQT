import re

question = "the total number of staff in 30?"
find = ["total", "staff"]
words = re.findall("\w+", question)
result = [x for x in find if x in words]
print(result)


re_pattern = r'\b(?:total|staff)\b'
result = re.findall(re_pattern, question)
print(result)


pattern = r"^Cookie"
sequence = "Cookie Monster"
if re.match(pattern, sequence):
    print("Match! for " + pattern)
else:
    print("Not a match!")

    syntax = QRegExp.RegExp  # can be one of QRegExp.RegExp2, QRegExp.WildCard, QRegExp.RegExp2 etc, see https://doc.qt.io/qt-5/qregexp.html#PatternSyntax-enum
    caseSensitivity = Qt.CaseInsensitive

sequence = " Having a good day"
sequence = sequence.lstrip()


pattern = r"^Having"

if re.match(pattern, sequence):
    print("Match! for " + pattern)
else:
    print("Not a match for " + pattern)


pattern = '^Having'
# Note that the result raw string has the quote at the beginning and end of the string. To remove them, you can use slices: [1:-1]
rawPattern = repr(pattern)[1:-1]
if re.match(rawPattern, sequence):
    print("Match! for " + pattern)
else:
    print("Not a match for " + rawPattern + " or " + pattern)

from pygments.style import Style
from pygments.token import (
    Keyword,
    Name,
    Comment,
    Other,
    String,
    Error,
    Number,
    Operator,
    Literal,
    Text,
    Punctuation,
    Generic,
    Whitespace,
    Escape,
    Token,
)


class CustomShellStyle(Style):
    styles = {
        Comment: "italic",
    }

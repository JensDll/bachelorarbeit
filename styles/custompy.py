from pygments.style import Style
from pygments.token import Keyword, Name, Comment, Other, String, Error, \
     Number, Operator, Literal, Text, Punctuation, Generic, Whitespace, Escape, Token

FOREGROUND = "#191565"

class CustompyStyle(Style):
    default_style = ''
    styles = {
        Whitespace:         '#bbbbbb',
        Comment:            'italic #007ccf',
        Comment.Preproc:    'noitalic #009999',
        Comment.Special:    'bold',

        Keyword:            'bold #006699',
        Keyword.Pseudo:     'nobold',
        Keyword.Type:       '#007788',

        Operator:           '#555555',
        Operator.Word:      'bold #000000',

        Name.Builtin:       '#336666',
        Name.Function:      '#A116C4',
        Name.Class:         'bold #00AA88',
        Name.Exception:     'bold #CC0000',
        Name.Variable:      '#003333',
        Name.Constant:      '#336600',
        Name.Label:         '#9999FF',
        Name.Entity:        'bold #999999',
        Name.Attribute:     '#330099',
        Name.Tag:           'bold #330099',
        Name.Decorator:     '#9999FF',

        String:             '#CC3300',
        String.Doc:         'italic',
        String.Interpol:    '#AA0000',
        String.Escape:      'bold #CC3300',
        String.Regex:       '#33AAAA',
        String.Symbol:      '#FFCC33',
        String.Other:       '#CC3300',

        Number:             '#FF6600',

        Generic.Heading:    'bold #003300',
        Generic.Subheading: 'bold #003300',
        Generic.Deleted:    'border:#CC0000 bg:#FFCCCC',
        Generic.Inserted:   'border:#00CC00 bg:#CCFFCC',
        Generic.Error:      '#FF0000',
        Generic.Emph:       'italic',
        Generic.Strong:     'bold',
        Generic.Prompt:     'bold #000099',
        Generic.Output:     '#000000',
        Generic.Traceback:  '#99CC66',

        Text:               FOREGROUND,
        Punctuation:        FOREGROUND,
        Name:               FOREGROUND,

        Error:              'bg:#FFAAAA #AA0000'
    }
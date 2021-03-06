# -*- coding: utf-8 -*-
"""TODO: doc module"""


from enum import Enum


class HtmlTag(Enum):
    """Requirements: #35, #70"""

    TAG_DOCTYPE = '!DOCTYPE'
    TAG_COMMENT = '!--...--'

    TAG_HTML = 'html'
    TAG_HEAD = 'head'
    TAG_TITLE = 'title'
    TAG_BODY = 'body'
    TAG_H1 = 'h1'
    TAG_P = 'p'
    TAG_BR = 'br'
    TAG_HR = 'hr'
    TAG_ACRONYM = 'acronym'
    TAG_ABBR = 'abbr'
    TAG_ADDRESS = 'address'
    TAG_B = 'b'
    TAG_BDI = 'bdi'
    TAG_BDO = 'bdo'
    TAG_BIG = 'big'
    TAG_BLOCKQUOTE = 'blockquote'
    TAG_CENTER = 'center'
    TAG_CITE = 'cite'
    TAG_CODE = 'code'
    TAG_DEL = 'del'
    TAG_DFN = 'dfn'
    TAG_EM = 'em'
    TAG_FONT = 'font'
    TAG_I = 'i'
    TAG_INS = 'ins'
    TAG_KBD = 'kbd'
    TAG_MARK = 'mark'
    TAG_METER = 'meter'
    TAG_PRE = 'pre'
    TAG_PROGRESS = 'progress'
    TAG_Q = 'q'
    TAG_RP = 'rp'
    TAG_RT = 'rt'
    TAG_RUBY = 'ruby'
    TAG_S = 's'
    TAG_SAMP = 'samp'
    TAG_SMALL = 'small'
    TAG_STRIKE = 'strike'
    TAG_STRONG = 'strong'
    TAG_SUB = 'sub'
    TAG_SUP = 'sup'
    TAG_TIME = 'time'
    TAG_TT = 'tt'
    TAG_U = 'u'
    TAG_VAR = 'var'
    TAG_WBR = 'wbr'
    TAG_FORM = 'form'
    TAG_INPUT = 'input'
    TAG_TEXTAREA = 'textarea'
    TAG_BUTTON = 'button'
    TAG_SELECT = 'select'
    TAG_OPTGROUP = 'optgroup'
    TAG_OPTION = 'option'
    TAG_LABEL = 'label'
    TAG_FIELDSET = 'fieldset'
    TAG_LEGEND = 'legend'
    TAG_DATALIST = 'datalist'
    TAG_OUTPUT = 'output'
    TAG_FRAME = 'frame'
    TAG_FRAMESET = 'frameset'
    TAG_NOFRAMES = 'noframes'
    TAG_IFRAME = 'iframe'
    TAG_IMG = 'img'
    TAG_MAP = 'map'
    TAG_AREA = 'area'
    TAG_CANVAS = 'canvas'
    TAG_FIGCAPTION = 'figcaption'
    TAG_FIGURE = 'figure'
    TAG_PICTURE = 'picture'
    TAG_AUDIO = 'audio'
    TAG_SOURCE = 'source'
    TAG_TRACK = 'track'
    TAG_VIDEO = 'video'
    TAG_A = 'a'
    TAG_LINK = 'link'
    TAG_NAV = 'nav'
    TAG_UL = 'ul'
    TAG_OL = 'ol'
    TAG_LI = 'li'
    TAG_DIR = 'dir'
    TAG_DL = 'dl'
    TAG_DT = 'dt'
    TAG_DD = 'dd'
    TAG_MENU = 'menu'
    TAG_MENUITEM = 'menuitem'
    TAG_TABLE = 'table'
    TAG_CAPTION = 'caption'
    TAG_TH = 'th'
    TAG_TR = 'tr'
    TAG_TD = 'td'
    TAG_THEAD = 'thead'
    TAG_TBODY = 'tbody'
    TAG_TFOOT = 'tfoot'
    TAG_COL = 'col'
    TAG_COLGROUP = 'colgroup'
    TAG_STYLE = 'style'
    TAG_DIV = 'div'
    TAG_SPAN = 'span'
    TAG_HEADER = 'header'
    TAG_FOOTER = 'footer'
    TAG_MAIN = 'main'
    TAG_SECTION = 'section'
    TAG_ARTICLE = 'article'
    TAG_ASIDE = 'aside'
    TAG_DETAILS = 'details'
    TAG_DIALOG = 'dialog'
    TAG_SUMMARY = 'summary'
    TAG_DATA = 'data'
    TAG_META = 'meta'
    TAG_BASE = 'base'
    TAG_BASEFONT = 'basefont'
    TAG_SCRIPT = 'script'
    TAG_NOSCRIPT = 'noscript'
    TAG_APPLET = 'applet'
    TAG_EMBED = 'embed'
    TAG_OBJECT = 'object'
    TAG_PARAM = 'param'

    @classmethod
    def get_tags(cls):
        """Return enum values"""
        return [item.value for item in HtmlTag]

    @classmethod
    def has_tag(cls, value):
        """Returns True if enum have value"""
        return any(value == item.value for item in cls)

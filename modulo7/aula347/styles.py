# import qdarkstyle
from vars import (PRIMARY_COLOR, DARKER_PRIMARY_COLOR, DARKEST_PRIMARY_COLOR,
                  BACKGORUND_COLOR, DISPLAY_COLOR)

qss = f"""
    MainWindow[cssClass="body"]{{
        background-color: {BACKGORUND_COLOR};
    }}
    Info[cssClass="info"]{{
        color: {DISPLAY_COLOR};
    }}
    Display[cssClass="display"]{{
        background-color: {DISPLAY_COLOR};
        border-color: {PRIMARY_COLOR};
        border-radius: 5px;
    }}
    Button[cssClass="specialButton"]{{
        color: #fff;
        background: {PRIMARY_COLOR};
        border-radius: 5px;
    }}
    Button[cssClass="specialButton"]:hover{{
        color: #fff;
        background: {DARKER_PRIMARY_COLOR};
        border-radius: 5px;
    }}
    Button[cssClass="specialButton"]:pressed{{
        color: #fff;
        background: {DARKEST_PRIMARY_COLOR};
        border-radius: 5px;
    }}
    Button[cssClass="normalButton"]{{
        color: #fff;
        background: {DARKEST_PRIMARY_COLOR};
        border-color: {DARKER_PRIMARY_COLOR};
        border-style: solid;
        border-width: 1px;
        border-radius: 5px;
    }}
    Button[cssClass="normalButton"]:hover{{
        color: #fff;
        background: {DARKER_PRIMARY_COLOR};
        border-radius: 5px;
    }}
    Button[cssClass="normalButton"]:pressed{{
        color: #fff;
        background: {PRIMARY_COLOR};
        border-color: {DARKER_PRIMARY_COLOR};
        border-style: solid;
        border-width: 1px;
        border-radius: 5px;
    }}
"""


def setTheme(app, window, display, info):
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())
    # app.setStyleSheet(app.styleSheet() + qss)
    app.setStyleSheet(qss)
    window.setProperty('cssClass', 'body')
    display.setProperty('cssClass', 'display')
    info.setProperty('cssClass', 'info')

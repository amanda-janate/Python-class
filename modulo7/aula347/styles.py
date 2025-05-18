import qdarkstyle
from vars import PRIMARY_COLOR, DARKER_PRIMARY_COLOR, DARKEST_PRIMARY_COLOR

qss = f"""
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
"""

def setTheme(app):
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())

    app.setStyleSheet(app.styleSheet() + qss)
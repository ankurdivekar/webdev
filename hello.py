from fasthtml.common import *

import adminpanel
import canvas
import dashboard
import landingpage
import sidebar
import table

app = FastHTML(
    hdrs=Link(rel="stylesheet", href="app.css", type="text/css"),
)
rt = app.route


@rt("/{fname:path}.{ext:static}")
def get(fname: str, ext: str):
    return FileResponse(f"public/{fname}.{ext}")


@rt("/")
def get():
    return Html("Hello World!")


@rt("/landing")
def get():
    return landingpage.content


@rt("/sidebar")
def get():
    # return landingpage.content
    return sidebar.content


@rt("/admin")
def get():
    return adminpanel.content


@rt("/canvas")
def get():
    return canvas.content


@rt("/dashboard")
def get():
    return dashboard.content


@rt("/table")
def get():
    return table.content


serve()

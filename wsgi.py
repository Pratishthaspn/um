from factory import create_app

# Vercel looks for a Flask instance named `app` at a supported entrypoint
# file (app.py, index.py, server.py, main.py, wsgi.py, or asgi.py) at the
# project root.
app = create_app()

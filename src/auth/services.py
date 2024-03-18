import functools

from flask import g, redirect, url_for


def get_current_user(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if not g.user:
            return redirect(url_for("auth.sign_in"))
        return view(**kwargs)
    return wrapped_view

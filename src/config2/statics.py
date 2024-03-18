import os
import pathlib

static = (
    str(
        pathlib.Path(__file__)
        .parent.resolve()
        .parent.resolve()
        # .parent.resolve()
    )
    + '/static/'
)

if not os.path.exists(static):
    os.mkdir(static)

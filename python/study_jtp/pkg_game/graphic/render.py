# render.py

# from pkg_game.sound.echo import echo_test # <- it's OK
from ..sound.echo import echo_test # <- it's also OK
# import ..sound.echo.echo_test  # <- it's also OK

def render_test():
    print ("render")
    echo_test()


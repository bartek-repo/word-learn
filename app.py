import layout
from layout import PARAMETERS

def push_event_dec(e):
    if e.keycode == PARAMETERS['bind-check-keycode']:
        global lay
        lay.bad_answear()

lay = layout.GameLayout(push_event_dec)

lay.display_layout()
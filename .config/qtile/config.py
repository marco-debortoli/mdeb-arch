

import enum
from typing import List

from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Screen
from libqtile.lazy import lazy

import os
import subprocess

from key_config import keys, MOD

# -- Colours and Font

FONT = "JetBrainsMono Nerd Font Mono"

class ColourTheme(enum.Enum):
    BACKGROUND = "#141D2B"
    LIGHT_TEXT = "#C5D1EB"
    DARK_TEXT = "#A4B1CD"
    RED = "#FF8484"
    TEAL = "#5CECC6"
    PURPLE = "#CF8DFB"
    YELLOW = "#FFCC5C"
    BLUE = "#5CB2FF"
    GREEN = "C5F467"

# -- Groups

numbered_groups = [
    ("", {"layout": "columns"}),
    ("", {"layout": "columns"}),
    ("", {"layout": "columns"}),
    ("", {"layout": "columns"}),
    ("", {"layout": "columns"}),
    ("", {"layout": "columns"})
]

groups = [
    Group(config[0], **config[1]) for config in numbered_groups
]

for i, group in enumerate(groups, 1):
    keys.extend([
        # Key to switch to group
        Key(
            [MOD], str(i), lazy.group[group.name].toscreen(), 
            desc=f"Switch to group {group.name}" 
        ),

        # Key to move a focused window to a group (but no follow)
        Key( 
            [MOD, "shift"], str(i), lazy.window.togroup(group.name), 
            desc=f"move focused window to group {group.name}"
        ) 
   ])

layout_theme = {
    "border_width": 4,
    "margin": [4, 4, 4, 4],
    "margin_on_single": [4, 4, 4, 4],
    "border_focus": ColourTheme.GREEN.value,
    "border_normal": ColourTheme.DARK_TEXT.value
}

layouts = [
    layout.Columns(**layout_theme, insert_position=1, num_columns=2)
]

# -- Widgets

def power_options():
    """
    Lock the computer using betterlockscreen
    """
    qtile.cmd_spawn("bash /home/marco/.config/scripts/power_options.sh")

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.Sep(
                    linewidth=0,
                    padding=24,
                    background=ColourTheme.BACKGROUND.value
                ),
                widget.Clock(
                    foreground=ColourTheme.LIGHT_TEXT.value,
                    background=ColourTheme.BACKGROUND.value,
                    format="%A %B %d %H:%M",
                    padding=0
                ),
                widget.Spacer(background=ColourTheme.BACKGROUND.value),
                widget.GroupBox(
                    background=ColourTheme.BACKGROUND.value,
                    active=ColourTheme.GREEN.value,
                    inactive=ColourTheme.DARK_TEXT.value,
                    disable_drag=True,
                    font=FONT,
                    fontsize=32,
                    padding=12,
                    highlight_color=[ColourTheme.BACKGROUND.value, ColourTheme.BACKGROUND.value],
                    highlight_method='line',
                    this_current_screen_border=ColourTheme.GREEN.value,
                    other_screen_border=ColourTheme.GREEN.value,
                    center_aligned=True,
                ),
                widget.Spacer(background=ColourTheme.BACKGROUND.value),
                widget.TextBox(
                    text="墳",
                    font=FONT,
                    fontsize=28,
                    foreground=ColourTheme.YELLOW.value,
                    background=ColourTheme.BACKGROUND.value,
                    padding=0
                ),
                widget.Sep(
                    linewidth=0, 
                    padding=4, 
                    background=ColourTheme.BACKGROUND.value
                ),
                widget.PulseVolume(
                    font=FONT,
                    foreground=ColourTheme.YELLOW.value,
                    background=ColourTheme.BACKGROUND.value,
                    update_interval=0.2
                ),
                widget.Sep(
                    linewidth=0,
                    padding=24,
                    background=ColourTheme.BACKGROUND.value
                ),
                widget.TextBox(
                    text="",
                    background=ColourTheme.BACKGROUND.value,
                    foreground=ColourTheme.RED.value,
                    font=FONT,
                    fontsize=28,
                    padding=0,
                    mouse_callbacks={
                        "Button1": power_options
                    }
                ),
                widget.Sep(
                    linewidth=0,
                    padding=24,
                    background=ColourTheme.BACKGROUND.value
                ),
            ],
            42,
            opacity=1,
            margin=[4,0,0,0],
            background=ColourTheme.BACKGROUND.value
        )
    )
]


# Drag floating layouts.
mouse = [
    Drag(
        [MOD], "Button1", lazy.window.set_position_floating(),
        start=lazy.window.get_position()
    ),
    Drag(
        [MOD], "Button3", lazy.window.set_size_floating(),
        start=lazy.window.get_size()
    ),
    Click([MOD], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules
    ]
)

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

auto_minimize = True

# -- Hooks

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser("~")
    subprocess.call([home + "/.config/qtile/autostart.sh"])


# Now sure what this is below
wmname = "LG3D"

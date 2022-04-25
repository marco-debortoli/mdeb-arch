from libqtile.config import Key
from libqtile.lazy import lazy

MOD = "mod4"
TERMINAL = "alacritty -e /usr/bin/fish"

keys = [

    # Switch between windows
    Key(
        [MOD], "Left", 
        lazy.layout.left(), 
        desc="Move focus to left"
    ),

    Key(
        [MOD], "Right", 
        lazy.layout.right(), 
        desc="Move focus to right" 
    ),
    
    Key(
        [MOD], "Down", 
        lazy.layout.down(), 
        desc="Move focus down" 
    ),

    Key(
        [MOD], "Up", 
        lazy.layout.up(), 
        desc="Move focus up"
    ),


    # Move windows between left/right columns or move up/down in current stack.
    Key( 
        [MOD, "shift"], "Left", 
        lazy.layout.shuffle_left(),
        desc="Move window to the left" 
    ),

    Key( 
        [MOD, "shift"], "Right", 
        lazy.layout.shuffle_right(),
        desc="Move window to the right"
    ),

    Key(
        [MOD, "shift"], "Down", 
        lazy.layout.shuffle_down(),
        desc="Move window down"
    ),

    Key(
        [MOD, "shift"], "Up", 
        lazy.layout.shuffle_up(), 
        desc="Move window up"
    ),



    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key(
        [MOD, "control"], "Left", 
        lazy.layout.grow_left(),
        desc="Grow window to the left"
    ),

    Key(
        [MOD, "control"], "Right", 
        lazy.layout.grow_right(),
        desc="Grow window to the right"
    ),
    
    Key(
        [MOD, "control"], "Down", 
        lazy.layout.grow_down(),
        desc="Grow window down"
    ),
    
    Key(
        [MOD, "control"], "Up", 
        lazy.layout.grow_up(), 
        desc="Grow window up"
    ),

    Key(
        [MOD], "n", 
        lazy.layout.normalize(), 
        desc="Reset all window sizes"
    ),

    Key(
        [MOD], "Return", 
        lazy.spawn(TERMINAL), 
        desc="Launch terminal"
    ),

    # Toggle between different layouts as defined below
    Key(
        [MOD], "Tab", 
        lazy.next_layout(), 
        desc="Toggle between layouts"
    ),

    Key(
        [MOD], "w", 
        lazy.window.kill(), 
        desc="Kill focused window"
    ),

    Key(
        [MOD, "control"], "r", 
        lazy.restart(), 
        desc="Restart Qtile"
    ),

    Key(
        [MOD, "control"], "q", 
        lazy.shutdown(), 
        desc="Shutdown Qtile"
    ),

    # Custom Controls

    Key(
        [MOD, "shift"], "4",
        lazy.spawn("import ~/Downloads/screenshot.png"),
        desc="Take a screenshot"
    ),

    Key(
        [MOD], "space", 
        lazy.spawn("rofi -show drun"),
        desc="Rofi spawn window"
    ),

    Key(
        [MOD, "shift"], "space",
        lazy.spawn("rofi -show run"),
        desc="Rofi show running windows"
    ),

    Key(
        [MOD, "shift"], "F1",
        lazy.spawn("betterlockscreen -l dim"),
        desc="Lock the screen"
    ),

    Key(
        [MOD, "shift"], "F2",
        lazy.spawn("systemctl suspend"),
        desc="Put the computer to sleep"
    )
]

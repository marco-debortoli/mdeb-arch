# MDEB Arch

This is my personal Arch Linux configuration built using Hyprland! Some screenshots and details can be found below.

![screenshot of terminal layout](https://raw.githubusercontent.com/marco-debortoli/mdeb-arch/main/screenshots/terminal.png)

![screenshot of rofi layout](https://raw.githubusercontent.com/marco-debortoli/mdeb-arch/main/screenshots/rofi.png)

![screenshot of wallpaper](https://raw.githubusercontent.com/marco-debortoli/mdeb-arch/main/screenshots/wallpaper.png)

## Install

Find below some of the installation instructions, which are tailored to my current Framework Laptop 13 (12th Gen Intel). You may need to make some adjustments if you have an NVIDIA GPU or use an AMD CPU.

Note that this install guide is primarily for my personal use - so that I don't remember how to install from scratch! At some point in time I may make this friendlier for other users.

### Packages

First you will want to install the packages below. Feel free to customize these to your device as needed.

Intel
- `intel-media-driver`
- `intel-gpu-tools`
- `intel-ucode`
- `mesa`

Terminal Emulator
- `alacritty`
- `fish`
- `btop`
- `vim`

Browser
- `firefox`

Hyprland (Wayland Window Manager)
- `hyprland-git`
- `waybar-hyprland-git`
- `pipewire`
- `wireplumber`
- `xdg-desktop-portal-hyprland`

Bluetooth, Brightness and Audio
- `light`
- `bluez`
- `bluez-utils`
- `blueman`
- `pavucontrol`

Power Management
- `power-profiles-daemon`
- `swaylock-effects`
- `swayidle`

SSH and Networking
- `net-tools`
- `openssh`

Wallpaper & Font
- `hyprpaper`
- `ttf-jetbrains-mono-nerd`
- `noto-fonts-emoji`

Application Launcher
- `rofi-lbonn-wayland-git`

Notifications
- `dunst`
- `libnotify`

Multimedia & Screenshots
- `grim`
- `slurp`
- `wf-recorder`
- `wl-clipboard`
- `feh`
- `mpv`

### Additional Install

Tailscale: `curl -fsSL https://tailscale.com/install.sh | sh`

Starship: `curl -sS https://starship.rs/install.sh | sh`

Enable bluetooth:
- `systemctl enable bluetooth.service`
- `systemctl start bluetooth.service`

Framework Laptop: Deactivate the Automatic Light Sensor
- Move the `modprobe/framework-als-deactivate.conf` to `/etc/modprobe.d/framework-als-deactivate.conf`

Scaling
- If using Hyprland with 1.0 scaling - set font sizes to 14
- If using Hyprland with 1.25 scaling - set font sizes to 11

### Install .config

Move all the packages in the `config` folder to the local `.config` - which should add all the configuration needed

## TODO

- [ ] Make it easier to change wallpaper for desktop and lock screen at the same time
- [ ] Add Dunst notifications to waybar
- [ ] Add rofi power menu
- [ ] Add install script


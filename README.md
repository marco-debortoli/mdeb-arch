# MDEB Arch

This is my personal Arch Linux configuration built using Hyprland! Some screenshots and details can be found below.

![screenshot of terminal layout](https://raw.githubusercontent.com/marco-debortoli/mdeb-arch/main/screenshots/terminal.png)

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
- `starship` (this can't be installed with yay - use the official starship install script)
- `btop`
- `nnn` (File Manager - Optional)
- `vim`

Browser
- `firefox`

Hyprland (Wayland Window Manager)
- `hyprland-git`
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
- `tlp`
- `swaylock-effects`
- `swayidle`

SSH and Networking
- `net-tools`
- `openssh`
- `tailscale` (Needed for my home network)

Wallpaper & Font
- `swww-git`
- `ttf-jetbrains-mono-nerd`

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

Enable bluetooth:
- `systemctl enable bluetooth.service`
- `systemctl start bluetooth.service`

Enable TLP
- `systemctl enable tlp.service`
- `sudo tlp start`
- Verify with: `tlp-stat -s`

Framework Laptop: Deactivate the Automatic Light Sensor
- Move the `modprobe/framework-als-deactivate.conf` to `/etc/modprobe.d/framework-als-deactivate.conf`

### Install .config

Move all the packages in the `config` folder to the local `.config` - which should add all the configuration needed

## TODO

- [ ] Make it easier to change wallpaper for desktop and lock screen at the same time
- [ ] Add Dunst notifications to waybar
- [ ] Add rofi power menu
- [ ] Look into `fw-fanctrl` for better Framework Laptop fan curves
- [ ] Add install script

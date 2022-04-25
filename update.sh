#!/bin/bash

echo "Performing Update!"

# Update Alacritty
cp .config/alacritty/alacritty.yml ~/.config/alacritty/alacritty.yml

# Update Fish
cp .config/fish/config.fish ~/.config/fish/config.fish
cp .config/fish/fish_variables ~/.config/fish/fish_variables

# Update Picom
cp .config/picom/picom.conf ~/.config/picom/picom.conf

# Update QTile
cp .config/qtile/autostart.sh ~/.config/qtile/autostart.sh
cp .config/qtile/config.py ~/.config/qtile/config.py
cp .config/qtile/key_config.py ~/.config/qtile/key_config.py

# Update Rofi
cp .config/rofi/config.rasi ~/.config/rofi/config.rasi
cp .config/rofi/hackthebox.rasi ~/.config/rofi/hackthebox.rasi

# Update Starship
cp .config/starship.toml ~/.config/starship.toml

# Update dunst
cp .config/dunst/dunstc ~/.config/dunst/dunstrc

echo "Update Complete"
echo "Run CMD + CTRL + r to restart QTile"
#!/bin/bash

VM=false;

while getopts ":v" option; do
   case $option in
      v)
         VM=true;
   esac
done

if [ $VM == true ]
then
    echo -e "Running in VM mode\n"
fi

# Step 1 - Update Arch Linux
echo "Updating Arch Linux"
echo "sudo pacman -Syu"
sudo pacman -Syu

# Step 2 - Install graphics drivers + ucode
echo "Installing graphics driver and CPU ucode"

if [ $VM == true ]
then
    echo "sudo pacman -S xf86-video-fbdev"
    sudo pacman -S xf86-video-fbdev

    echo "sudo pacman -S virtualbox-guest-utils"
    sudo pacman -S virtualbox-guest-utils
else
    echo "sudo pacman -S amd-ucode"
    sudo pacman -S amd-ucode

    echo "sudo pacman -S nvidia"
    sudo pacman -S nvidia
fi

# Step 3 - Install Xorg
echo "Install Xorg"
echo "sudo pacman -S xorg xorg-xinit"
sudo pacman -S xorg xorg-xinit

echo "Copying xinitrc"
echo "cp .config/.xinitrc ~/.xinitrc"
cp .config/.xinitrc ~/.xinitrc

# Step 4 - Installing YAY package manager
echo "Installing Yay package manager"
echo "sudo pacman -S base-devel"
sudo pacman -S base-devel

echo "mkdir yay_install"
mkdir yay_install

echo "cd yay_install"
cd yay_install

echo "git clone https://aur.archlinux.org/yay-git.git"
git clone https://aur.archlinux.org/yay-git.git

echo "cd yay-git"
cd yay-git

echo "makepkg -si"
makepkg -si

echo "cd ../../"
cd ../../

echo "rm -rf yay_install"
rm -rf yay_install

# Step 5 - Install QTile
echo "Installing QTile"
echo "sudo pacman -S python-pip qtile"
sudo pacman -S python-pip qtile

# Step 6 - Install Fonts
echo "Installing JetBrains Mono Nerd Font"
echo "yay -S nerd-fonts-jetbrains-mono"
yay -S nerd-fonts-jetbrains-mono

# Step 7 - Create the .config/ directory
echo "Creating .config directory"
echo "mkdir ~/.config"
mkdir ~/.config

# Step 8 - Alacritty, Fish and Starship
echo "Installing Alacritty, Fish Shell and Starship Prompt"

# Alacritty
echo "sudo pacman -S alacritty"
sudo pacman -S alacritty

echo "cp -r .config/alacritty ~/.config/alacritty"
cp -r .config/alacritty ~/.config/alacritty

# Fish
echo "sudo pacman -S fish"
sudo pacman -S fish

echo "chsh -s /usr/bin/fish"
chsh -s /usr/bin/fish

echo "cp -r .config/fish ~/.config/fish"
cp -r .config/fish ~/.config/fish

# Starship
echo "curl -sS https://starship.rs/install.sh | sh"
curl -sS https://starship.rs/install.sh | sh

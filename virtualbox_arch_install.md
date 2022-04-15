# mArch VM Installation Instructions
Video Followed: https://www.youtube.com/watch?v=PQgyW10xD8s

1. Download the Arch Linux ISO from a mirror
- Such as http://mirror.csclub.uwaterloo.ca/archlinux/iso/

## Creating the machine in VirtualBox

1. Open Virtual Box

2. Create a new VM in VirtualBox by doing Machine > New
	1. Enter a name and install location
	2. Select the machine type as `Linux`
	3. Select the machine version as `Arch Linux (64 bit)`

3. Provision the VM with 4GB of RAM (4096)

4. For the Hard Disk menu, just leave as is - `Create a virtual hard disk now`

5. Select Hard disk file type as `VDI`

6. Storage on physical hard disk -> `Dynamically Allocated`

7. Give it a size of `20GB`

## Adjusting VM settings

1. Right click on the VM and click `Settings`

2. On the `System` settings, `Processor` tab, give the VM `2` or more CPUs

3. Under `Motherboard` (in `System`) - click `Enable EFI (Special OSes Only)`

4. Under `Display` settings, `Screen` tab, give it 128MB of Video Memory

5. Go to `Storage` settings - click the little optical disk next to `Controller IDE`

6. Add the Arch Linux ISO

## Initial Boot

1. Launch the VM
	1. Note you can always use `Scaled Mode` if the screen is small with `CMD+C`

2. Open the Arch wiki installation guide (which we will be following along with)

3. Verify that you have working internet with -> `ping www.google.com`

4. Enable `NTP` with `timedatectl set-ntp true`
	1. Verify with `timedatectl status`


## Partition the Disk

1. Run `fdisk -l` to see available disks to install on

2. Run `fdisk /dev/<disk>` where `<disk>` is the disk that you want to install Arch on
	1. Note this will open a submenu like system asking for additional commands

3. Type `g` to create a `GPT` partition table

4. Type `n` to create a new partition
	1. Partition Number -> `1`
	2. First sector -> Go with default (just hit enter)
	3. Last sector -> `+550M`
		1. This is the EFI partition

5. Type `n` to create a new partition
	1. Partition Number -> `2`
	2. First sector -> Go with default (just hit enter)
	3. Last sector -> `+2G`
		1. This is the swap partition

6. Type `n` to create a new partition
	1. Partition Number -> `3`
	2. First sector -> Go with default (just hit enter)
	3. Last sector -> Give all remaining space
		1. This is the filesystem

6. Type `t` to change a partition type
	1. Partition Number -> `1`
	2. Partition Type -> `1` (EFI System)

7. Type `t` to change a partition type
	1. Partition Number -> `2`
	2. Partition Type -> `19` (Linux Swap)

8. Type `w` to write changes to the disks
	1. Then review with `fdisk -l` that the new partitions appear

## Creating the filesystem

1. `mkfs.fat -F32 /dev/<disk>1`
	1. This will format the EFI partition FAT 32

2. `mkswap /dev/<disk>2`
	1. This will format the swap partition

3. `swapon /dev/<disk>2`
	1. Turn on the swap partition

4. `mkfs.ext4 /dev/<disk>3`
	1. This will format the main linux filesystem

## Base Installation

1. `mount /dev/<disk>3 /mnt`
	1. Mounting the new disk filesystem so that we can install things on it

2. `pacstrap /mnt base linux linux-firmware`
	1. This will install linux on `/mnt`

3. `genfstab -U /mnt >> /mnt/etc/fstab`
	1. Generates the filesystem table

## Setting up the new system

1. `arch-chroot /mnt`
	1. Change into the root directory of our new machine

2. `ln -sf /usr/share/zoneinfo/Canada/Eastern /etc/localtime`
	1. This will set the timezone

3. `hwclock --systohc`
	1. This will set the hardware clock

4. Install an editor: `pacman -S vim`

5. Run `vim /etc/locale.gen`
	1. Find the locale you need - in my case `en_CA.UTF-8 UTF-8` and uncomment it
	2. Save and exit

6. `locale-gen`
	1. Generates the locales

7. `vim /etc/hostname`
	1. Set the hostname such as `mArch-vbox`

8. Create a host file -> `vim /etc/hosts`
```
127.0.0.1     localhost
::1           localhost
127.0.1.1     mArch-vbox.localdomain     mArch-vbox
```

## Setup initial users

1. `passwd`
	1. Set the root password

2. `useradd -m marco`
	1. Adds the user `marco`

3. `passwd marco`
	1. Set the password for marco

4. `usermod -aG wheel,audio,video,optical,storage marco`
	1. Adds `marco` to all the above groups
	2. `wheel` = `sudo`

5. Install sudo -> `pacman -S sudo`

6. `EDITOR=vim visudo`
	1. Uncomment the line about the wheel group
	2. `%wheel ALL=(ALL:ALL) ALL`

## Setting up Grub

1. `pacman -S grub`
	1. Installs the grub manager

2. Since we are using EFI - run: `pacman -S efibootmgr dosfstools os-prober mtools`

3. `mkdir /boot/EFI`
	1. Creating the EFI boot directory

4. `mount /dev/<disk>1 /boot/EFI`
	1. Mount the EFI partition to that boot directory

5. `grub-install --target=x86_64-efi --bootloader-id=grub_uefi --recheck`
	1. Install grub to the boot directory

6. `grub-mkconfig -o /boot/grub/grub.cfg`

## Final Installation

1. `pacman -S networkmanager git`

2. `systemctl enable NetworkManager`

## Unmount and reboot

1. `exit` (exits out of the chroot)

2. `umount -l /mnt`
	1. Unmount our filesystem

3. `reboot`
	1. (or `shutdown -h now` in a VM)

## VM Remove ISO

1. Select the ISO in `Settings` and click the red `x` at the bottom

# 🚀 Voyager GE 20.04.2 LTS Live USB — Reference Guide

This USB is a **dedicated Voyager / Ubuntu-based test & installer medium**.

Distribution: Voyager GE  
Base: Ubuntu 20.04 LTS  
Version: 20.04.2  
Architecture: 64-bit  
USB Size: ~2.7 GB  
Free Space: 0 MB (100% full)

This USB is **NOT a storage device**. It is a **read-only live boot & installation tool**.

---

## ✅ What This USB Is For (Primary Uses)

This Voyager Live USB is designed for:

- ✅ Trying Voyager GE without installing
- ✅ Testing hardware compatibility:
  - Wi-Fi
  - Graphics (Intel / AMD / NVIDIA)
  - Sound
  - Bluetooth
  - Touchpad
- ✅ Installing Voyager GE on:
  - Laptops
  - Backup machines
  - Test systems
- ✅ Emergency access to:
  - Linux partitions
  - Windows partitions
  - File recovery via live session
- ✅ Basic system diagnostics & repair

---

## ❌ What This USB Is NOT For

Because this USB is **100% full and non-persistent**:

❌ Do NOT use it for:
- File storage  
- Backups  
- Encrypted vaults  
- Persistence  
- Daily work  
- Data transfer  

Anything saved during a live session is:
➡️ Stored only in RAM  
➡️ **Lost on shutdown**

---

## ✅ What The Folders Mean

```

boot/        → Kernel and boot files
casper/      → Core Ubuntu live system (initrd, squashfs)
dists/       → Package repository structure
EFI/         → UEFI bootloader
install/     → Installer boot components
isolinux/    → Legacy BIOS bootloader
md5sum.txt   → File integrity checksums
pool/        → Software packages
preseed/     → Automated installer configs
ubuntu/     → Ubuntu branding & metadata

````

⚠️ **Do NOT delete or modify any of these files.**
Doing so can break booting or installation.

---

## ✅ How To Boot From This USB

1. Insert the USB
2. Power on the PC
3. Press:
   - `F12`, `Esc`, `F9`, or `Del` (varies by system)
4. Select the Voyager USB device
5. Choose:
   - **Try Voyager without installing**
   - or **Install Voyager**

---

## ✅ Typical Use Scenarios

### 🧪 1. Test Voyager Without Installing
- Boot live
- Explore the Voyager desktop
- Test drivers and hardware
- Reboot → system remains unchanged

---

### 💿 2. Install Voyager GE
- Boot live
- Click **Install Voyager**
- Follow partitioning carefully
- Voyager becomes the installed OS

---

### 🛠️ 3. Emergency File Recovery
- Boot Voyager live
- Mount internal disks
- Copy files to:
  - External hard drive
  - Another USB
  - Network share

---

## ✅ Free Space Status

Current status:
- Total Size: 2.7 GB
- Used: 2.7 GB
- Available: 0 MB

This confirms:
- ✅ Perfect as a **live test & installer USB**
- ❌ Not usable for storage or persistence

---

## ✅ Why It Appears as Two Drives

This USB uses a **hybrid multi-partition ISO layout**:
- One partition for UEFI/boot
- One for the live filesystem

File managers show these as **two drives**, even though it is **one physical USB**.

✅ Normal  
✅ Expected  
❌ Not a fault

---

## ✅ Companion Tools (Your Full Toolkit)

This Voyager USB complements:

- 🔐 Encrypted Secure USB → passwords & sensitive documents  
- 🛠 MX Live USB → deep rescue & boot repair  
- 🧪 Fedora KDE Live USB → Fedora testing & install  
- 💾 Large External Drive → backups & snapshots  

Each device has a **single clear purpose**.

---

## ✅ If You Ever Want To Repurpose This USB

⚠️ This will **permanently erase Voyager** from the USB:

```bash
sudo wipefs -a /dev/sdX
sudo parted -s /dev/sdX mklabel gpt
sudo parted -s -a optimal /dev/sdX mkpart primary 0% 100%
sudo mkfs.exfat /dev/sdX1
````

Replace `sdX` with the correct USB device.

Only do this **after creating another Voyager or Ubuntu installer USB**.

---

## ✅ Golden Rules

1. Never delete files from this USB.
2. Never try to store files on it.
3. Never format it casually.
4. Always keep at least one Ubuntu-based live installer.
5. Recreate it if boot ever fails.

---

✅ STATUS: **VERIFIED WORKING VOYAGER GE 20.04.2 LTS LIVE USB**

u’d like next 👌
```

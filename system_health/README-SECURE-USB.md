
# 🔐 Secure Encrypted USB Guide (MX Linux)

This document explains how to:
- Create a **fully encrypted USB drive**
- Unlock and use it safely
- Lock it correctly
- Recover from common problems
- Avoid permanent data loss

This guide is tested and verified on MX Linux using:
- `cryptsetup`
- `ext4` filesystem
- LUKS full-disk encryption

---

# ⚠️ CRITICAL WARNING

> If you forget your encryption password, **ALL DATA IS PERMANENTLY LOST.**
There is **NO recovery without the password or header backup**.

---

# ✅ PART 1 — IDENTIFY THE USB DEVICE

Always verify before ANY disk operation:

```bash
lsblk
````

Example:

```
sdb     7.6G  disk
└─sdb1  7.6G  part
```

✅ The removable device (`RM = 1`) with correct size is your USB.
❌ NEVER operate on `sda` or `nvme0n1` (system disks).

---

# ✅ PART 2 — ONE-TIME ENCRYPTION SETUP (ERASES EVERYTHING)

⚠️ This permanently deletes all data on the USB.

## 1. Unmount the USB

```bash
sudo umount /dev/sdb* 2>/dev/null
```

## 2. Encrypt the USB with LUKS

```bash
sudo cryptsetup luksFormat /dev/sdb1
```

Type:

```
YES
```

Then enter a **strong password**.

---

## 3. Unlock the Encrypted USB

```bash
sudo cryptsetup open /dev/sdb1 secureusb
```

Creates:

```
/dev/mapper/secureusb
```

---

## 4. Create Encrypted Filesystem

```bash
sudo mkfs.ext4 /dev/mapper/secureusb
```

---

## 5. Mount the Secure USB

```bash
sudo mkdir -p /media/jasvir/SECURE_USB
sudo mount /dev/mapper/secureusb /media/jasvir/SECURE_USB
```

---

## 6. Fix Ownership (IMPORTANT FOR PASTE IN FILE MANAGER)

```bash
sudo chown -R jasvir:jasvir /media/jasvir/SECURE_USB
```

---

## 7. Create Secure Folder Structure

```bash
mkdir -p /media/jasvir/SECURE_USB/{Passwords,Keys,Documents,Emergency}
```

---

# ✅ PART 3 — DAILY USAGE (NORMAL WORKFLOW)

### 🔓 Unlock & Mount (WHEN YOU PLUG IN USB)

```bash
sudo cryptsetup open /dev/sdb1 secureusb
sudo mount /dev/mapper/secureusb /media/jasvir/SECURE_USB
```

Now use it normally at:

```
/media/jasvir/SECURE_USB
```

---

### 📂 Copy Files (GUI or Terminal)

GUI:

* Open file manager
* Paste normally inside SECURE_USB folders

Terminal:

```bash
cp ~/Documents/file.pdf /media/jasvir/SECURE_USB/Documents/
```

---

### 🔒 Lock & Secure (ALWAYS DO THIS BEFORE UNPLUGGING)

```bash
sudo umount /media/jasvir/SECURE_USB
sudo cryptsetup close secureusb
```

⚠️ NEVER unplug without doing this first.

---

# ✅ PART 4 — VERIFY MOUNT STATUS

```bash
df -h | grep SECURE
```

If nothing shows → it is locked.

---

# ✅ PART 5 — DISASTER RECOVERY HEADER BACKUP (DO THIS ONCE)

This protects against corruption:

```bash
sudo cryptsetup luksHeaderBackup /dev/sdb1 --header-backup-file ~/Documents/SECURE_USB_HEADER_BACKUP.img
```

Store this file:

* On cloud storage
* On your main external hard drive
* ❌ NOT on this USB

---

# ❌ COMMON PROBLEMS & FIXES

## ❌ Paste option missing

✅ Fix:

```bash
sudo chown -R jasvir:jasvir /media/jasvir/SECURE_USB
```

---

## ❌ USB says "device in use"

✅ Fix:

```bash
sudo umount /dev/sdb1
```

---

## ❌ USB shows size as 0B

✅ Fix:

* Physically unplug
* Wait 10 seconds
* Plug into another port
* Run:

```bash
lsblk
```

---

# ✅ PART 6 — WHAT TO STORE HERE (BEST PRACTICES)

✅ Good for:

* Aadhaar / PAN / Passport
* Password manager backups
* SSH keys
* OTP recovery keys
* Legal documents
* Emergency recovery notes

❌ Do NOT store:

* Movies
* Large downloads
* Software installers
* Temporary files

---

# ✅ SECURITY RULES

1. Never leave it unlocked.
2. Never share your password.
3. Always keep header backup.
4. Always unmount before unplugging.
5. Never run `mkfs`, `wipefs`, or `dd` on this disk again.

---

# ✅ QUICK COMMAND SUMMARY

Unlock:

```bash
sudo cryptsetup open /dev/sdb1 secureusb
sudo mount /dev/mapper/secureusb /media/jasvir/SECURE_USB
```

Lock:

```bash
sudo umount /media/jasvir/SECURE_USB
sudo cryptsetup close secureusb
```

---

✅ **STATUS: VERIFIED WORKING ENCRYPTED USB VAULT ON MX LINUX**

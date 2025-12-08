
# 💾 USB / External Drive Formatting Guide (MX Linux)

This document explains the **safe, correct, and repeatable** way to format any USB or external hard drive on MX Linux.

This avoids:
- Multiple partitions showing as multiple drives
- Broken mounts
- File system errors
- Accidental formatting of the wrong disk

---

## ⚠️ GOLDEN SAFETY RULE

> **Always confirm the disk name with `lsblk` BEFORE formatting.  
> Never assume `/dev/sdb` is correct.**

---

## ✅ Step 1: Identify the USB Drive

```bash
lsblk
````

Example output:

```
sdb     231.1G  disk
└─sdb1  231.1G  part
```

✔ The one with:

* `RM = 1`
* Correct size
* Not your system disk (`/`)

That is your USB device (example: `/dev/sdb`).

---

## ✅ Step 2: Unmount Everything on That USB

```bash
sudo umount /dev/sdb* 2>/dev/null
```

(Replace `sdb` if your device is different.)

---

## ✅ Step 3: Wipe All Old Partition Data

This removes:

* Old boot loaders
* Old hidden partitions
* Old filesystem traces

```bash
sudo wipefs -a /dev/sdb
```

---

## ✅ Step 4: Create a New Clean Partition Table (GPT)

```bash
sudo parted -s /dev/sdb mklabel gpt
```

---

## ✅ Step 5: Create ONE Full-Size Partition

```bash
sudo parted -s -a optimal /dev/sdb mkpart primary 0% 100%
```

---

## ✅ Step 6: Format the Drive (exFAT Recommended)

Best for **Linux + Windows compatibility**:

```bash
sudo mkfs.exfat -n MyUSB /dev/sdb1
```

You may rename `MyUSB` to:

* `SeagateUSB`
* `Backups`
* `Snapshots`
* `MediaDrive`

---

## ✅ Step 7: Unplug & Replug the USB

This forces the system to reread the new partition table.

---

## ✅ Step 8: Verify Final State

```bash
lsblk
```

✅ You should see:

```
sdb
└─sdb1  231.1G  /media/username/MyUSB
```

This confirms:

* ✅ One partition
* ✅ Full size available
* ✅ Clean filesystem
* ✅ No duplicate drives

---

## ✅ Manual Mount (If It Doesn’t Auto-Mount)

```bash
sudo mkdir -p /media/jasvir/MyUSB
sudo mount /dev/sdb1 /media/jasvir/MyUSB
```

---

## ✅ Move Backups / Snapshots

```bash
sudo mv /home/snapshot/*.iso* /media/jasvir/MyUSB/
```

---

## ❌ COMMON MISTAKES TO AVOID

❌ Running `mkfs` before creating a partition
❌ Using `exfat` inside `parted`
❌ Formatting without checking `lsblk`
❌ Formatting `sda` or the system disk
❌ Mixing interactive `parted` with pasted commands

---

## ✅ Emergency Recovery (If USB Acts Weird Again)

```bash
sudo wipefs -a /dev/sdb
sudo parted -s /dev/sdb mklabel gpt
sudo parted -s -a optimal /dev/sdb mkpart primary 0% 100%
sudo mkfs.exfat -n MyUSB /dev/sdb1
```

---

## ✅ Best Practices

* Always store backups on **separate physical drives**
* Use **exFAT for portability**, **ext4 for Linux-only**
* Never unplug during formatting
* Always verify with `lsblk` after formatting

---

## ✅ Last Verified Working On

* MX Linux
* External USB HDD / SSD
* exFAT filesystem


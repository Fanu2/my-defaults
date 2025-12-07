
# 🛠️ MX Linux System Health & Maintenance Playbook
**Personal Long-Term Operations Guide**

This guide is your **single source of truth** for keeping your MX Linux system:

- ✅ Fast  
- ✅ Clean  
- ✅ Secure  
- ✅ Update-safe  
- ✅ Crash-resistant  

Use this anytime your system feels slow, storage fills up, or before major updates.

---

## 🧠 CURRENT BASELINE (LAST VERIFIED)

- ✅ MX Linux 23.6 KDE
- ✅ Root `/` under 50% usage
- ✅ RAM healthy, swap unused
- ✅ No broken packages
- ✅ Clean APT sources
- ✅ No Plex, no legacy keys
- ✅ Recovery partition untouched

---

# ⚡ DAILY / WEEKLY QUICK HEALTH CHECK

Run this anytime:

```bash
echo "====== DISK ======" && df -h && \
echo "====== RAM ======" && free -h && \
echo "====== SERVICES ======" && service --status-all | grep '\[ + \]' && \
echo "====== UPDATES ======" && apt list --upgradable && \
echo "====== MX VERSION ======" && cat /etc/mx-version && \
echo "====== KERNEL ======" && uname -r
````

### ✅ Healthy System Looks Like:

* `/` under **80%**
* RAM has **>1GB available**
* No massive swap usage
* No long update lists

---

# 🔄 SAFE SYSTEM UPDATE (ALWAYS USE THIS)

```bash
sudo apt update
sudo apt full-upgrade -y
sudo apt autoremove --purge -y
sudo apt clean
```

✅ Safe
✅ Does not break MX
✅ Keeps security fully patched

---

# 🧹 SUPER SAFE CLEAN COMMAND (RUN ANYTIME)

```bash
sudo apt clean && sudo apt autoclean && sudo apt autoremove --purge -y \
&& rm -rf ~/.cache/* && rm -rf ~/.local/share/Trash/* \
&& sudo journalctl --vacuum-size=100M
```

✅ Frees GBs
✅ Prevents update failures
✅ Clears logs, cache, trash

---

# 🔥 FIND WHAT IS EATING DISK

### 🔍 Files Larger Than 1GB

```bash
find / -type f -size +1G -exec ls -lh {} \; 2>/dev/null
```

### 📁 Biggest Folders in Home

```bash
du -h --max-depth=1 ~ | sort -h
```

---

# 🤖 AI MODEL STORAGE (BIGGEST SPACE RISK)

### Ollama:

```
~/.ollama/models/blobs/
```

### LM Studio:

```
~/.lmstudio/models/
```

✅ Each model = 3–8GB
✅ Safe to delete
✅ Will re-download if needed

### 🔥 Emergency AI Cleanup:

```bash
rm -rf ~/.ollama/models/blobs/*
rm -rf ~/.lmstudio/models/*
```

---

# 🛑 DO NOT EVER DELETE THESE

| Path                        | Why                   |
| --------------------------- | --------------------- |
| `/boot`                     | Bootloader            |
| `/lib`                      | Core system libraries |
| `/usr`                      | Applications          |
| `/etc`                      | System configs        |
| Windows Recovery Partitions | OS recovery           |

---

# 🛡️ PREVENT LOG BLOAT FOREVER (IMPORTANT)

```bash
sudo nano /etc/systemd/journald.conf
```

Add or edit:

```
SystemMaxUse=200M
```

Then:

```bash
sudo systemctl restart systemd-journald
```

✅ System logs will never eat your disk again.

---

# ⏱️ AUTOMATIC WEEKLY CLEANUP (SET & FORGET)

```bash
crontab -e
```

Add:

```
0 3 * * 0 sudo apt clean && sudo apt autoremove -y && rm -rf ~/.cache/*
```

✅ Auto-cleans every Sunday
✅ No manual work required

---

# 💾 STORAGE SAFETY RULES

* ✅ Always keep **20–25 GB free on `/`**
* ✅ Never allow `/` above **85%**
* ✅ Store large videos on **external drives**
* ✅ AI models never stay long-term on `/`

---

# ⚙️ PERFORMANCE BOOST OPTIONS (OPTIONAL)

### ✅ Enable ZRAM

```bash
sudo apt install zram-tools
```

### ✅ Reduce Swap Pressure

```bash
echo "vm.swappiness=10" | sudo tee -a /etc/sysctl.conf
sudo sysctl -p
```

---

# 🚨 EMERGENCY RECOVERY MODE

If system becomes unstable:

```bash
sudo dpkg --configure -a
sudo apt -f install
sudo apt full-upgrade --fix-missing
```

---

# ✅ WHAT THIS PLAYBOOK PROTECTS YOU FROM

* ❌ Disk full crashes
* ❌ Failed updates
* ❌ Broken packages
* ❌ Slow KDE performance
* ❌ AI models silently eating storage
* ❌ Log files growing forever
* ❌ Background service overload

---

# 🏁 FINAL GOLDEN RULE

> 🟢 **If your system feels slow, check disk first.**

```bash
df -h
```

Low disk space causes:

* Freezes
* Browser crashes
* Software install failures
* Boot problems

---

# ✅ END RESULT

With this guide, your MX Linux system remains:

* 🚀 Fast
* 🔒 Secure
* 🧹 Clean
* 🧠 Stable
* 🎬 FFmpeg-ready
* 🤖 AI-ready

**This is your lifetime MX Linux survival guide.**

`

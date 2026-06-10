# ESP32 CSI Tool Setup & Configuration Guide

This guide explains how to set up the ESP32 hardware and environment to collect Wi-Fi Channel State Information (CSI) for spatial analytics and tracking.

---

## 🛠️ Step 1: Install ESP-IDF
This project requires **ESP-IDF v4.3**. Install it by following the official setup instructions:
* **Installer Link**: [ESP-IDF v4.3 Download](https://dl.espressif.com/dl/esp-idf/?idf=4.3)
* **Official Guide**: [ESP-IDF Getting Started Guide](https://docs.espressif.com/projects/esp-idf/en/release-v4.3/esp32/get-started/index.html)

> [!NOTE]
> Ensure you can successfully build and flash a default ESP-IDF example project (like hello_world) to verify your development environment before moving forward.

---

## 📥 Step 2: Clone the Base Repository
Clone the original ESP32 CSI Tool repository:
```bash
git clone https://github.com/StevenMHernandez/esp32-csi-tool
```

---

## ⚙️ Step 3: Select Operating Mode
Navigate to the directory corresponding to your desired operating mode. To form a complete system, use at least two ESP32 devices:
1. **TX Mode (Active Transmitter/Station)**: Sends packet requests and triggers CSI signals.
   ```bash
   cd ./active_sta
   ```
2. **RX Mode (Active Access Point)**: Receives packets and measures CSI.
   ```bash
   cd ./active_ap
   ```
3. **Passive Mode**: Listens silently to CSI packets on a pre-defined channel.
   ```bash
   cd ./passive
   ```

---

## 🔧 Step 4: Configure via Project Menuconfig
Within your selected working directory, open the IDF configuration menu:
```bash
idf.py menuconfig
```

Configure the following recommended settings:

### 🚀 1. Serial Baud Rate Optimization
For high-rate data transfers:
* Navigate to: `Serial flasher config` -> `'idf.py monitor' baud rate` -> Select **Custom Baud Rate**
* Set value to: **`921600`**
* Navigate to: `Component config` -> `Common ESP32-related` -> `Channel for console output` -> Select **Custom UART**
* Set Console baud rate to: **`921600`**

### 📶 2. Wi-Fi CSI Settings
* Navigate to: `Component config` -> `Wi-Fi` -> **`WiFi CSI (Channel State Information)`** -> Press **Space** to select (marked with `*`).

### ⏱️ 3. FreeRTOS Tick Rate Setup
* Navigate to: `Component config` -> `FreeRTOS` -> **`Tick rate (Hz)`** -> Set to **`1000`**

### 🔬 4. CSI Custom Metrics
* Navigate to: `ESP32 CSI Tool Config` to customize logging intervals, Wi-Fi channels, SD Card pins, and subcarrier capture configurations.

---

## ⚡ Step 5: Flash & Monitor
Compile the application, write it to the microcontroller, and open the serial monitor:
```bash
idf.py flash monitor
```

* **`flash`**: Compiles and writes the binary to the ESP32.
* **`monitor`**: Opens the serial stream console to read CSI output.
* **Exit Console**: Press `Ctrl + ]` to exit.

---

## 💾 Step 6: Collect CSI Data

### Option A: Save Directly to SD Card
If your ESP32 board has an onboard SD card slot (e.g., TTGO T8 V1.7), the CSI tool writes files to the card automatically.

### Option B: Capture via Serial Port (PC-side)
Dump the console stdout directly to a CSV file from command prompt:
```cmd
idf.py monitor | findstr "CSI_DATA" > my-experiment-file.csv
```

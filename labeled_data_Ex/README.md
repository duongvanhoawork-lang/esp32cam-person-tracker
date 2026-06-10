# 📂 `labeled_data_Ex` — Sample CSI Dataset

This directory contains **example labeled CSI (Channel State Information) recordings**
collected from a real ESP32 deployment under the experimental conditions described in the
main [README](../README.md).

Each file corresponds to one physical cell in the 3×3 metre sensing grid.

| File | Cell | Position |
|------|------|----------|
| `grid_1.csv` | Cell 1 | Top-Left |
| `grid_2.csv` | Cell 2 | Top-Center |
| `grid_3.csv` | Cell 3 — Top-Right |
| `grid_4.csv` | Cell 4 | Middle-Left |
| `grid_5.csv` | Cell 5 | Center |
| `grid_6.csv` | Cell 6 | Middle-Right |
| `grid_7.csv` | Cell 7 | Bottom-Left |
| `grid_8.csv` | Cell 8 | Bottom-Center |
| `grid_9.csv` | Cell 9 | Bottom-Right |

---

## ⚠️ Important: Noise Characteristics of Wi-Fi CSI

Wi-Fi CSI signals are **inherently very noisy**. Unlike clean sensor readings,
CSI amplitude data is affected by a wide range of uncontrollable environmental factors:

- **Multipath interference** — reflections from walls, furniture, and the human body
  cause constructive and destructive wave superposition that randomly shifts amplitude values.
- **Hardware-level thermal noise** — the ESP32 RF front-end introduces thermal noise
  that fluctuates at a per-packet level, even in a completely static environment.
- **Body orientation & micro-movements** — subtle postural shifts (breathing, weight
  transfer, head turns) produce amplitude variations that are indistinguishable from
  inter-cell movement at low sample counts.
- **Channel contention** — nearby Wi-Fi networks operating on overlapping channels
  inject burst interference that appears as sudden, extreme amplitude spikes.
- **Non-stationarity** — the statistical distribution of the CSI signal drifts over
  time due to temperature changes in both the hardware and the surrounding environment.

Because of these combined noise sources, **a very large number of samples is required**
before the signal-to-noise ratio (SNR) is sufficient for the Transformer model to learn
reliable spatial propagation patterns for each cell.

---

## 📏 Minimum Data Requirement: 2,000,000 Lines per Cell

> [!IMPORTANT]
> For acceptable model accuracy (target ≥ 80%), each `grid_N.csv` file should contain
> **at least 2,000,000 lines** of raw `CSI_DATA` packets before filtering.

### Why 2 Million Lines?

| Factor | Impact |
|--------|--------|
| **4-stage noise filter** consumes data at the boundary of each window | Up to 5–10% of rows are discarded during the Hampel and Butterworth stages |
| **Sliding window augmentation** (step = 25, length = 100) expands samples | ~75× sequence multiplication from raw rows to training windows |
| **Class imbalance correction** requires sufficient samples in every cell | Rare posture variants (e.g., sitting near the cell edge) need adequate coverage |
| **Model generalisation** over session-to-session distribution shift | More data reduces overfitting to a single recording session |

The files in this sample directory contain approximately **10,000 lines each** (~4 MB).
This is intentionally kept small for quick prototyping and pipeline verification only.

> [!WARNING]
> Do **not** use this sample dataset to train a production model.
> 10,000 lines per cell is far below the 2,000,000-line minimum needed for reliable
> real-world deployment. Models trained on this data will show artificially high
> training accuracy but will generalise poorly to live inference.

---

## ✅ Recommended Data Collection Protocol

To reach the 2,000,000-line target for each cell:

1. **Session duration**: Run `1_collect_labeled_data.py` for **at least 30–40 minutes
   per cell** at 921,600 baud (approximately 300–400 packets/second → ~1 M rows per 1 hour).
2. **Posture diversity**: During each session, alternate between:
   - Standing upright (facing TX, facing RX, facing sideways)
   - Sitting on a chair
   - Slow movement within the cell boundary
   - Momentary stillness (at least 20% of the session)
3. **Multiple sessions**: Collect across **at least 2–3 separate sessions** (different
   times of day) per cell to capture environmental drift.
4. **Verify before filtering**: Open the raw CSV and confirm the row count exceeds
   2,000,000 before running `2_data_filtering.py`.

```powershell
# Quick row count check (PowerShell)
(Get-Content .\labeled_data_Ex\grid_1.csv | Measure-Object -Line).Lines
```

```bash
# Quick row count check (bash / WSL)
wc -l labeled_data_Ex/grid_1.csv
```

---

## 📄 CSV Format Reference

Each row in the CSV file is a single raw `CSI_DATA` packet captured from the ESP32
serial stream. The format mirrors the ESP32 CSI Tool output:

```
CSI_DATA,<timestamp>,<mac>,<rssi>,<rate>,<sig_mode>,<mcs>,<bandwidth>,
<smoothing>,<not_sounding>,<aggregation>,<stbc>,<fec_coding>,<sgi>,
<noise_floor>,<ampdu_cnt>,<channel>,<secondary_channel>,<local_timestamp>,
<ant>,<sig_len>,<rx_state>,[<imag_1> <real_1> <imag_2> <real_2> ... <imag_64> <real_64>]
```

The pipeline extracts the last bracketed field and computes per-subcarrier amplitude:

$$\text{Amplitude}_i = \sqrt{\text{Real}_i^2 + \text{Imag}_i^2}, \quad i = 1 \ldots 64$$

---

## 🔗 Related Files

| Script | Role |
|--------|------|
| [`1_collect_labeled_data.py`](../1_collect_labeled_data.py) | Collects and saves raw CSI packets to this directory |
| [`2_data_filtering.py`](../2_data_filtering.py) | Applies the 4-stage noise reduction pipeline to all grid files |
| [`4_train_transformer.py`](../4_train_transformer.py) | Trains the Transformer model using the filtered output |
| [`3_realtime_predict.py`](../3_realtime_predict.py) | Runs live inference using the trained model weights |

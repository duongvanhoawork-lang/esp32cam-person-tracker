# -*- coding: utf-8 -*-
"""
================================================================================
DATA FILTERING — 4-STAGE CSI SIGNAL DENOISING & SMOOTHING PIPELINE
================================================================================

[LIBRARY INSTALLATION]
  set NO_PROXY=* && pip install numpy scipy

[FILTER DESCRIPTION & CONFIGURATION PARAMETERS]
  Reads all raw data files grid_1.csv ... grid_9.csv from e:\\DATA\\labeled_data\\,
  applies the 4-stage sequential noise-reduction pipeline,
  and writes the cleaned results to e:\\DATA\\labeled_data_filtered\\

  Filter stages applied (in strict logical order):

  1. Hampel Filter (Spike / Temporal Outlier Removal)
     - Window Size: 10 neighbouring samples on each side.
     - Sigma threshold: 2.0.
     - Mechanism: Computes the local Median and MAD (Median Absolute Deviation)
       within a sliding window. Values exceeding sigma * MAD are replaced with
       the local Median.

  2. IQR Filter (Statistical Distribution Clamp — Interquartile Range)
     - IQR Multiplier: 1.5.
     - Mechanism: Defines the valid range [Q1 - 1.5*IQR, Q3 + 1.5*IQR].
       Signal points outside this range are clamped to the boundary.

  3. Butterworth Low-Pass Filter (LPF)
     - Cutoff Frequency: 0.05 (normalized, range 0.0 – 0.5).
     - Filter Order: 5th order (provides good high-frequency roll-off).
     - Mechanism: Zero-phase bidirectional filtering (filtfilt) to suppress
       high-frequency noise from the environment and unintended motion.

  4. Savitzky-Golay Filter (Peak-Preserving Smoothing)
     - Window Length: 21 samples (must be odd).
     - Polynomial Order: 3.
     - Mechanism: Fits a local polynomial using least-squares regression,
       producing a smooth CSI curve while preserving characteristic peaks and valleys.

[IMPLEMENTATION DIRECTION & DATA PROCESSING FLOW]
1. Parse raw CSI lines:
   - Extract the amplitude array from the raw format: CSI_DATA,...[subcarriers]
   - Compute Amplitude = sqrt(Real^2 + Imag^2) for each subcarrier (64 subcarriers).
2. Process the CSI matrix of shape (N_Samples, 64) in parallel through all 4 filter stages.
3. Reconstruct the data stream into the original format with the filtered amplitude array.
4. Write the cleaned data to the corresponding output file in the target directory.
"""

def print_architecture():
    print("=====================================================================")
    print("ALGORITHM DESCRIPTION: 4-STAGE CSI DENOISING PIPELINE")
    print("=====================================================================")
    print("Input Directory  : e:\\DATA\\labeled_data")
    print("Output Directory : e:\\DATA\\labeled_data_filtered")
    print("Pipeline Stages  :")
    print("  Stage 1. Hampel Filter     -> Local spike & outlier removal via MAD")
    print("  Stage 2. IQR Clamp Filter  -> Statistical boundary clipping (1.5 * IQR)")
    print("  Stage 3. Butterworth LPF   -> Phase-preserving low-pass filter (Cutoff: 0.05, Order: 5)")
    print("  Stage 4. Savitzky-Golay    -> Local polynomial smoothing (Window: 21, Poly: 3)")
    print("=====================================================================")
    print("Note: The executable source file has been converted to a research blueprint.")
    print("To run the actual implementation, please refer to the linked main repository.")

if __name__ == '__main__':
    print_architecture()

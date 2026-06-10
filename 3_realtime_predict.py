# -*- coding: utf-8 -*-
"""
================================================================================
REAL-TIME PREDICTOR — LIVE SPATIAL LOCALISATION USING AI TRANSFORMER
================================================================================

[LIBRARY INSTALLATION]
    set NO_PROXY=* && pip install torch numpy pyserial

[RUNTIME REQUIREMENTS]
- The transmitter (TX) and receiver (RX) must be fixed 5 metres apart
  (identical to the configuration used during training).
- The physical movement space (9 cells, 1m x 1m each) must preserve the
  same geometric structure used during data collection.
- Ensure the mobile device maintains a continuous Wi-Fi connection to keep
  the CSI transmission stream stable.

[SYSTEM CONFIGURATION PARAMETERS]
- Sliding Sequence Length: 100 consecutive CSI samples.
- Number of Subcarriers processed: 64.
- Model Path  : e:\\DATA\\transformer_csi_model.pth
- Scaler Path : e:\\DATA\\scaler_params.npz
  (stores Mean and Std for direct Z-score normalisation at inference time).

[CONFIDENCE DECISION THRESHOLDS]
1. Out-of-Zone Threshold (CONF_OUT_OF_ZONE = 0.40):
   - If the probability of the top-1 predicted class is below 40%, the model
     concludes the subject is outside the detection coverage zone (Out of Zone).
2. Boundary Threshold (CONF_BOUNDARY = 0.06):
   - Computes the probability gap between the top-1 and top-2 predictions (p1 - p2).
   - If this gap is <= 6%, the system concludes the subject is standing on the
     boundary between the two cells (e.g., Between Cell 2 and Cell 3).
   - If the gap is > 6%, the system concludes the subject is fully inside the
     cell with the highest probability.

[TRANSFORMER AI ARCHITECTURE]
- Input Layer     : Linear projection mapping 64 CSI subcarrier dimensions to d_model (128).
- Transformer Encoder:
    - 3 stacked Encoder Layers.
    - Number of attention heads (nhead): 8.
    - Feed-forward size (dim_feedforward): 256.
    - Dropout: 0.2.
- Classification Head:
    - Input: Hidden state of the last time-step in the sequence (out[:, -1, :]).
    - Fully Connected structure: Linear(128 -> 64) -> ReLU -> Dropout -> Linear(64 -> 9 classes).

[RUNTIME ALGORITHM]
1. Load the trained machine-learning model and Z-score scaler parameters from disk.
2. Open the serial port COM6 to receive the live CSI stream from the ESP32 RX device.
3. Use a sliding deque (queue) with a maximum size of 100 samples.
4. When the queue is full:
   - Apply Z-score normalisation to the entire sequence using the pre-loaded Mean and Std.
   - Convert the sequence to a Tensor and send it to the compute device (CPU/GPU).
   - Run a forward pass through the Transformer to obtain the Softmax probability distribution.
   - Apply the CONF_OUT_OF_ZONE and CONF_BOUNDARY threshold logic and print the real-time prediction.
   - Slide the window by 50% (discard the oldest 50 samples) to wait for the next batch,
     reducing overall computation latency.
"""

def print_architecture():
    print("=====================================================================")
    print("ALGORITHM DESCRIPTION: REAL-TIME SPATIAL PREDICTOR")
    print("=====================================================================")
    print("Model Path        : e:\\DATA\\transformer_csi_model.pth")
    print("Scaler Path       : e:\\DATA\\scaler_params.npz")
    print("Decision Logic    :")
    print("  - If Max Prob < 40%              -> Output: 'OUT OF ZONE'")
    print("  - If (Prob_1 - Prob_2) <= 6%     -> Output: 'BOUNDARY: Cell A & Cell B'")
    print("  - Else                           -> Output: 'INSIDE Cell A'")
    print("Sliding Window    : Sequence Length = 100 | Step Size = 50 (50% Overlap)")
    print("=====================================================================")
    print("Note: The executable source file has been converted to a research blueprint.")
    print("To run the actual implementation, please refer to the linked main repository.")

if __name__ == '__main__':
    print_architecture()

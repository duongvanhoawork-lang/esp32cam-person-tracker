# -*- coding: utf-8 -*-
"""
================================================================================
SERIAL DATA CAPTURE & WRITER (COM6)
================================================================================

[PURPOSE]
- Record the complete data stream (CSI and system logs) from the ESP32 to local disk.
- Provides raw data archival for offline research and post-processing.

[HARDWARE CONFIGURATION NOTES]
- Default connection port : COM6
- Serial communication frequency : 921600 baud
- DTR/RTS disabled to prevent the ESP32 from resetting each time the COM port is opened or closed.

[IMPLEMENTATION DIRECTION & ALGORITHM]
1. Establish a safe Serial connection using COM6 at 921600 baud.
2. Open the target output file (e.g., e:\\DATA\\data.txt) in append mode with UTF-8 encoding.
3. Continuously poll the serial receive buffer (in_waiting):
   - Read data line by line (complete lines).
   - Strip null bytes caused by transient noise spikes during cable insertion.
   - Convert from byte stream to a UTF-8 string (ignoring malformed bytes).
4. Classify and validate incoming data:
   - If data is valid: write the raw line to disk and immediately flush the write buffer
     to prevent data loss in case of power failure.
   - If data is invalid or empty: print a diagnostic message showing the raw byte
     representation (repr) of the noisy data to the console.
5. Release resources and safely close the Serial port when the user stops the program
   with an interrupt key combination.
"""

def print_architecture():
    print("=====================================================================")
    print("ALGORITHM DESCRIPTION: SERIAL DATA WRITER")
    print("=====================================================================")
    print("1. Target Output    : e:\\DATA\\data.txt (Append Mode)")
    print("2. Port Config      : COM6 | Baudrate: 921600")
    print("3. Integrity Control: Null-byte filtering & UTF-8 decoding protection")
    print("4. Disk Sync        : Instant file flush on every packet write")
    print("=====================================================================")
    print("Note: The executable source file has been converted to a research blueprint.")
    print("To run the actual implementation, please refer to the linked main repository.")

if __name__ == '__main__':
    print_architecture()

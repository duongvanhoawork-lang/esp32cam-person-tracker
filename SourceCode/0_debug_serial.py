# -*- coding: utf-8 -*-
"""
================================================================================
DIAGNOSTIC SCRIPT — RAW SERIAL DATA READER & ANALYSER (COM6)
================================================================================

[PURPOSE]
- Verify the physical UART connection between the PC and the ESP32.
- Check the integrity of CSI (Channel State Information) packets transmitted over Serial.
- Ensure the ESP32 output format matches the expected format of the data acquisition tool.

[HOW TO RUN]
- Launch the diagnostic from a terminal:
    python e:\\DATA\\debug_serial.py
- Stop the diagnostic: Press Ctrl+C

[IMPLEMENTATION DIRECTION & ALGORITHM]
1. Initialise the Serial port connection (baudrate: 921600, port: COM6) with DTR/RTS
   disabled to prevent the ESP32 from resetting when the port is opened.
2. Set up an infinite monitoring loop over the COM port buffer.
3. When data is available in the buffer:
   - Read one complete raw line (readline).
   - Clean the line: remove null bytes (\\x00) introduced by physical noise.
   - Decode the byte string to UTF-8, ignoring any malformed bytes.
4. Classify and analyse the line content:
   - If the line starts with "CSI" or "CSI_DATA": extract and display the prefix
     together with the first 120 characters to verify the amplitude array.
   - If the line contains regular system information: display it as a standard
     ESP32 log entry.
5. Release system resources (close the Serial port safely) upon receiving a
   KeyboardInterrupt signal.
"""

import sys

def print_architecture():
    print("=====================================================================")
    print("ALGORITHM DESCRIPTION: DIAGNOSTIC SERIAL INTERFACE")
    print("=====================================================================")
    print("1. Serial Connection    : COM6 | Baudrate: 921600 | DTR/RTS: False")
    print("2. Raw Stream Processing: Null-byte stripping -> UTF-8 decoding")
    print("3. Data Classification  : Split into [CSI Data Stream] & [System Log Stream]")
    print("=====================================================================")
    print("Note: The executable source file has been converted to a research blueprint.")
    print("To run the actual implementation, please refer to the linked main repository.")

if __name__ == '__main__':
    print_architecture()

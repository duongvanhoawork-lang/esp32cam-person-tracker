# -*- coding: utf-8 -*-
"""
================================================================================
LABELED CSI DATA ACQUISITION TOOL (9-Cell Spatial Grid — 1m x 1m each)
================================================================================

[LIBRARY INSTALLATION]
Open PowerShell or Command Prompt and run the following command
(if you encounter a proxy error, copy the command exactly as shown):
  $env:NO_PROXY="*"; pip install pyserial

[PHYSICAL LAYOUT (Recommended Setup)]
- Distance from TX to RX: 5 meters.
- Detection area: 3x3 m grid divided into 9 cells (each cell is 1m x 1m).
- Cell 5 is located at the center (2.5 m from both TX and RX).

[IMPLEMENTATION DIRECTION & ALGORITHM]
1. Cell selection interface:
   - Prompts the user to enter the spatial cell index to collect data for (1 to 9).
   - Validates the input (Grid Index Validation).
2. Storage directory setup:
   - Automatically creates the target directory for labeled data at: e:\\DATA\\labeled_data\\
   - Output file naming format per cell: grid_{grid_num}.csv
3. Serial connection setup for data acquisition:
   - Opens serial port COM6 at baudrate 921600. DTR/RTS disabled to prevent board reset.
4. Data acquisition & storage loop:
   - Reads data from the buffer. Removes null bytes (\\x00).
   - Filters data: Only records lines that begin with the prefix "CSI_DATA".
   - Valid CSI_DATA lines are written directly to the target CSV file with an immediate flush().
5. Handles KeyboardInterrupt to safely save the file, close the serial port,
   and report the completion of the current data collection session.
"""

def print_architecture():
    print("=====================================================================")
    print("ALGORITHM DESCRIPTION: LABELED CSI DATA ACQUISITION")
    print("=====================================================================")
    print("1. Workspace Spatial Layout : 3x3 Grid (9 Cells, 1m x 1m each)")
    print("2. Serial Ingestion         : COM6 @ 921600 baud, non-reset configuration")
    print("3. Target Directory         : e:\\DATA\\labeled_data\\grid_{1-9}.csv")
    print("4. Protocol Filter          : Line-start prefix matching on 'CSI_DATA'")
    print("=====================================================================")
    print("Note: The executable source file has been converted to a research blueprint.")
    print("To run the actual implementation, please refer to the linked main repository.")

if __name__ == '__main__':
    print_architecture()

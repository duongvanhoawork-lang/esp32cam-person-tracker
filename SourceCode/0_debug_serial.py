# -*- coding: utf-8 -*-
"""
================================================================================
SCRIPT CHẨN ĐOÁN - ĐỌC VÀ PHÂN TÍCH DỮ LIỆU THÔ TỪ CỔNG SERIAL (COM6)
================================================================================

[MỤC ĐÍCH NGHIÊN CỨU]
- Kiểm tra kết nối vật lý UART giữa máy tính và ESP32.
- Kiểm tra tính toàn vẹn của gói tin CSI (Channel State Information) truyền qua Serial.
- Đảm bảo định dạng đầu ra của ESP32 trùng khớp với định dạng bộ thu thập dữ liệu mong đợi.

[CMD HƯỚNG DẪN CHẠY]
- Chạy lệnh chẩn đoán từ terminal:
  python e:\DATA\debug_serial.py
- Dừng chẩn đoán: Nhấn Ctrl+C

[HƯỚNG ĐI VÀ THUẬT TOÁN TRIỂN KHAI]
1. Khởi tạo kết nối cổng Serial (baudrate: 921600, port: COM6) tránh reset mạch ESP32 bằng cách tắt DTR/RTS.
2. Thiết lập vòng lặp vô hạn giám sát bộ đệm cổng COM.
3. Khi có dữ liệu trong buffer:
   - Đọc một dòng dữ liệu thô (readline).
   - Tiến hành làm sạch dòng dữ liệu: Loại bỏ null bytes (\\x00) sinh ra do nhiễu vật lý.
   - Giải mã (decode) chuỗi byte sang UTF-8, bỏ qua các byte lỗi (ignore).
4. Phân tích nội dung dòng dữ liệu:
   - Nếu dòng chứa từ khóa đầu "CSI" hoặc "CSI_DATA": Tách và hiển thị tiền tố kèm theo 120 ký tự đầu tiên để kiểm tra mảng amplitude.
   - Nếu dòng chứa thông tin hệ thống thông thường: Hiển thị dòng nhật ký (log) thông thường từ ESP32.
5. Quản lý tài nguyên hệ thống (Giải phóng cổng Serial khi nhận tín hiệu ngắt KeyboardInterrupt).
"""

import sys

def print_architecture():
    print("=====================================================================")
    print("MÔ TẢ THUẬT TOÁN DIAGNOSTIC SERIAL INTERFACE")
    print("=====================================================================")
    print("1. Serial Connection: COM6 | Baudrate: 921600 | DTR/RTS: False")
    print("2. Raw Stream Processing: Null byte stripping -> UTF-8 decoding")
    print("3. Data Classification: Split into [CSI Data Stream] & [System Log Stream]")
    print("=====================================================================")
    print("Lưu ý: File mã nguồn chạy thực tế đã được chuyển đổi sang hướng tiếp cận nghiên cứu.")
    print("Để chạy thực tế, vui lòng liên kết tới repository chính chứa mã nguồn thực thi.")

if __name__ == '__main__':
    print_architecture()

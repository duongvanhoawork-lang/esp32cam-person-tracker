# -*- coding: utf-8 -*-
"""
================================================================================
BỘ THU THẬP VÀ GHI NHẬN DỮ LIỆU SERIAL PORT (COM6)
================================================================================

[MỤC ĐÍCH NGHIÊN CỨU]
- Lưu vết toàn bộ dữ liệu dòng truyền (CSI và Log) từ ESP32 xuống ổ đĩa cục bộ.
- Phục vụ việc lưu dữ liệu thô phục vụ nghiên cứu offline.

[LƯU Ý CẤU HÌNH PHẦN CỨNG]
- Cổng kết nối mặc định: COM6
- Tần số giao tiếp Serial: 921600 baud
- Tắt DTR/RTS nhằm chống hiện tượng ESP32 bị reset mỗi khi mở/đóng cổng COM.

[HƯỚNG ĐI VÀ THUẬT TOÁN TRIỂN KHAI]
1. Kết nối an toàn cổng Serial sử dụng tham số cấu hình COM6, 921600 baudrate.
2. Mở tệp tin lưu trữ dữ liệu tại đường dẫn cục bộ (ví dụ: e:\\DATA\\data.txt) ở chế độ ghi tiếp (append mode) và mã hóa UTF-8.
3. Liên tục thăm dò bộ đệm truyền nhận cổng serial (in_waiting):
   - Đọc dữ liệu theo từng dòng hoàn chỉnh.
   - Loại bỏ null bytes sinh ra bởi các xung nhiễu quá độ lúc cắm cáp.
   - Chuyển đổi từ byte stream sang chuỗi ký tự UTF-8 (bỏ qua ký tự lỗi).
4. Phân loại và kiểm tra:
   - Nếu dữ liệu hợp lệ: Ghi dữ liệu thô vào file đĩa cứng đồng thời ép xả bộ nhớ đệm ghi (flush) để tránh mất mát dữ liệu khi mất điện.
   - Nếu dữ liệu bị lỗi/trống: In thông báo chẩn đoán dữ liệu nhiễu dưới dạng biểu diễn byte (repr) lên màn hình.
5. Giải phóng tài nguyên và đóng cổng Serial an toàn khi người dùng dừng chương trình bằng tổ hợp phím ngắt.
"""

def print_architecture():
    print("=====================================================================")
    print("MÔ TẢ THUẬT TOÁN SERIAL DATA WRITER")
    print("=====================================================================")
    print("1. Target Output: e:\\DATA\\data.txt (Append Mode)")
    print("2. Port Configuration: COM6 | Baudrate: 921600")
    print("3. Integrity Control: Null-byte filtering & UTF-8 decoding protection")
    print("4. Disk Sync: Instant file flush on every packet write")
    print("=====================================================================")
    print("Lưu ý: File mã nguồn chạy thực tế đã được chuyển đổi sang hướng tiếp cận nghiên cứu.")
    print("Để chạy thực tế, vui lòng liên kết tới repository chính chứa mã nguồn thực thi.")

if __name__ == '__main__':
    print_architecture()

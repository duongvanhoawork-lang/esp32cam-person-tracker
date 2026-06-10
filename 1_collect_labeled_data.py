# -*- coding: utf-8 -*-
"""
================================================================================
CÔNG CỤ THU THẬP DỮ LIỆU CSI CÓ NHÃN (9 Ô PHÂN HOẠCH - 1m x 1m)
================================================================================

[HƯỚNG DẪN CÀI ĐẶT THƯ VIỆN]
Mở PowerShell hoặc Command Prompt và chạy lệnh sau (nếu bị lỗi proxy hãy copy y hệt):
$env:NO_PROXY="*"; pip install pyserial

[SƠ ĐỒ BỐ TRÍ THỰC TẾ (Khuyến nghị)]
- Khoảng cách TX đến RX = 5m.
- Vùng nhận diện 3x3m, chia làm 9 ô (mỗi ô 1m x 1m).
- Ô số 5 nằm ở chính giữa (2.5m). Cách TX 1m, cách RX 1m.

[HƯỚNG ĐI VÀ THUẬT TOÁN TRIỂN KHAI]
1. Giao diện lựa chọn vị trí:
   - Yêu cầu người dùng nhập chỉ số Ô không gian cần thu thập dữ liệu (từ 1 đến 9).
   - Kiểm tra tính hợp lệ của đầu vào (Grid Index Validation).
2. Thiết lập thư mục lưu trữ:
   - Tự động tạo thư mục đích lưu trữ dữ liệu nhãn tại: e:\\DATA\\labeled_data\\
   - Định dạng tên file lưu trữ tương ứng với từng ô không gian: grid_{grid_num}.csv
3. Thiết lập kết nối Serial thu nhận dữ liệu:
   - Mở cổng serial COM6 với baudrate 921600. Tắt DTR/RTS để chống reset mạch.
4. Vòng lặp thu nhận & Lưu trữ dữ liệu:
   - Đọc dữ liệu từ bộ đệm. Loại bỏ ký tự null (\x00).
   - Lọc lọc lọc dữ liệu: Chỉ ghi nhận các dòng bắt đầu bằng ký tự đặc trưng "CSI_DATA".
   - Định dạng dòng CSI_DATA hợp lệ được ghi trực tiếp vào tệp CSV đích kèm theo lệnh flush() dữ liệu ngay lập tức.
5. Xử lý ngắt KeyboardInterrupt để lưu file an toàn, đóng cổng serial và thông báo hoàn thành phiên thu thập dữ liệu cho ô hiện hành.
"""

def print_architecture():
    print("=====================================================================")
    print("MÔ TẢ THUẬT TOÁN LABELED CSI DATA ACQUISITION")
    print("=====================================================================")
    print("1. Workspace Spatial Layout: 3x3 Grid (9 Cells, 1m x 1m each)")
    print("2. Serial Ingestion: COM6 @ 921600 baud, non-reset configurations")
    print("3. Target Directory: e:\\DATA\\labeled_data\\grid_{1-9}.csv")
    print("4. Protocol Filter: Line-start prefix matching on 'CSI_DATA'")
    print("=====================================================================")
    print("Lưu ý: File mã nguồn chạy thực tế đã được chuyển đổi sang hướng tiếp cận nghiên cứu.")
    print("Để chạy thực tế, vui lòng liên kết tới repository chính chứa mã nguồn thực thi.")

if __name__ == '__main__':
    print_architecture()

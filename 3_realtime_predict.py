# -*- coding: utf-8 -*-
"""
================================================================================
REAL-TIME PREDICTOR - DỰ ĐOÁN VỊ TRÍ THỜI GIAN THỰC SỬ DỤNG AI TRANSFORMER
================================================================================

[HƯỚNG DẪN CÀI ĐẶT THƯ VIỆN]
    set NO_PROXY=* && pip install torch numpy pyserial

[LƯU Ý KHI CHẠY THỰC TẾ]
- Bộ phát (TX) và bộ thu (RX) phải được cố định cách nhau 5 mét (giống thiết lập lúc huấn luyện).
- Không gian di chuyển (9 ô vật lý, kích thước 1m x 1m mỗi ô) phải giữ nguyên cấu trúc hình học.
- Đảm bảo thiết bị di động kết nối Wi-Fi liên tục để giữ luồng truyền nhận CSI ổn định.

[THAM SỐ CẤU HÌNH HỆ THỐNG]
- Độ dài chuỗi trượt (Sequence Length): 100 mẫu CSI liên tục.
- Số lượng Subcarrier xử lý: 64 subcarriers.
- Đường dẫn Model: e:\\DATA\\transformer_csi_model.pth
- Đường dẫn Scaling: e:\\DATA\\scaler_params.npz (Lưu Mean và Std phục vụ chuẩn hóa Z-score trực tiếp).

[NGƯỠNG QUYẾT ĐỊNH ĐỘ TIN CẬY (CONFIDENCE LOGIC)]
1. Ngưỡng Ngoài Vùng (CONF_OUT_OF_ZONE = 0.40):
   - Nếu xác suất (Probability) của lớp dự đoán cao nhất nhỏ hơn 40%, mô hình sẽ kết luận đối tượng nằm ngoài vùng phủ sóng (Out of zone).
2. Ngưỡng Ranh Giới (CONF_BOUNDARY = 0.06):
   - Tính toán hiệu số xác suất giữa lớp cao thứ nhất và lớp cao thứ hai (p1 - p2).
   - Nếu hiệu số này nhỏ hơn hoặc bằng 6%, hệ thống kết luận đối tượng đang đứng ở ranh giới giữa hai ô không gian này (ví dụ: Giữa ô 2 và ô 3).
   - Nếu hiệu số lớn hơn 6%, kết luận đối tượng nằm hoàn toàn trong ô có xác suất cao nhất.

[KIẾN TRÚC MẠNG AI TRANSFORMER]
- Input Layer: Linear projection biến đổi 64 chiều CSI subcarrier lên d_model (128 chiều).
- Transformer Encoder: 
  - Gồm 3 lớp Encoder Layer ghép nối tiếp.
  - Số đầu chú ý (nhead): 8 heads.
  - Kích thước Feedforward (dim_feedforward): 256.
  - Dropout: 0.2.
- Classification Layer:
  - Input: Trạng thái ẩn của time-step cuối cùng trong sequence (out[:, -1, :]).
  - Cấu trúc Fully Connected Layers: Linear(128 -> 64) -> ReLU -> Dropout -> Linear(64 -> 9 lớp đầu ra đại diện cho 9 ô).

[THUẬT TOÁN HỆ THỐNG RUNTIME]
1. Tải mô hình học máy đã huấn luyện và nạp các tham số Z-score scaler cục bộ.
2. Mở kết nối cổng Serial COM6 nhận dòng CSI trực tiếp từ ESP32 RX.
3. Sử dụng cấu trúc hàng đợi (Queue) kiểu trượt (deque) với kích thước tối đa 100 mẫu.
4. Khi hàng đợi lấp đầy:
   - Áp dụng Z-score Normalization cho toàn chuỗi dựa trên tham số Mean và Std được nạp sẵn.
   - Chuyển đổi chuỗi thành Tensor và đẩy vào thiết bị tính toán (CPU/GPU).
   - Thực thi Feed-forward qua Transformer để lấy phân phối xác suất Softmax.
   - Áp dụng logic so sánh ngưỡng CONF_OUT_OF_ZONE và CONF_BOUNDARY để in kết quả dự đoán thời gian thực.
   - Thực hiện cơ chế trượt cửa sổ 50% (loại bỏ 50 mẫu cũ nhất) để chờ loạt mẫu tiếp theo, giảm trễ tính toán.
"""

def print_architecture():
    print("=====================================================================")
    print("MÔ TẢ THUẬT TOÁN HỆ THỐNG DỰ ĐOÁN THỜI GIAN THỰC (REAL-TIME PREDICTOR)")
    print("=====================================================================")
    print("Model Path        : e:\\DATA\\transformer_csi_model.pth")
    print("Scaler Path       : e:\\DATA\\scaler_params.npz")
    print("Decision Logic    :")
    print("  - If Max Prob < 40% -> Output: 'KHÔNG TRONG VÙNG'")
    print("  - If (Prob_1 - Prob_2) <= 6% -> Output: 'GIỮA Ô A và Ô B'")
    print("  - Else -> Output: 'NẰM TRONG Ô A'")
    print("Sliding Window    : Sequence Length = 100 | Step size = 50 (50% Overlap)")
    print("=====================================================================")
    print("Lưu ý: File mã nguồn chạy thực tế đã được chuyển đổi sang hướng tiếp cận nghiên cứu.")
    print("Để chạy thực tế, vui lòng liên kết tới repository chính chứa mã nguồn thực thi.")

if __name__ == '__main__':
    print_architecture()

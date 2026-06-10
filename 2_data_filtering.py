# -*- coding: utf-8 -*-
"""
================================================================================
DATA FILTERING - BỘ LỌC KHỬ NHIỄU VÀ LÀM MƯỢT TÍN HIỆU CSI 4 TẦNG
================================================================================

[HƯỚNG DẪN CÀI ĐẶT THƯ VIỆN]
  set NO_PROXY=* && pip install numpy scipy

[MÔ TẢ VÀ THAM SỐ CẤU HÌNH BỘ LỌC]
  Đọc toàn bộ file dữ liệu thô grid_1.csv ... grid_9.csv trong thư mục e:\\DATA\\labeled_data\\
  áp dụng chuỗi lọc nhiễu 4 tầng tuần tự, và ghi kết quả ra e:\\DATA\\labeled_data_filtered\\

  Các tầng lọc được áp dụng (theo đúng thứ tự logic):

  1. Hampel Filter (Loại bỏ nhiễu nhọn - Spike / Outlier theo thời gian)
     - Window Size (Cửa sổ tìm kiếm): 10 mẫu lân cận mỗi bên.
     - Sigma threshold (Ngưỡng sigma): 2.0.
     - Cơ chế: Tính toán Median và MAD (Median Absolute Deviation) trong cửa sổ trượt.
       Nếu giá trị vượt quá ngưỡng sigma * MAD, thay thế nó bằng giá trị Median.

  2. IQR Filter (Bộ lọc phân phối thống kê - Interquartile Range)
     - IQR Multiplier (Hệ số nhân): 1.5.
     - Cơ chế: Xác định khoảng biến thiên chuẩn [Q1 - 1.5*IQR, Q3 + 1.5*IQR].
       Các điểm tín hiệu nằm ngoài khoảng này sẽ bị kẹp (clamp/clip) về biên giới hạn.

  3. Butterworth Low-Pass Filter (Bộ lọc thông thấp Butterworth)
     - Cutoff Frequency (Tần số cắt): 0.05 (chuẩn hóa từ 0.0 đến 0.5).
     - Order (Bậc bộ lọc): Bậc 5 (tạo độ dốc suy hao tần số cao tốt).
     - Cơ chế: Lọc hai chiều không lệch pha (filtfilt) để triệt tiêu nhiễu tần số cao
       phát ra từ môi trường và chuyển động không mong muốn.

  4. Savitzky-Golay Filter (Bộ lọc làm mượt giữ đỉnh đặc trưng)
     - Window Length (Độ dài khung nội suy): 21 mẫu (phải là số lẻ).
     - Polyorder (Bậc đa thức khớp): Bậc 3.
     - Cơ chế: Sử dụng phương pháp bình phương tối thiểu để khớp đa thức cục bộ cho tín hiệu,
       giúp đường cong CSI mượt mà nhưng không làm mất đi các đỉnh/đáy đặc trưng.

[HƯỚNG ĐI VÀ LƯU ĐỒ XỬ LÝ DỮ LIỆU]
1. Parse dòng CSI gốc:
   - Trích xuất mảng amplitude từ chuỗi định dạng raw dạng: CSI_DATA,...[subcarriers]
   - Tính toán biên độ sóng Amplitude = sqrt(Real^2 + Imag^2) cho từng subcarrier (64 subcarriers).
2. Xử lý song song ma trận CSI kích thước (N_Samples, 64) qua 4 tầng lọc trên.
3. Tái cấu trúc (reconstruct) dòng dữ liệu thành định dạng gốc kèm mảng amplitude đã lọc.
4. Ghi lại dữ liệu sạch ra tệp tương ứng tại thư mục đích.
"""

def print_architecture():
    print("=====================================================================")
    print("MÔ TẢ THUẬT TOÁN HỆ THỐNG LỌC NHIỄU CSI 4 TẦNG (4-STAGE FILTER PIPELINE)")
    print("=====================================================================")
    print("Input Directory  : e:\\DATA\\labeled_data")
    print("Output Directory : e:\\DATA\\labeled_data_filtered")
    print("Pipeline Stages  :")
    print("  Stage 1. Hampel Filter     -> Local spike & outlier removal via MAD")
    print("  Stage 2. IQR Clamp Filter  -> Statistical boundary clipping (1.5 * IQR)")
    print("  Stage 3. Butterworth LPF   -> Phase-preserving low pass filter (Cutoff: 0.05, Order: 5)")
    print("  Stage 4. Savitzky-Golay    -> Local polynomial smoothing (Window: 21, Poly: 3)")
    print("=====================================================================")
    print("Lưu ý: File mã nguồn chạy thực tế đã được chuyển đổi sang hướng tiếp cận nghiên cứu.")
    print("Để chạy thực tế, vui lòng liên kết tới repository chính chứa mã nguồn thực thi.")

if __name__ == '__main__':
    print_architecture()

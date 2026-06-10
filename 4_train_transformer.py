# -*- coding: utf-8 -*-
"""
================================================================================
TRAIN AI - HUẤN LUYỆN MÔ HÌNH NHẬN DẠNG BẢN ĐỒ KHÔNG GIAN DỰA TRÊN CSI TRANSFORMER
================================================================================

[HƯỚNG DẪN CÀI ĐẶT THƯ VIỆN]
    set NO_PROXY=* && pip install torch numpy

[VỀ MÔ HÌNH TRANSFORMER VÀ PHƯƠNG PHÁP HUẤN LUYỆN]
- Mô hình AI học trực tiếp các "đặc trưng phân tán sóng" (Spatial Propagation Patterns)
  từ các tín hiệu CSI thu được trong thư mục labeled_data.
- Mô hình không cần biết thông số vật lý (như khoảng cách 5m hay diện tích 1m vuông của các ô).
- Để đạt độ chính xác cao (>80%), mỗi ô không gian cần tối thiểu 5 - 10 phút dữ liệu thô
  chứa nhiều tư thế hoạt động đa dạng (đứng, ngồi, di động, xoay người).

[THÔNG SỐ HUẤN LUYỆN (HYPERPARAMETERS)]
- Số lượng Epoch (Chu kỳ): 20 epochs.
- Batch Size (Kích thước lô): 64 mẫu/lô.
- Tốc độ học ban đầu (Learning Rate): 0.0005.
- Kích thước cửa sổ dữ liệu (Sequence Length): 100 mẫu.
- Số lượng Subcarrier (Chiều đầu vào): 64 subcarriers.
- Hàm mất mát: CrossEntropyLoss (áp dụng cho phân loại 9 lớp ô không gian).
- Thuật toán tối ưu: Adam Optimizer.
- Cơ chế kiểm soát tốc độ học: ReduceLROnPlateau (giảm tốc độ học đi 50% nếu loss của tập train không giảm sau 5 epochs).

[HƯỚNG ĐI VÀ LƯU ĐỒ PIPELINE TRAIN]
1. Đọc và tải dữ liệu (Load Dataset):
   - Đọc các tệp dữ liệu sạch từ thư mục e:\\DATA\\labeled_data_filtered\\ (grid_{1-9}.csv).
   - Biến đổi dữ liệu sang dạng amplitude.
   - Áp dụng kỹ thuật Cửa sổ trượt (Sliding Window) với bước nhảy trượt (step = 25 mẫu) để tăng cường dữ liệu (Data Augmentation) bằng cách tạo các mẫu đè nhau 75% (Overlap).
2. Chuẩn hóa dữ liệu (Z-score Normalization):
   - Tính toán giá trị Mean và Standard Deviation (Std) trên toàn bộ tập dữ liệu huấn luyện.
   - Lưu trữ các tham số chuẩn hóa này ra file e:\\DATA\\scaler_params.npz để phục vụ cho tiền xử lý thời gian thực sau này.
3. Phân chia Lô và đưa vào DataLoader:
   - Đóng gói chuỗi CSI kích thước (Batch_Size, Sequence_Length, 64) kèm theo Nhãn lớp (0-8 tương ứng ô 1-9).
4. Huấn luyện mạng Neural Network (CSITransformer):
   - Feed forward dữ liệu qua Linear Projection -> Multi-Head Self-Attention (Transformer Encoder) -> Classifier.
   - Tính toán loss, lan truyền ngược (backward) để cập nhật trọng số.
   - Theo dõi độ chính xác (Accuracy %) sau mỗi epoch và lưu trạng thái mô hình tốt nhất (Best weights) vào tệp e:\\DATA\\transformer_csi_model.pth.
"""

def print_architecture():
    print("=====================================================================")
    print("MÔ TẢ THUẬT TOÁN HUẤN LUYỆN MÔ HÌNH TRANSFORMER AI (TRAINING PIPELINE)")
    print("=====================================================================")
    print("Dataset Directory : e:\\DATA\\labeled_data")
    print("Model Output Path : e:\\DATA\\transformer_csi_model.pth")
    print("Scaler Param Path : e:\\DATA\\scaler_params.npz")
    print("Hyperparameters   :")
    print("  - Sequence Length : 100 samples")
    print("  - Augmentation    : Sliding Window with step = 25 (75% Overlap)")
    print("  - Epochs / Batch  : 20 epochs / Batch size 64")
    print("  - Optimization    : Adam (LR: 0.0005) with ReduceLROnPlateau (Factor: 0.5, Patience: 5)")
    print("=====================================================================")
    print("Lưu ý: File mã nguồn chạy thực tế đã được chuyển đổi sang hướng tiếp cận nghiên cứu.")
    print("Để chạy thực tế, vui lòng liên kết tới repository chính chứa mã nguồn thực thi.")

if __name__ == '__main__':
    print_architecture()

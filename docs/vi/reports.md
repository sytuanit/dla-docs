# Báo cáo

## 1. Mục đích

Module **Báo cáo** cung cấp các báo cáo tài chính chi tiết, giúp bạn:
- Xem tổng quan tài chính tháng hiện tại
- Phân tích thu nhập và chi tiêu
- Theo dõi tiến độ tiết kiệm
- Dự báo chi tiêu cuối tháng
- Xem báo cáo theo từng loại (Thu nhập, Chi tiêu, Tiết kiệm, Khoản vay)

## 2. Khi nào nên dùng

Sử dụng module này khi bạn muốn:
- Xem tổng quan tài chính
- Phân tích xu hướng chi tiêu
- Kiểm tra tiến độ đạt mục tiêu tiết kiệm
- Dự báo khả năng vượt ngân sách
- Xem báo cáo chi tiết theo từng loại

## 3. Các màn hình liên quan

- Báo cáo tổng quan
- Báo cáo thu nhập
- Báo cáo chi tiêu
- Báo cáo tiết kiệm
- Báo cáo khoản vay

## 4. Cách sử dụng chính

### 4.1 Xem báo cáo tổng quan

1. Vào tab **Báo cáo** ở bottom navigation
2. Xem các thông tin:
   - **Tổng quan tài chính**: Thu nhập, chi tiêu, tiết kiệm
   - **Tiến độ tiết kiệm**: % đạt mục tiêu
   - **Dự báo cuối tháng**: Chi tiêu dự kiến
   - **Phân tích theo danh mục**: Top danh mục chi tiêu nhiều nhất

### 4.2 Xem báo cáo thu nhập

1. Vào **Báo cáo** → Chọn **Báo cáo thu nhập**
2. Xem:
   - Tổng thu nhập trong tháng
   - Phân tích theo nguồn (Thu nhập định kỳ, Thu nhập thêm)
   - Biểu đồ xu hướng

### 4.3 Xem báo cáo chi tiêu

1. Vào **Báo cáo** → Chọn **Báo cáo chi tiêu**
2. Xem:
   - Tổng chi tiêu trong tháng
   - Phân tích theo danh mục
   - So sánh với tháng trước

### 4.4 Xem báo cáo tiết kiệm

1. Vào **Báo cáo** → Chọn **Báo cáo tiết kiệm**
2. Xem:
   - Tổng số dư tiết kiệm
   - Lãi dự kiến
   - Danh sách tài khoản

### 4.5 Xem báo cáo khoản vay

1. Vào **Báo cáo** → Chọn **Báo cáo khoản vay**
2. Xem:
   - Tổng nợ còn lại
   - Số tiền trả trong tháng
   - Lịch trả nợ

## 5. Minh hoạ giao diện (Wireframe)

### 5.1 Màn hình Báo cáo tổng quan

```text
┌─────────────────────────────────────────┐
│  Báo cáo                                │
├─────────────────────────────────────────┤
│  Tháng 11/2024                          │
│                                         │
│  ┌───────────────────────────────────┐ │
│  │ Tổng quan tài chính                 │ │
│  │                                     │ │
│  │ Thu nhập: 12,000,000 đ              │ │
│  │ Chi tiêu: 7,500,000 đ               │ │
│  │ Tiết kiệm: 2,400,000 đ              │ │
│  │                                     │ │
│  │ Dòng tiền ròng: +4,500,000 đ       │ │
│  └───────────────────────────────────┘ │
│                                         │
│  ┌───────────────────────────────────┐ │
│  │ Tiến độ tiết kiệm                   │ │
│  │                                     │ │
│  │ Mục tiêu: 2,400,000 đ               │ │
│  │ Thực tế: 2,400,000 đ                │ │
│  │                                     │ │
│  │ [████████████] 100%                 │ │
│  │ ✅ Đạt mục tiêu                     │ │
│  └───────────────────────────────────┘ │
│                                         │
│  ┌───────────────────────────────────┐ │
│  │ Dự báo cuối tháng                   │ │
│  │                                     │ │
│  │ Chi tiêu dự kiến: 9,000,000 đ      │ │
│  │ Còn lại: 3,000,000 đ                │ │
│  │                                     │ │
│  │ Rủi ro vượt ngân sách: Thấp        │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Phân tích theo danh mục                │
│  ┌───────────────────────────────────┐ │
│  │ 1. Ăn ngoài: 800,000 đ (32%)       │ │
│  │ 2. Mua sắm: 500,000 đ (20%)       │ │
│  │ 3. Giao thông: 300,000 đ (12%)    │ │
│  └───────────────────────────────────┘ │
│                                         │
│  [Báo cáo thu nhập] [Báo cáo chi tiêu] │
│  [Báo cáo tiết kiệm] [Báo cáo khoản vay]│
└─────────────────────────────────────────┘
```

## 6. Logic & quy tắc

### 6.1 Tính toán dòng tiền ròng

- Dòng tiền ròng = Thu nhập - Chi tiêu - Tiết kiệm
- Giá trị dương = Còn dư, Giá trị âm = Thiếu hụt

### 6.2 Tiến độ tiết kiệm

- So sánh tiết kiệm thực tế với mục tiêu trong ngân sách
- Hiển thị % đạt mục tiêu và mức độ (Tốt / Trung bình / Kém)

### 6.3 Dự báo cuối tháng

- Dựa trên chi tiêu trung bình/ngày và số ngày còn lại
- Tính cả chi tiêu cố định chưa thanh toán và khoản vay chưa trả

### 6.4 Rủi ro vượt ngân sách

- **Đang đúng hướng**: Chi tiêu < 70% ngân sách
- **Rủi ro thấp**: Chi tiêu 70-85% ngân sách
- **Rủi ro trung bình**: Chi tiêu 85-95% ngân sách
- **Rủi ro cao**: Chi tiêu > 95% ngân sách

## 7. Lưu ý quan trọng

- **Dữ liệu tháng hiện tại**: Báo cáo chỉ hiển thị dữ liệu tháng hiện tại
- **Cần có ngân sách**: Một số báo cáo yêu cầu đã lập ngân sách
- **Dự báo chỉ mang tính tham khảo**: Dựa trên xu hướng hiện tại

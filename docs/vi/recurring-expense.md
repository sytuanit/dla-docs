# Chi tiêu cố định

## 1. Mục đích

Module **Chi tiêu cố định** giúp bạn quản lý các khoản chi tiêu định kỳ, có chu kỳ cố định như:
- Tiền điện, nước, gas
- Internet, cáp TV
- Bảo hiểm
- Học phí
- Tiền thuê nhà
- Các khoản chi tiêu định kỳ khác

Module này tự động tạo các **kỳ phát sinh** (occurrences) dựa trên chu kỳ bạn đã cấu hình, và nhắc nhở bạn khi đến kỳ thanh toán.

## 2. Khi nào nên dùng

Sử dụng module này khi bạn có:
- Chi tiêu cố định theo chu kỳ (hàng tuần, 2 tuần, hoặc hàng tháng)
- Cần theo dõi và xác nhận khi đã thanh toán
- Muốn tự động tính toán vào ngân sách hàng tháng

## 3. Các màn hình liên quan

- Danh sách chi tiêu cố định
- Thêm chi tiêu cố định mới
- Sửa chi tiêu cố định
- Lịch sử các kỳ phát sinh

## 4. Cách sử dụng chính

### 4.1 Thêm chi tiêu cố định mới

1. Vào **Chức năng** → Chọn **Chi tiêu cố định**
2. Nhấn nút **+** (FAB) ở góc dưới bên phải
3. Điền thông tin:
   - **Danh mục**: Chọn hoặc tạo danh mục mới
   - **Số tiền**: Nhập số tiền chi tiêu (có thể để trống, nhập sau khi xác nhận)
   - **Chu kỳ**: Chọn Hàng tuần / 2 tuần / Hàng tháng
   - **Ngày**: Chọn ngày trong chu kỳ (ví dụ: ngày 15 hàng tháng)
   - **Ngày bắt đầu**: (Chỉ cho chu kỳ 2 tuần) Chọn ngày bắt đầu thanh toán
   - **Ghi chú**: Thông tin bổ sung (tùy chọn)
4. Nhấn **Lưu**

### 4.2 Xác nhận đã thanh toán

1. Vào danh sách chi tiêu cố định
2. Tìm item có badge **"Chờ xác nhận"** (màu vàng)
3. Nhấn vào item để mở dialog xác nhận
4. Điền:
   - **Số tiền thực tế**: (nếu khác với dự kiến)
   - **Ghi chú**: (tùy chọn)
5. Nhấn **Xác nhận**

### 4.3 Sửa chi tiêu cố định

1. Vào danh sách chi tiêu cố định
2. Nhấn vào item cần sửa
3. Chọn **Sửa** từ menu
4. Cập nhật thông tin
5. Nhấn **Lưu**

### 4.4 Xem lịch sử

1. Vào danh sách chi tiêu cố định
2. Nhấn vào item
3. Chọn **Lịch sử** để xem tất cả các kỳ phát sinh đã qua

### 4.5 Tắt/Bật chi tiêu

1. Vào danh sách chi tiêu cố định
2. Tìm item cần tắt/bật
3. Bật/tắt switch **Hoạt động** ở bên phải item

## 5. Minh hoạ giao diện (Wireframe)

### 5.1 Màn hình Danh sách

```text
┌─────────────────────────────────────────┐
│  ← Quay lại    Chi tiêu cố định         │
├─────────────────────────────────────────┤
│  [🔍 Tìm kiếm...]                        │
│  [Tất cả ▼] [Chờ xác nhận] [Đã xác nhận]│
├─────────────────────────────────────────┤
│  ┌───────────────────────────────────┐ │
│  │ Tiền điện          [Hoạt động]     │ │
│  │ 500,000 đ                         │ │
│  │ Hàng tháng - Ngày 15              │ │
│  │ Kỳ tiếp theo: 15/12/2024         │ │
│  │ [Chờ xác nhận]                    │ │
│  │                                    │ │
│  │ [Sửa] [Lịch sử] [Xóa]             │ │
│  └───────────────────────────────────┘ │
│                                         │
│  ┌───────────────────────────────────┐ │
│  │ Tiền nước          [Hoạt động]     │ │
│  │ 200,000 đ                         │ │
│  │ Hàng tháng - Ngày 10              │ │
│  │ Kỳ tiếp theo: 10/12/2024         │ │
│  │ [Đã xác nhận]                     │ │
│  │                                    │ │
│  │ [Sửa] [Lịch sử] [Xóa]             │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Tổng: 700,000 đ/tháng                 │
├─────────────────────────────────────────┤
│                                    [+]   │
└─────────────────────────────────────────┘
```

### 5.2 Màn hình Thêm/Sửa

```text
┌─────────────────────────────────────────┐
│  ← Quay lại    Thêm chi tiêu cố định    │
├─────────────────────────────────────────┤
│  Danh mục *                              │
│  [Tiền điện ▼]                           │
│                                         │
│  Số tiền                                 │
│  [500,000] đ                             │
│  (Có thể để trống, nhập khi xác nhận)   │
│                                         │
│  Chu kỳ *                                │
│  ○ Hàng tuần                             │
│  ● Hàng tháng                            │
│  ○ 2 tuần                                │
│                                         │
│  Ngày *                                  │
│  [15]                                    │
│  (1-31 cho hàng tháng, 1-7 cho hàng tuần)│
│                                         │
│  Ngày bắt đầu                            │
│  [15/11/2024]                            │
│  (Chỉ cho chu kỳ 2 tuần)                │
│                                         │
│  Ghi chú                                 │
│  [Tiền điện tháng 11/2024]               │
│                                         │
│  [Lưu] [Hủy]                            │
└─────────────────────────────────────────┘
```

## 6. Logic & quy tắc

### 6.1 Chu kỳ và Ngày

- **Hàng tuần**: Chọn ngày trong tuần (1=Thứ 2, 7=Chủ nhật)
- **2 tuần**: Chọn ngày trong tuần + ngày bắt đầu cụ thể
- **Hàng tháng**: Chọn ngày trong tháng (1-31)

### 6.2 Tự động tạo kỳ phát sinh

- App tự động tạo **occurrence** (kỳ phát sinh) khi:
  - Thêm chi tiêu mới
  - Đến ngày trong chu kỳ
  - Tháng mới bắt đầu

### 6.3 Trạng thái kỳ phát sinh

- **PENDING**: Chờ xác nhận (hiển thị badge vàng)
- **COMPLETED**: Đã xác nhận (hiển thị badge xanh)
- **CANCELLED**: Đã hủy (hiển thị badge đỏ)

### 6.4 Tích hợp với Ngân sách

- Khi xác nhận chi tiêu, app tự động cập nhật ngân sách tháng hiện tại (nếu có)
- Chi tiêu được tính vào "Chi tiêu cố định" trong ngân sách

### 6.5 Thông báo

- App gửi thông báo nhắc nhở khi đến kỳ thanh toán
- Thời gian thông báo có thể cấu hình cho từng khoản (`notificationTime1`, `notificationTime2`, mặc định 16:00 và 19:00)

## 7. Lưu ý quan trọng

- **Số tiền có thể để trống**: Nếu bạn chưa biết chính xác số tiền, có thể để trống và nhập khi xác nhận
- **Không thể xóa khi đã có occurrence**: Nếu đã có kỳ phát sinh, bạn chỉ có thể tắt (isActive = false), không thể xóa
- **Xác nhận muộn**: Bạn có thể xác nhận các kỳ đã qua, app sẽ tự động tính lại ngân sách
- **Thay đổi chu kỳ**: Khi sửa chu kỳ, các occurrence tương lai sẽ được tính lại

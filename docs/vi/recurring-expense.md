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

## 5. Ví dụ & minh hoạ giao diện

### 5.1 Ví dụ 1: Tạo chi tiêu cố định hàng tháng (tiền điện)

**Tình huống**: Bạn muốn theo dõi tiền điện hàng tháng để app tự động nhắc nhở khi đến kỳ thanh toán.

**Thực hiện**:
1. Vào màn hình Chức năng, chọn "Chi tiêu cố định"
2. Nhấn nút "➕ Thêm mới" ở góc dưới bên phải
3. Chọn danh mục "Tiền điện" (hoặc tạo mới nếu chưa có)
4. Nhập số tiền: 500.000
5. Chọn chu kỳ "Tháng"
6. Chọn "Chọn ngày trong tháng", nhập số 15
7. Ghi chú tự động điền "Tiền điện hàng tháng" (có thể chỉnh sửa)
8. Nhấn "Lưu"

**Kết quả**: App hiển thị thông báo thành công và quay về danh sách. Item mới xuất hiện với thông tin đầy đủ, và app sẽ tự động nhắc nhở khi đến ngày 15 hàng tháng.

**Màn hình Thêm chi tiêu cố định**:

```text
┌─────────────────────────────────────────┐
│  ← Quay lại    Thêm chi tiêu cố định    │
├─────────────────────────────────────────┤
│  Danh mục *                              │
│  [Tiền điện ▼] [+ Thêm mới]            │
│                                         │
│  Số tiền (VND) *                         │
│  [500.000]                              │
│                                         │
│  Chu kỳ *                                │
│  ┌──────┐ ┌────────┐ ┌────────┐        │
│  │Tuần  │ │2 tuần  │ │Tháng │        │
│  └──────┘ └────────┘ └────────┘        │
│                                         │
│  Ngày chi trong chu kỳ                  │
│  ⚪ Cuối tháng                           │
│  ⚫ Chọn ngày trong tháng                │
│  ┌───────────────────────────────────┐ │
│  │ Ngày trong tháng: [15]            │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Ghi chú                                 │
│  ┌───────────────────────────────────┐ │
│  │ Tiền điện hàng tháng               │ │
│  └───────────────────────────────────┘ │
│                                         │
│  [Hủy]                    [Lưu]        │
└─────────────────────────────────────────┘
```

---

### 5.2 Ví dụ 2: Xác nhận chi tiêu đến hạn và cập nhật số tiền thực tế

**Tình huống**: Đã đến ngày thanh toán tiền nước (ngày 10), nhưng số tiền thực tế phải trả là 180.000 (giảm) thay vì 200.000 như đã đặt.

**Thực hiện**:
1. Mở app hoặc vào màn hình "Chi tiêu cố định"
2. App tự động phát hiện có kỳ đến hạn và hiển thị dialog xác nhận
3. Dialog hiển thị số tiền mặc định: 200.000
4. Cập nhật số tiền thực tế thành 180.000
5. Nhập ghi chú: "Tháng này tiết kiệm nước" (tùy chọn)
6. Nhấn "Xác nhận đã chi"

**Kết quả**: App cập nhật kỳ vừa xác nhận với số tiền thực tế 180.000, tự động tạo kỳ tiếp theo, và cập nhật số dư tài chính hiện tại (trừ 180.000).

**Dialog Xác nhận chi tiêu**:

```text
┌─────────────────────────────────────────┐
│  Xác nhận đã chi                         │
├─────────────────────────────────────────┤
│  Tiền nước                               │
│  Hàng tháng (ngày 10)                   │
│  Ngày đến hạn: Hôm nay                  │
│                                         │
│  Số tiền thực tế *                       │
│  [180.000] đ                            │
│                                         │
│  Ghi chú                                 │
│  [Tháng này tiết kiệm nước]             │
│                                         │
│  [Hủy kỳ này]    [Xác nhận đã chi]      │
└─────────────────────────────────────────┘
```

---

### 5.3 Ví dụ 3: Tạm ngưng chi tiêu cố định khi không còn áp dụng

**Tình huống**: Bạn tạm thời không thuê nhà trong 2 tháng, nên muốn tạm ngưng khoản chi tiêu "Tiền thuê nhà" thay vì xóa hoàn toàn.

**Thực hiện**:
1. Vào màn hình "Chi tiêu cố định"
2. Tìm khoản "Tiền thuê nhà" trong danh sách
3. Nhấn vào công tắc "Hoạt động" ở bên phải item
4. App hiển thị dialog xác nhận: "Bạn có chắc muốn tạm ngưng khoản chi tiêu này?"
5. Nhấn nút "Tạm ngưng" để xác nhận

**Kết quả**: Card "Tiền thuê nhà" chuyển sang trạng thái "Tạm ngưng" (màu xám), công tắc chuyển sang "Inactive". App không còn tạo kỳ mới cho khoản chi tiêu này. Bạn có thể bật lại bằng cách nhấn công tắc "Inactive" → "Active".

**Màn hình Danh sách với công tắc**:

```text
┌─────────────────────────────────────────┐
│  ← Quay lại    Chi tiêu cố định         │
├─────────────────────────────────────────┤
│  ┌───────────────────────────────────┐ │
│  │ Tiền thuê nhà      [⚪ Inactive] │ │
│  │ 3.000.000 đ                      │ │
│  │ Hàng tháng - Ngày 1              │ │
│  │ (Đã tạm ngưng)                   │ │
│  │                                    │ │
│  │ [Sửa] [Lịch sử] [Xóa]             │ │
│  └───────────────────────────────────┘ │
└─────────────────────────────────────────┘
```

---

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

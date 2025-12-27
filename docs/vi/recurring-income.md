# Thu nhập định kỳ

## 1. Mục đích

Module **Thu nhập định kỳ** giúp bạn quản lý các nguồn thu nhập thường xuyên như:
- Lương hàng tháng
- Tiền cho thuê nhà
- Lương hưu
- Cổ tức đầu tư
- Các khoản thu nhập khác có tính chu kỳ

Module này tự động tạo các **kỳ phát sinh** (occurrences) dựa trên chu kỳ bạn đã cấu hình, và nhắc nhở bạn khi đến kỳ nhận tiền.

## 2. Khi nào nên dùng

Sử dụng module này khi bạn có:
- Thu nhập cố định theo chu kỳ (hàng tuần, 2 tuần, hoặc hàng tháng)
- Cần theo dõi và xác nhận khi đã nhận tiền
- Muốn tự động tính toán vào ngân sách hàng tháng

## 3. Các màn hình liên quan

- Danh sách thu nhập định kỳ
- Thêm thu nhập định kỳ mới
- Sửa thu nhập định kỳ
- Lịch sử các kỳ phát sinh

## 4. Cách sử dụng chính

### 4.1 Thêm thu nhập định kỳ mới

1. Vào **Chức năng** → Chọn **Thu nhập định kỳ**
2. Nhấn nút **+** (FAB) ở góc dưới bên phải
3. Điền thông tin:
   - **Danh mục**: Chọn hoặc tạo danh mục mới
   - **Số tiền**: Nhập số tiền thu nhập (có thể để trống, nhập sau khi xác nhận)
   - **Chu kỳ**: Chọn Hàng tuần / 2 tuần / Hàng tháng
   - **Ngày**: Chọn ngày trong chu kỳ (ví dụ: ngày 15 hàng tháng)
   - **Ngày bắt đầu**: (Chỉ cho chu kỳ 2 tuần) Chọn ngày bắt đầu nhận
   - **Ghi chú**: Thông tin bổ sung (tùy chọn)
4. Nhấn **Lưu**

### 4.2 Xác nhận đã nhận tiền

1. Vào danh sách thu nhập định kỳ
2. Tìm item có badge **"Chờ xác nhận"** (màu vàng)
3. Nhấn vào item để mở dialog xác nhận
4. Điền:
   - **Số tiền thực tế**: (nếu khác với dự kiến)
   - **Ghi chú**: (tùy chọn)
5. Nhấn **Xác nhận**

### 4.3 Sửa thu nhập định kỳ

1. Vào danh sách thu nhập định kỳ
2. Nhấn vào item cần sửa
3. Chọn **Sửa** từ menu
4. Cập nhật thông tin
5. Nhấn **Lưu**

### 4.4 Xem lịch sử

1. Vào danh sách thu nhập định kỳ
2. Nhấn vào item
3. Chọn **Lịch sử** để xem tất cả các kỳ phát sinh đã qua

### 4.5 Tắt/Bật thu nhập

1. Vào danh sách thu nhập định kỳ
2. Tìm item cần tắt/bật
3. Bật/tắt switch **Hoạt động** ở bên phải item

## 5. Ví dụ & minh hoạ giao diện

### 5.1 Ví dụ 1: Tạo thu nhập định kỳ hàng tháng (lương)

**Tình huống**: Bạn muốn theo dõi lương hàng tháng để app tự động nhắc nhở khi đến kỳ nhận tiền.

**Thực hiện**:
1. Vào màn hình Chức năng, chọn "Thu nhập định kỳ"
2. Nhấn nút "➕ Thêm mới" ở góc dưới bên phải
3. Chọn danh mục "Lương" (hoặc tạo mới nếu chưa có)
4. Nhập số tiền: 10.000.000
5. Chọn chu kỳ "Tháng"
6. Chọn "Chọn ngày trong tháng", nhập số 5
7. Ghi chú tự động điền "Lương hàng tháng" (có thể chỉnh sửa)
8. Nhấn "Lưu"

**Kết quả**: App hiển thị thông báo thành công và quay về danh sách. Item mới xuất hiện với thông tin đầy đủ, và app sẽ tự động nhắc nhở khi đến ngày 5 hàng tháng.

**Màn hình Thêm thu nhập định kỳ**:

```text
┌─────────────────────────────────────────┐
│  ← Quay lại    Thêm thu nhập định kỳ     │
├─────────────────────────────────────────┤
│  Danh mục *                              │
│  [Lương ▼] [+ Thêm mới]                 │
│                                         │
│  Số tiền (VND) *                         │
│  [10.000.000]                           │
│                                         │
│  Chu kỳ *                                │
│  ┌──────┐ ┌────────┐ ┌────────┐        │
│  │Tuần  │ │2 tuần  │ │Tháng │        │
│  └──────┘ └────────┘ └────────┘        │
│                                         │
│  Ngày nhận trong chu kỳ                  │
│  ⚪ Cuối tháng                           │
│  ⚫ Chọn ngày trong tháng                │
│  ┌───────────────────────────────────┐ │
│  │ Ngày trong tháng: [5]             │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Ghi chú                                 │
│  ┌───────────────────────────────────┐ │
│  │ Lương hàng tháng                   │ │
│  └───────────────────────────────────┘ │
│                                         │
│  [Hủy]                    [Lưu]        │
└─────────────────────────────────────────┘
```

---

### 5.2 Ví dụ 2: Xác nhận thu nhập đến hạn và cập nhật số tiền thực tế

**Tình huống**: Đã đến ngày nhận lương (ngày 5), nhưng số tiền thực tế nhận được là 10.500.000 (tăng lương) thay vì 10.000.000 như đã đặt.

**Thực hiện**:
1. Mở app hoặc vào màn hình "Thu nhập định kỳ"
2. App tự động phát hiện có kỳ đến hạn và hiển thị dialog xác nhận
3. Dialog hiển thị số tiền mặc định: 10.000.000
4. Cập nhật số tiền thực tế thành 10.500.000
5. Nhập ghi chú: "Lương tháng này có thưởng" (tùy chọn)
6. Nhấn "Xác nhận đã nhận"

**Kết quả**: App cập nhật kỳ vừa xác nhận với số tiền thực tế 10.500.000, tự động tạo kỳ tiếp theo, và cập nhật số dư tài chính hiện tại.

**Dialog Xác nhận thu nhập**:

```text
┌─────────────────────────────────────────┐
│  Xác nhận đã nhận                        │
├─────────────────────────────────────────┤
│  Lương                                   │
│  Hàng tháng (ngày 5)                    │
│  Ngày đến hạn: Hôm nay                  │
│                                         │
│  Số tiền thực tế *                       │
│  [10.500.000] đ                         │
│                                         │
│  Ghi chú                                 │
│  [Lương tháng này có thưởng]            │
│                                         │
│  [Hủy kỳ này]    [Xác nhận đã nhận]    │
└─────────────────────────────────────────┘
```

---

### 5.3 Ví dụ 3: Hủy kỳ thu nhập khi không nhận được tiền

**Tình huống**: Đã đến ngày nhận tiền thuê nhà (ngày 1), nhưng khách thuê chưa chuyển khoản nên không nhận được tiền.

**Thực hiện**:
1. Mở app hoặc vào màn hình "Thu nhập định kỳ"
2. App hiển thị dialog xác nhận cho kỳ đến hạn
3. Nhấn nút "Hủy kỳ này"
4. Nhập lý do: "Khách thuê chưa chuyển khoản" (bắt buộc)
5. Nhấn "Xác nhận hủy"

**Kết quả**: Kỳ vừa hủy chuyển sang trạng thái "Huỷ", hiển thị lý do hủy, và app tự động tạo kỳ tiếp theo. Số dư tài chính không thay đổi vì không nhận được tiền.

**Dialog Hủy kỳ thu nhập**:

```text
┌─────────────────────────────────────────┐
│  Hủy kỳ này                              │
├─────────────────────────────────────────┤
│  Tiền thuê nhà                           │
│  Hàng tháng (ngày 1)                    │
│  Ngày đến hạn: Hôm nay                  │
│                                         │
│  Lý do hủy *                             │
│  ┌───────────────────────────────────┐ │
│  │ Khách thuê chưa chuyển khoản      │ │
│  └───────────────────────────────────┘ │
│                                         │
│  [Quay lại]        [Xác nhận hủy]      │
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
  - Thêm thu nhập mới
  - Đến ngày trong chu kỳ
  - Tháng mới bắt đầu

### 6.3 Trạng thái kỳ phát sinh

- **PENDING**: Chờ xác nhận (hiển thị badge vàng)
- **COMPLETED**: Đã xác nhận (hiển thị badge xanh)
- **CANCELLED**: Đã hủy (hiển thị badge đỏ)

### 6.4 Tích hợp với Ngân sách

- Khi xác nhận thu nhập, app tự động cập nhật ngân sách tháng hiện tại (nếu có)
- Thu nhập được tính vào "Thu nhập định kỳ" trong ngân sách

### 6.5 Thông báo

- App gửi thông báo nhắc nhở khi đến kỳ nhận tiền
- Thời gian thông báo có thể cấu hình cho từng khoản (`notificationTime1`, `notificationTime2`, mặc định 16:00 và 19:00)

## 7. Lưu ý quan trọng

- **Số tiền có thể để trống**: Nếu bạn chưa biết chính xác số tiền, có thể để trống và nhập khi xác nhận
- **Không thể xóa khi đã có occurrence**: Nếu đã có kỳ phát sinh, bạn chỉ có thể tắt (isActive = false), không thể xóa
- **Xác nhận muộn**: Bạn có thể xác nhận các kỳ đã qua, app sẽ tự động tính lại ngân sách
- **Thay đổi chu kỳ**: Khi sửa chu kỳ, các occurrence tương lai sẽ được tính lại

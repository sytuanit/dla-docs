# Tiết kiệm

## 1. Mục đích

Module **Tiết kiệm** giúp bạn quản lý các tài khoản tiết kiệm tại ngân hàng, theo dõi số dư, lãi suất, và kỳ hạn. Module này hỗ trợ:
- Quản lý nhiều tài khoản tiết kiệm
- Theo dõi lãi suất và kỳ hạn
- Tự động tính lãi khi đến kỳ đáo hạn
- Rút tiền trước hạn (nếu cần)
- Gia hạn (rollover) tài khoản

## 2. Khi nào nên dùng

Sử dụng module này khi bạn có:
- Tài khoản tiết kiệm tại ngân hàng
- Cần theo dõi số dư và lãi suất
- Muốn nhắc nhở khi đến kỳ đáo hạn
- Cần quản lý nhiều tài khoản tiết kiệm

## 3. Các màn hình liên quan

- Danh sách tài khoản tiết kiệm
- Thêm tài khoản mới
- Sửa tài khoản
- Chi tiết tài khoản
- Rút tiền trước hạn

## 4. Cách sử dụng chính

### 4.1 Tạo sổ tiết kiệm mới

1. Vào **Chức năng** → Chọn **Tiết kiệm ngân hàng**
2. Nhấn nút **+** (FAB) ở góc dưới bên phải
3. Xem "Tổng tiền hiện có" (có thể click để xem chi tiết)
4. Chọn ngân hàng:
   - Nếu đã có: Chọn từ dropdown
   - Nếu chưa có: Nhấn nút "+" để tạo ngân hàng mới
5. Nhập số tiền gửi (phải ≤ Tổng tiền hiện có)
6. Nhập kỳ hạn: 1-36 tháng
7. Nhập lãi suất: %/năm (1-100%)
8. Chọn ngày bắt đầu (mặc định là hôm nay, có thể chọn từ tháng trước đến hiện tại)
9. Xem ngày đáo hạn tự động tính (từ ngày bắt đầu + kỳ hạn)
10. Chọn kế hoạch khi đáo hạn:
    - Tất toán cả gốc và lãi (mặc định)
    - Tái tục GỐC (lãi về tài khoản)
    - Tái tục GỐC + LÃI
11. (Tùy chọn) Nhập ghi chú
12. (Tùy chọn) Chọn thời gian thông báo (mặc định: 10:00 và 19:00)
13. Nhấn **TẠO SỔ**

### 4.2 Xem danh sách và chi tiết sổ tiết kiệm

1. Vào **Chức năng** → Chọn **Tiết kiệm ngân hàng**
2. Xem màn hình "Danh sách sổ tiết kiệm" với filter mặc định "Đang gửi"
3. Xem Card tổng quan:
   - Filter "Đang gửi": Số dư hiện có, Tiền đang gửi TK, Lãi dự kiến, Lãi tháng này
   - Filter "Đã tất toán": Tổng tiền đã tất toán, Lãi đã nhận
4. (Tùy chọn) Sử dụng thanh tìm kiếm để tìm sổ theo tên ngân hàng hoặc mã ngân hàng
5. Chuyển filter giữa "Đang gửi" và "Đã tất toán"
6. Nhấn vào một sổ tiết kiệm để xem chi tiết:
   - Thông tin sổ: Ngân hàng, Kỳ hạn, Lãi suất, Số tiền gửi, Lãi tạm tính
   - Ngày bắt đầu và ngày đáo hạn
   - Trạng thái: Đang gửi
   - Kế hoạch khi đáo hạn
   - (Nếu có) Lịch sử tái tục
   - Nút "TẤT TOÁN" (nếu đang gửi)

### 4.3 Tất toán sổ tiết kiệm

1. Vào danh sách sổ tiết kiệm, tìm sổ đã đến hoặc quá ngày đáo hạn
2. Nhấn nút **TẤT TOÁN** trên card (hoặc vào chi tiết rồi nhấn "TẤT TOÁN")
3. Xem dialog "TẤT TOÁN SỔ TIẾT KIỆM" với:
   - Thông tin sổ: Ngân hàng, Số tiền gửi, Kỳ hạn, Lãi suất
   - Ngày tất toán (mặc định = ngày đáo hạn, có thể chọn ngày khác)
   - Lãi nhận được (mặc định = lãi tạm tính, có thể chỉnh sửa)
   - Tổng nhận (tự động tính = gốc + lãi)
4. (Tùy chọn) Chỉnh sửa ngày tất toán hoặc lãi nhận được
5. Nhấn **XÁC NHẬN**

### 4.4 Tái tục sổ tiết kiệm

1. Vào danh sách sổ tiết kiệm, tìm sổ đã đến ngày đáo hạn với kế hoạch "Tái tục GỐC" hoặc "Tái tục GỐC + LÃI"
2. Nhấn nút **TÁI TỤC** hoặc "Tái tục theo kế hoạch"
3. Xem dialog "TÁI TỤC SỔ TIẾT KIỆM" với:
   - Thông tin sổ: Ngân hàng, Số tiền gốc, Kỳ hạn, Lãi suất
   - Lãi nhận (nếu tái tục GỐC, lãi sẽ về tài khoản)
4. (Tùy chọn) Chỉnh sửa lãi suất mới hoặc kỳ hạn mới (mặc định = kỳ hạn cũ)
5. Nhấn **XÁC NHẬN TÁI TỤC**

### 4.5 Chỉnh sửa sổ tiết kiệm

1. Vào chi tiết sổ tiết kiệm đang gửi
2. Nhấn nút **Sửa** ở góc trên bên phải
3. Chỉnh sửa các thông tin:
   - Ngân hàng (nếu cần)
   - Số tiền gửi (nếu tăng, phải ≤ Tổng tiền hiện có)
   - Kỳ hạn, Lãi suất
   - Ngày bắt đầu (nếu cần)
   - Kế hoạch khi đáo hạn
   - Ghi chú, Thời gian thông báo
4. Xem ngày đáo hạn tự động tính lại (nếu kỳ hạn/ngày bắt đầu thay đổi)
5. Nhấn **LƯU THAY ĐỔI**

### 4.6 Tạo ngân hàng mới

1. Ở màn hình "Thêm sổ tiết kiệm" hoặc "Sửa sổ tiết kiệm"
2. Nhấn vào field "Ngân hàng"
3. Nhấn nút "+" bên cạnh dropdown để tạo ngân hàng mới
4. Xem dialog "THÊM NGÂN HÀNG MỚI"
5. Nhập tên ngân hàng
6. Nhập mã ngân hàng (tối đa 3-4 ký tự, tự động uppercase)
7. Chọn màu icon (từ color picker hoặc palette)
8. Xem preview icon
9. Nhấn **TẠO**

## 5. Ví dụ & minh hoạ giao diện

### SAVINGS-01: Tạo sổ tiết kiệm mới

**Mục tiêu**: Tạo một sổ tiết kiệm mới để theo dõi số tiền gửi ngân hàng, lãi suất, và ngày đáo hạn.

**Các bước chính**:
1. Vào Chức năng → Tiết kiệm ngân hàng
2. Nhấn nút "+" (FAB)
3. Chọn ngân hàng (hoặc tạo mới)
4. Nhập số tiền gửi, kỳ hạn, lãi suất
5. Chọn ngày bắt đầu (mặc định hôm nay)
6. Chọn kế hoạch khi đáo hạn
7. (Tùy chọn) Nhập ghi chú và thời gian thông báo
8. Nhấn "TẠO SỔ"

**Wireframe - Màn hình Thêm sổ tiết kiệm**:

```text
┌──────────────────────────────────────────────┐
│ <  Thêm sổ tiết kiệm                          │
└──────────────────────────────────────────────┘

┌──────────────────────────────────────────────┐
│ [ Card ]                                      │
│                                               │
│ Tổng tiền hiện có                    [ > ]    │
│ 52.000.000 đ                                  │
│                                               │
│ Ngân hàng *                                   │
│ [ Vietcombank ▼ ]                      [ + ] │
│                                               │
│ Số tiền gửi (VND) *                          │
│ [ 100.000.000 đ ]                             │
│                                               │
│ Kỳ hạn *                                      │
│ [ 6 ] tháng                                   │
│                                               │
│ Lãi suất *                                    │
│ [ 4.8 ] %/năm                                 │
│                                               │
│ Ngày bắt đầu *                                │
│ [ 20/12/2025 ]                    [📅]        │
│                                               │
│ Ngày đáo hạn (readonly)                       │
│ [ 20/06/2026 ]                                 │
│                                               │
│ Kế hoạch khi đáo hạn                          │
│ (●) Tất toán cả gốc và lãi                   │
│ ( ) Tái tục GỐC                               │
│ ( ) Tái tục GỐC + LÃI                        │
│                                               │
│ Ghi chú (optional)                            │
│ [                                      ]      │
│                                               │
│ Hiện thông báo lần 1 lúc                      │
│ [ 10:00 ]                          [🕐]       │
│                                               │
│ Hiện thông báo lần 2 lúc                      │
│ [ 19:00 ]                          [🕐]       │
└──────────────────────────────────────────────┘

        [  HỦY  ]       [  TẠO SỔ  ]
```

---

### SAVINGS-02: Tất toán sổ tiết kiệm

**Mục tiêu**: Tất toán sổ tiết kiệm khi đến ngày đáo hạn để nhận lại gốc và lãi.

**Các bước chính**:
1. Vào danh sách sổ tiết kiệm, tìm sổ đã đến hoặc quá ngày đáo hạn
2. Nhấn nút "TẤT TOÁN"
3. Xem dialog với thông tin sổ, ngày tất toán, lãi nhận được
4. (Tùy chọn) Chỉnh sửa ngày tất toán hoặc lãi nhận được
5. Nhấn "XÁC NHẬN"

**Wireframe - Dialog Tất toán**:

```text
┌─────────────────────────────────────────┐
│  TẤT TOÁN SỔ TIẾT KIỆM                   │
├─────────────────────────────────────────┤
│  [ICON BANK]  Vietcombank                │
│                                         │
│  Kỳ hạn & Lãi suất: 6 tháng · 4.8%/năm │
│  Số tiền gửi: 100.000.000 đ            │
│                                         │
│  Ngày tất toán:                         │
│  [ 20 / 12 / 2025 ]  [📅]               │
│                                         │
│  Lãi nhận được:                         │
│  [ 2.400.000 đ ]                        │
│                                         │
│  Tổng nhận: 102.400.000 đ               │
│                                         │
│  [  XÁC NHẬN  ]                         │
└─────────────────────────────────────────┘
```

---

### SAVINGS-03: Xem danh sách và chi tiết sổ tiết kiệm

**Mục tiêu**: Xem tổng quan các sổ tiết kiệm đang gửi và đã tất toán, cũng như chi tiết từng sổ.

**Các bước chính**:
1. Vào Chức năng → Tiết kiệm ngân hàng
2. Xem Card tổng quan theo filter
3. Sử dụng thanh tìm kiếm (tùy chọn)
4. Chuyển filter giữa "Đang gửi" và "Đã tất toán"
5. Nhấn vào sổ để xem chi tiết

**Wireframe - Màn hình Danh sách**:

```text
┌──────────────────────────────────────────────┐
│ <  Quản lý tiết kiệm ngân hàng                │
│                  [ + [FAB] Thêm sổ TK ]      │
└──────────────────────────────────────────────┘

[Chip] Bộ lọc
[ Đang gửi ]   [ Đã tất toán ]

┌──────────────────────────────────────────────┐
│  CARD TỔNG QUAN                              │
│  ┌──────────────┐  ┌──────────────┐         │
│  │ Số dư hiện có│  │ Lãi dự kiến   │         │
│  │ 52.000.000 đ │  │ 5.480.000 đ   │         │
│  └──────────────┘  └──────────────┘         │
│  ┌──────────────┐  ┌──────────────┐         │
│  │ Tiền đang    │  │ Lãi tháng này│         │
│  │ gửi TK       │  │ 1.900.000 đ   │         │
│  │ 350.000.000 đ│  └──────────────┘         │
│  └──────────────┘                            │
└──────────────────────────────────────────────┘

┌──────────────────────────────────────────────┐
│  🔍 Search Bar                               │
│  [ 🔍 Tìm kiếm... ]                          │
└──────────────────────────────────────────────┘

┌──────────────────────────────────────────────┐
│ [ICON BANK] Vietcombank          [Icon Xóa] │
│                                              │
│ 100.000.000 đ         |  6 tháng @ 4.8%     │
│                                              │
│ Lãi tạm tính: 2.400.000 đ                   │
│ Đáo hạn: 20/12/2025   (còn 5 ngày)          │
│                    🔔 Sắp đáo hạn            │
│                                              │
│                    [ TẤT TOÁN ]             │
└──────────────────────────────────────────────┘
```

**Wireframe - Màn hình Chi tiết**:

```text
┌──────────────────────────────────────────────┐
│ [ICON BANK]  Vietcombank              [ Sửa ]│
│                                              │
│ Kỳ hạn & Lãi suất: 6 tháng · 4.8%/năm      │
│ Số tiền gửi: 100.000.000 đ                  │
│ Lãi tạm tính: 2.400.000 đ                   │
│                                              │
│ Ngày bắt đầu: 20/06/2025                    │
│ Ngày đáo hạn: (Còn 5 ngày) 20/12/2025       │
│                                              │
│ Trạng thái: Đang gửi                        │
│                                              │
│ Kế hoạch khi đáo hạn:                       │
│ (●) Tất toán cả gốc và lãi                 │
│                                              │
│                    [  TẤT TOÁN  ]           │
└──────────────────────────────────────────────┘
```

---

### SAVINGS-04: Tái tục sổ tiết kiệm

**Mục tiêu**: Tái tục sổ tiết kiệm theo kế hoạch đã đặt khi đến ngày đáo hạn.

**Các bước chính**:
1. Tìm sổ đã đến ngày đáo hạn với kế hoạch "Tái tục GỐC" hoặc "Tái tục GỐC + LÃI"
2. Nhấn nút "TÁI TỤC"
3. Xem dialog với thông tin sổ và lãi nhận
4. (Tùy chọn) Chỉnh sửa lãi suất mới hoặc kỳ hạn mới
5. Nhấn "XÁC NHẬN TÁI TỤC"

**Kết quả**: Sổ cũ được cập nhật, sổ mới được tạo với rootSavingId liên kết với sổ cũ. Nếu tái tục GỐC, lãi được cộng vào tổng tiền hiện có. Nếu tái tục GỐC + LÃI, cả gốc và lãi đều được tái tục.

---

### SAVINGS-05: Tạo ngân hàng mới

**Mục tiêu**: Tạo một ngân hàng mới để sử dụng khi tạo sổ tiết kiệm.

**Các bước chính**:
1. Ở màn hình "Thêm sổ tiết kiệm" hoặc "Sửa sổ tiết kiệm"
2. Nhấn nút "+" bên cạnh dropdown "Ngân hàng"
3. Nhập tên ngân hàng, mã ngân hàng
4. Chọn màu icon
5. Xem preview icon
6. Nhấn "TẠO"

**Wireframe - Dialog Tạo ngân hàng**:

```text
┌─────────────────────────────────────────┐
│  THÊM NGÂN HÀNG MỚI                     │
├─────────────────────────────────────────┤
│  TÊN NGÂN HÀNG                          │
│  [ Ngân hàng ABC ]                      │
│                                         │
│  MÃ NGÂN HÀNG                           │
│  [ ABC ]                                │
│                                         │
│  MÀU ICON                               │
│  [ 🎨 ]  #FF5722                        │
│                                         │
│  PREVIEW ICON                           │
│  ┌─────────┐                            │
│  │   ABC   │  (Background: #FF5722)     │
│  └─────────┘                            │
│                                         │
│  [  HỦY  ]    [  TẠO  ]                 │
└─────────────────────────────────────────┘
```

---

### SAVINGS-06: Chỉnh sửa sổ tiết kiệm

**Mục tiêu**: Chỉnh sửa thông tin sổ tiết kiệm đang gửi (ngân hàng, số tiền, kỳ hạn, lãi suất, kế hoạch đáo hạn).

**Các bước chính**:
1. Vào chi tiết sổ tiết kiệm đang gửi
2. Nhấn nút "Sửa"
3. Chỉnh sửa các thông tin cần thiết
4. Xem ngày đáo hạn tự động tính lại (nếu kỳ hạn/ngày bắt đầu thay đổi)
5. Nhấn "LƯU THAY ĐỔI"

**Kết quả**: Thông tin sổ được cập nhật, lãi tạm tính được tính lại theo lãi suất mới. Nếu số tiền thay đổi, tổng tiền hiện có được điều chỉnh tương ứng.

## 6. Logic & quy tắc

### 6.1 Tính lãi

- Lãi được tính theo công thức: `Số tiền × Lãi suất × (Kỳ hạn / 12)`
- Lãi được tính khi đáo hạn hoặc khi rút trước hạn

### 6.2 Trạng thái

- **Đang gửi (ACTIVE)**: Sổ tiết kiệm đang hoạt động, chưa đến ngày đáo hạn hoặc chưa được xử lý
- **Đã tất toán (COMPLETED)**: Sổ đã được tất toán (rút tiền)
- **Đã tái tục (ROLLED_OVER)**: Sổ đã được tái tục, tạo sổ mới

### 6.3 Tất toán và tái tục

- **Tất toán**: Khi tất toán, gốc + lãi được cộng vào tổng tiền hiện có, tự động tạo "Thu nhập thêm" với category "Lãi tiết kiệm"
- **Tất toán trước hạn**: Có thể tất toán trước ngày đáo hạn, lãi nhận được có thể thấp hơn lãi tạm tính
- **Tái tục GỐC**: Lãi được cộng vào tổng tiền hiện có, gốc được tái tục với kỳ hạn mới
- **Tái tục GỐC + LÃI**: Cả gốc và lãi đều được tái tục, tổng tiền hiện có không thay đổi
- **Lịch sử tái tục**: Các lần tái tục được lưu và hiển thị trong chi tiết sổ, liên kết qua `rootSavingId`

### 6.4 Thông báo

- App gửi thông báo nhắc nhở khi đến ngày đáo hạn
- Thời gian thông báo có thể cấu hình cho từng sổ (`notificationTime1`, `notificationTime2`, mặc định 10:00 và 19:00)

## 7. Lưu ý quan trọng

- **Module yêu cầu Premium**: Tính năng này chỉ dành cho người dùng Premium
- **Lãi suất**: Nhập lãi suất theo năm (%/năm), từ 1 đến 100%
- **Kỳ hạn**: Tính theo tháng, từ 1 đến 36 tháng
- **Ngày đáo hạn**: Tự động tính từ ngày bắt đầu + kỳ hạn
- **Số tiền gửi**: Phải ≤ Tổng tiền hiện có, khi tạo sổ sẽ tự động trừ khỏi tổng tiền hiện có
- **Ngày bắt đầu**: Chỉ có thể chọn từ đầu tháng trước đến hiện tại
- **Thông báo**: Thông báo được gửi vào ngày đáo hạn tại 2 thời điểm (mặc định 10:00 và 19:00), có thể tùy chỉnh cho từng sổ
- **Badge "Sắp đáo hạn"**: Hiển thị khi còn ≤ 7 ngày đến ngày đáo hạn
- **Badge "Đã đáo hạn"**: Hiển thị khi đã đến ngày đáo hạn
- **Xóa sổ**: Khi xóa sổ đang gửi, số tiền gốc được cộng lại vào tổng tiền hiện có. Xóa sổ gốc sẽ xóa cả chuỗi sổ tái tục liên quan
- **Card tổng quan**: Thay đổi theo filter, hiển thị thông tin tổng hợp cho các sổ đang gửi hoặc đã tất toán

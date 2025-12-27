# Việc phải làm

## 1. Mục đích

Module **Việc phải làm** giúp bạn quản lý các công việc định kỳ và theo dõi tiến độ thực hiện, bao gồm:
- Việc phải làm theo chu kỳ thời gian (ngày/tuần/tháng/năm)
- Việc phải làm theo chỉ số (km/giờ/lần...)
- Nhắc nhở khi đến hạn
- Theo dõi lịch sử thực hiện
- Ghi nhận chi phí phát sinh (nếu có)

Module này giúp bạn không bỏ sót các công việc quan trọng như bảo dưỡng xe, thay lõi lọc nước, kiểm tra định kỳ, v.v.

## 2. Khi nào nên dùng

Sử dụng module này khi bạn có:
- Công việc lặp lại theo thời gian (ví dụ: Thay lõi lọc nước mỗi 3 tháng)
- Công việc lặp lại theo chỉ số (ví dụ: Thay nhớt xe mỗi 2.000 km)
- Cần nhắc nhở tự động khi đến hạn
- Muốn theo dõi lịch sử thực hiện
- Cần ghi nhận chi phí phát sinh

## 3. Các màn hình liên quan

- Danh sách việc phải làm
- Chọn loại việc (Theo chu kỳ / Theo chỉ số)
- Thêm việc phải làm mới
- Sửa việc phải làm
- Ghi nhận việc theo chỉ số
- Lịch sử việc phải làm
- Danh sách đến hạn (bell list)

## 4. Cách sử dụng chính

### 4.1 Thêm việc phải làm theo chu kỳ

1. Vào **Chức năng** → Chọn **Việc phải làm**
2. Nhấn nút **+** (FAB) ở góc dưới bên phải
3. Chọn **Việc phải làm theo chu kỳ**
4. Điền thông tin:
   - **Tên việc**: (bắt buộc, ví dụ: "Thay lõi lọc nước")
   - **Chu kỳ lặp**: Nhập số và chọn đơn vị (Ngày/Tuần/Tháng/Năm)
   - **Ngày đến hạn tiếp theo**: Chọn ngày (chỉ cho phép chọn từ ngày mai trở đi)
   - **Nhận thông báo lúc**: Chọn giờ (bắt buộc, ví dụ: 08:00)
   - **Việc này có phát sinh chi phí**: (Tùy chọn) Tick nếu có chi phí
     - Nếu tick: Chọn **Danh mục** (bắt buộc)
   - **Ghi chú**: Thông tin bổ sung (tùy chọn)
5. Nhấn **Lưu**

### 4.2 Thêm việc phải làm theo chỉ số

1. Vào **Chức năng** → Chọn **Việc phải làm**
2. Nhấn nút **+** (FAB)
3. Chọn **Việc phải làm theo chỉ số**
4. Điền thông tin:
   - **Tên việc**: (bắt buộc, ví dụ: "Thay nhớt xe")
   - **Chu kỳ**: Nhập số (ví dụ: 2.000)
   - **Đơn vị**: Nhập đơn vị (ví dụ: "Km")
   - **Chỉ số tại lần làm gần nhất**: Nhập chỉ số hiện tại (ví dụ: 12.500)
   - **Việc này có phát sinh chi phí**: (Tùy chọn) Tick nếu có chi phí
     - Nếu tick: Chọn **Danh mục** (bắt buộc)
   - **Ghi chú**: Thông tin bổ sung (tùy chọn)
5. Nhấn **Lưu**

### 4.3 Ghi nhận việc theo chỉ số

1. Vào danh sách việc phải làm
2. Tìm việc theo chỉ số (METRIC type) cần ghi nhận
3. Nhấn nút **Ghi nhận** trong card (chỉ hiển thị khi `isActive = true`)
4. Điền thông tin:
   - **Chỉ số tại thời điểm làm**: Nhập chỉ số hiện tại (bắt buộc, phải ≥ chỉ số lần làm gần nhất)
   - **Ghi chú**: (Tùy chọn)
5. Xem **Chênh lệch** tự động tính (chỉ số hiện tại - chỉ số lần làm gần nhất)
6. Nhấn **Đã nhận**
7. (Nếu việc có phát sinh chi phí) Chọn **Nhập chi tiêu** hoặc **Hủy**

**Lưu ý**: Việc theo chu kỳ (CYCLE type) không có nút "Ghi nhận" trong card. Ghi nhận chỉ thực hiện ở màn "Danh sách đến hạn" (bell list).

### 4.4 Xem danh sách và chi tiết

1. Vào **Chức năng** → Chọn **Việc phải làm**
2. Sử dụng **Search bar** để tìm kiếm theo tên việc
3. Sử dụng **Filter chips** để lọc:
   - **Tất cả**: Hiển thị tất cả việc
   - **Theo chu kỳ**: Chỉ hiển thị việc CYCLE type
   - **Theo chỉ số**: Chỉ hiển thị việc METRIC type
4. Nhấn vào card việc để xem chi tiết và sửa

### 4.5 Sửa việc phải làm

1. Vào danh sách việc phải làm
2. Nhấn vào card việc cần sửa
3. Chỉnh sửa thông tin:
   - **Lưu ý**: Nếu đã có lịch sử, **Chu kỳ** (CYCLE) hoặc **Đơn vị/Chu kỳ** (METRIC) sẽ bị khóa và không thể sửa
4. Nhấn **Lưu**

### 4.6 Xem lịch sử

1. Vào danh sách việc phải làm
2. Nhấn vào link **Xem lịch sử ›** của việc cần xem
3. Sử dụng **Filter chips** để lọc theo thời gian:
   - **Tất cả**: Hiển thị tất cả lịch sử
   - **Tháng này**: Chỉ hiển thị lịch sử trong tháng hiện tại
   - **Tháng trước**: Chỉ hiển thị lịch sử trong tháng trước
   - **3 tháng gần nhất**: Chỉ hiển thị lịch sử trong 3 tháng gần nhất

### 4.7 Tạm ngưng/Kích hoạt việc

1. Vào danh sách việc phải làm
2. Tìm việc cần tạm ngưng/kích hoạt
3. Bật/tắt switch **Active** ở footer card
4. Việc tạm ngưng sẽ hiển thị badge **"Tạm ngưng"** (màu xám)

### 4.8 Xóa việc phải làm

1. Vào danh sách việc phải làm
2. Nhấn vào icon **Xóa** (🗑️) ở header card
3. Xác nhận xóa trong dialog
4. Việc và tất cả lịch sử liên quan sẽ bị xóa

## 5. Ví dụ & minh hoạ giao diện

### TODO-01: Tạo việc phải làm theo chu kỳ (thay lõi lọc nước)

**Mục tiêu**: Tạo một việc phải làm theo chu kỳ để app tự động nhắc nhở khi đến hạn.

**Các bước chính**:
1. Vào Chức năng → Việc phải làm → Nhấn nút "+" (FAB)
2. Chọn "Việc phải làm theo chu kỳ"
3. Nhập tên việc: "Thay lõi lọc nước"
4. Nhập chu kỳ: "3" tháng
5. Chọn ngày đến hạn tiếp theo: 01/03/2026
6. Chọn giờ nhắc: 08:00
7. Tick "Việc này có phát sinh chi phí", chọn danh mục "Tiền điện nước"
8. Nhập ghi chú: "Thay lõi số 1 và số 2"
9. Nhấn "Lưu"

**Wireframe - Màn hình Thêm việc phải làm theo chu kỳ**:

```text
┌──────────────────────────────────────────────┐
│ <  Thêm việc phải làm theo chu kỳ           │
├──────────────────────────────────────────────┤

Tên việc
[ Thay lõi lọc nước                    ]

Chu kỳ lặp
Mỗi [ 3 ] [ Tháng ▼ ]
(Đơn vị: Ngày / Tuần / Tháng / Năm)

Ngày đến hạn tiếp theo
[ 01 / 03 / 2026    ▼ ]
Hint: 
Ngày đến hạn cho lần đầu tiên.
Các lần tiếp theo sẽ tự động tính theo chu kỳ bạn đã nhập.

Nhận thông báo lúc
[ 08 : 00           ▼ ]

──────────────────────────────────────────────
[✓] Việc này có phát sinh chi phí

┌─────────────────────────────────────┐
│ Danh mục *                           │
│ [Tiền điện nước ▼] [+ Tạo mới]      │
└─────────────────────────────────────┘

──────────────────────────────────────────────
Ghi chú (tùy chọn)
[                                          ]
[                                          ]
[                                          ]

──────────────────────────────────────────────
[ Hủy ]                               [ Lưu ]
└──────────────────────────────────────────────┘
```

---

### TODO-02: Tạo việc phải làm theo chỉ số (thay nhớt xe)

**Mục tiêu**: Tạo một việc phải làm theo chỉ số để theo dõi việc bảo dưỡng xe dựa trên số km.

**Các bước chính**:
1. Vào Chức năng → Việc phải làm → Nhấn nút "+" (FAB)
2. Chọn "Việc phải làm theo chỉ số"
3. Nhập tên việc: "Thay nhớt xe"
4. Nhập chu kỳ: "2.000", đơn vị: "Km"
5. Nhập chỉ số tại lần làm gần nhất: "12.500"
6. Tick "Việc này có phát sinh chi phí", chọn danh mục "Bảo dưỡng xe"
7. Nhập ghi chú: "Thay nhớt + lọc nhớt"
8. Nhấn "Lưu"

**Wireframe - Màn hình Thêm việc phải làm theo chỉ số**:

```text
┌──────────────────────────────────────────────┐
│ <  Thêm việc phải làm theo chỉ số            │
├──────────────────────────────────────────────┤

Tên việc
[ Thay nhớt xe                        ]

Chu kỳ
Mỗi [ 2,000 ] Đơn vị [ Km ]
(Đơn vị: Km / Giờ / Lần / ...)

Chỉ số tại lần làm gần nhất
[ 12,500 ]

──────────────────────────────────────────────
[✓] Việc này có phát sinh chi phí

┌─────────────────────────────────────┐
│ Danh mục *                           │
│ [Bảo dưỡng xe ▼] [+ Tạo mới]        │
└─────────────────────────────────────┘

──────────────────────────────────────────────
Ghi chú (tùy chọn)
[                                          ]
[                                          ]
[                                          ]

──────────────────────────────────────────────
[ Hủy ]                               [ Lưu ]
└──────────────────────────────────────────────┘
```

---

### TODO-03: Xem danh sách và chi tiết việc phải làm

**Mục tiêu**: Xem tổng quan các việc phải làm, lọc theo loại, tìm kiếm, và xem chi tiết từng việc.

**Các bước chính**:
1. Vào Chức năng → Việc phải làm
2. Xem danh sách với search bar và filter chips
3. Sử dụng filter: "Tất cả", "Theo chu kỳ", "Theo chỉ số"
4. Sử dụng search bar để tìm kiếm theo tên việc
5. Nhấn vào card việc để xem chi tiết

**Wireframe - Màn hình Danh sách việc phải làm**:

```text
┌─────────────────────────────────────────────────────────┐
│  [← Back]  Việc phải làm                    [🔔]        │
└─────────────────────────────────────────────────────────┘
│  🔍 Tìm kiếm...                                          │
│                                                          │
│  [Tất cả] [Theo chu kỳ] [Theo chỉ số]                  │
│                                                          │
│  ┌─────────────────────────────────────────────────┐    │
│  │ Card: Thay lõi lọc nước                          │    │
│  │ ┌─────────────────────────────────────────────┐ │    │
│  │ │ Thay lõi lọc nước    [Đã làm] [🗑️ Delete] │ │    │
│  │ │                                              │ │    │
│  │ │ 📅 Chu kỳ: Mỗi 3 tháng                       │ │    │
│  │ │ ✅ Ngày làm gần nhất: 01/12/2025             │ │    │
│  │ │ 📅 Ngày đến hạn tiếp theo: 01/03/2026        │ │    │
│  │ │ ⏳ Còn 76 ngày                               │ │    │
│  │ │ ───────────────────────────────────────────── │ │    │
│  │ │ Xem lịch sử ›                     [⚪ Active]│ │    │
│  │ └─────────────────────────────────────────────┘ │    │
│  └─────────────────────────────────────────────────┘    │
│                                                          │
│  ┌─────────────────────────────────────────────────┐    │
│  │ Card: Thay nhớt xe                              │    │
│  │ ┌─────────────────────────────────────────────┐ │    │
│  │ │ Thay nhớt xe                    [🗑️ Delete] │ │    │
│  │ │                                              │ │    │
│  │ │ 📏 Theo dõi: Km                              │ │    │
│  │ │ ✅ Xác nhận gần nhất: 02/12/2025             │ │    │
│  │ │ 🔢 Chỉ số lần gần nhất: 12.500 km           │ │    │
│  │ │ 🎯 Đến hạn tiếp theo: 14.500 km              │ │    │
│  │ │ ⏳ Còn ~300 km                               │ │    │
│  │ │ ───────────────────────────────────────────── │ │    │
│  │ │ [✓ Ghi nhận]                                 │ │    │
│  │ │ ───────────────────────────────────────────── │ │    │
│  │ │ Xem lịch sử ›                     [⚪ Active]│ │    │
│  │ └─────────────────────────────────────────────┘ │    │
│  └─────────────────────────────────────────────────┘    │
│                                                          │
│  [+ FAB]                                                 │
└─────────────────────────────────────────────────────────┘
```

---

### TODO-04: Ghi nhận việc theo chỉ số (thay nhớt xe)

**Mục tiêu**: Ghi nhận đã thực hiện việc theo chỉ số bằng cách nhập chỉ số hiện tại.

**Các bước chính**:
1. Vào danh sách việc phải làm
2. Tìm việc "Thay nhớt xe" (METRIC type)
3. Nhấn nút "Ghi nhận"
4. Nhập chỉ số tại thời điểm làm: "14.520"
5. Xem chênh lệch tự động tính: "+2.020 km"
6. Nhập ghi chú: "Thay nhớt + lọc nhớt"
7. Nhấn "Đã nhận"

**Wireframe - Dialog Ghi nhận việc theo chỉ số**:

```text
┌──────────────────────────────────────────────┐
│  Ghi nhận việc theo chỉ số                   │
├──────────────────────────────────────────────┤

Tên việc:
Thay nhớt xe   (readonly)

Theo dõi:
Km   (readonly)

Chỉ số lần làm gần nhất:
12,500 Km   (readonly)

──────────────────────────────────────────────
Chỉ số tại thời điểm làm
[ 14,520 ] Km

Chênh lệch:
+2,020 Km   (auto)

──────────────────────────────────────────────
Ghi chú
[                                          ]
[                                          ]
[                                          ]

──────────────────────────────────────────────
        [ Chưa nhận ]         [ Đã nhận ]
└──────────────────────────────────────────────┘
```

---

### TODO-05: Sửa việc phải làm và xem lịch sử

**Mục tiêu**: Chỉnh sửa thông tin việc phải làm và xem lịch sử các lần đã thực hiện.

**Các bước chính**:
1. Vào danh sách việc phải làm
2. Nhấn vào card việc "Thay lõi lọc nước"
3. Xem warning: "⚠️ Chu kỳ đã bị khóa vì có lịch sử" (nếu có history)
4. Chỉnh sửa ngày đến hạn, giờ nhắc, ghi chú
5. Nhấn "Lưu"
6. Nhấn "Xem lịch sử ›" để xem lịch sử với filter

**Wireframe - Màn hình Lịch sử việc phải làm**:

```text
┌─────────────────────────────────────────────────────────┐
│  [← Back]  Lịch sử việc - Thay lõi lọc nước              │
└─────────────────────────────────────────────────────────┘
│  [Tất cả] [Tháng này] [Tháng trước] [3 tháng gần nhất]  │
│                                                          │
│  ┌─────────────────────────────────────────────────┐    │
│  │ Thay lõi lọc nước              [Đã làm]          │    │
│  │                                                  │    │
│  │ 📅 Chu kỳ: Mỗi 3 tháng                           │    │
│  │ ✅ Ngày đã làm: 01/12/2025 – 09:10               │    │
│  │ 📝 Ghi chú: Thay lõi số 1 và số 2                │    │
│  └─────────────────────────────────────────────────┘    │
│                                                          │
│  ┌─────────────────────────────────────────────────┐    │
│  │ Thay lõi lọc nước              [Đã làm]          │    │
│  │                                                  │    │
│  │ 📅 Chu kỳ: Mỗi 3 tháng                           │    │
│  │ ✅ Ngày đã làm: 01/09/2025 – 08:45               │    │
│  └─────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────┘
```

---

### TODO-06: Tạm ngưng và xóa việc phải làm

**Mục tiêu**: Tạm ngưng hoặc xóa việc phải làm khi không còn cần thiết.

**Các bước chính**:
1. Vào danh sách việc phải làm
2. Tìm việc cần tạm ngưng
3. Nhấn vào switch "Active" để tắt
4. Xem badge "Tạm ngưng" xuất hiện
5. Nhấn lại switch để kích hoạt lại
6. Nhấn icon Xóa (🗑️) để xóa việc
7. Xác nhận xóa trong dialog

---

### TODO-07: Ghi nhận việc theo chỉ số và nhập chi tiêu

**Mục tiêu**: Ghi nhận việc theo chỉ số và tự động nhập chi tiêu liên quan.

**Các bước chính**:
1. Vào danh sách việc phải làm
2. Tìm việc "Thay nhớt xe" (METRIC type, hasCost = true)
3. Nhấn nút "Ghi nhận"
4. Nhập chỉ số tại thời điểm làm: "14.520"
5. Nhập ghi chú: "Thay nhớt + lọc nhớt"
6. Nhấn "Đã nhận"
7. Xem dialog "Phát sinh chi phí?" tự động mở
8. Nhấn "Nhập chi tiêu"
9. Xem màn hình "Thêm chi tiêu" với ghi chú và danh mục đã điền sẵn
10. Nhập số tiền: 500.000 đ
11. Nhấn "Lưu"

**Wireframe - Dialog Phát sinh chi phí**:

```text
┌──────────────────────────────────────────────┐
│  Phát sinh chi phí?                          │
├──────────────────────────────────────────────┤
Bạn có muốn nhập chi tiêu cho lần ghi nhận này
không?

        [ Hủy ]         [ Nhập chi tiêu ]
└──────────────────────────────────────────────┘
```

## 6. Logic & quy tắc

### 6.1 Loại việc phải làm

- **Theo chu kỳ (CYCLE type)**:
  - Lặp lại theo thời gian (Ngày/Tuần/Tháng/Năm)
  - Có thông báo nhắc nhở khi đến hạn
  - Ghi nhận chỉ thực hiện ở màn "Danh sách đến hạn" (bell list)
  - Không có nút "Ghi nhận" trong card

- **Theo chỉ số (METRIC type)**:
  - Lặp lại theo mốc chỉ số (Km/Giờ/Lần/Khác)
  - Không có thông báo (MVP1)
  - Có nút "Ghi nhận" trong card (chỉ hiển thị khi `isActive = true`)
  - Ghi nhận bằng cách nhập chỉ số hiện tại

### 6.2 Trạng thái việc phải làm

- **PENDING**: Sắp tới (chưa đến hạn)
  - Không hiển thị badge: `nextDueDate - today > 7 ngày`
  - Hiển thị badge "Sắp tới" (màu vàng): `0 < nextDueDate - today ≤ 7 ngày`
- **OVERDUE**: Quá hạn (màu đỏ) - `nextDueDate < today` và chưa xác nhận
- **NOT_COMPLETED**: Chưa làm (màu cam) - Đã đến hạn nhưng chưa xác nhận
- **COMPLETED**: Đã làm (màu xanh lá) - Đã xác nhận ghi nhận
- **CANCELLED**: Đã hủy (màu xám) - Đã hủy kỳ này
- **INACTIVE**: Tạm ngưng (màu xám) - `isActive = false`

### 6.3 Khóa chu kỳ/đơn vị

- Nếu đã có lịch sử (history records):
  - **CYCLE type**: Chu kỳ bị khóa, không thể sửa
  - **METRIC type**: Đơn vị và chu kỳ bị khóa, không thể sửa
- Hiển thị warning: "⚠️ Chu kỳ đã bị khóa vì có lịch sử" hoặc "⚠️ Đơn vị đã bị khóa vì có lịch sử"

### 6.4 Ghi nhận việc theo chỉ số

- **Validation**:
  - Chỉ số hiện tại phải ≥ chỉ số lần làm gần nhất
  - Nếu không hợp lệ: Hiển thị lỗi "Chỉ số hiện tại phải ≥ chỉ số lần làm gần nhất"
- **Tự động cập nhật**:
  - `lastMetricValue` = chỉ số hiện tại
  - `nextMetricValue` = chỉ số hiện tại + chu kỳ
  - `lastCompletedDate` = ngày hôm nay
- **Chi phí**:
  - Nếu `hasCost = true`: Hiển thị dialog "Phát sinh chi phí?" sau khi ghi nhận thành công
  - Navigate đến màn hình "Thêm chi tiêu" với `initialNote`, `initialCategoryId`, `todoHistoryId`

### 6.5 Thông báo

- **CYCLE type**: 
  - Thông báo được lên lịch khi tạo/sửa việc
  - Thông báo được hủy khi tạm ngưng hoặc xóa việc
  - Thông báo được lên lịch lại khi kích hoạt lại (nếu `nextDueDate >= hôm nay`)
- **METRIC type**: Không có thông báo (MVP1)

### 6.6 Tính toán ngày đến hạn

- **CYCLE type**: 
  - Ngày đến hạn tiếp theo tự động tính theo chu kỳ sau khi ghi nhận
  - Ví dụ: Chu kỳ 3 tháng, ngày đến hạn 01/03/2026 → Sau khi ghi nhận, ngày đến hạn tiếp theo = 01/06/2026
- **METRIC type**: 
  - Đến hạn tiếp theo = chỉ số hiện tại + chu kỳ
  - Ví dụ: Chỉ số hiện tại 14.520 km, chu kỳ 2.000 km → Đến hạn tiếp theo = 16.520 km

## 7. Lưu ý quan trọng

1. **Nút ghi nhận**:
   - **Việc theo chu kỳ (CYCLE)**: Không có nút "Ghi nhận" trong card. Ghi nhận chỉ thực hiện ở màn "Danh sách đến hạn" (bell list).
   - **Việc theo chỉ số (METRIC)**: Có nút "Ghi nhận" trong card (chỉ hiển thị khi `isActive = true`).

2. **Bell Icon**: Bell icon ở header để navigate đến màn "Danh sách đến hạn" (bell list) nơi user có thể ghi nhận các việc đến hạn (chỉ cho CYCLE type).

3. **Khóa chu kỳ/đơn vị**: Nếu đã có lịch sử, chu kỳ (CYCLE) hoặc đơn vị/chu kỳ (METRIC) sẽ bị khóa và không thể sửa để đảm bảo tính nhất quán của dữ liệu.

4. **Validation chỉ số**: Khi ghi nhận việc theo chỉ số, chỉ số hiện tại phải ≥ chỉ số lần làm gần nhất. Nếu không, app sẽ hiển thị lỗi và không cho phép ghi nhận.

5. **Chi phí phát sinh**: Nếu việc có phát sinh chi phí (`hasCost = true`), sau khi ghi nhận thành công, app sẽ hỏi có muốn nhập chi tiêu không. Nếu chọn "Nhập chi tiêu", app sẽ tự động điền sẵn ghi chú và danh mục.

6. **Xóa việc**: Khi xóa việc, tất cả lịch sử liên quan cũng sẽ bị xóa (cascade delete). Thông báo cũng sẽ được hủy.

7. **Tạm ngưng**: Khi tạm ngưng việc CYCLE type, thông báo sẽ được hủy. Khi kích hoạt lại, thông báo sẽ được lên lịch lại (nếu `nextDueDate >= hôm nay`).

8. **Premium Access**: Module này yêu cầu Premium Access. Nếu chưa có Premium, app sẽ hiển thị dialog yêu cầu nâng cấp.


# Khoản vay ngân hàng

## 1. Mục đích

Module **Khoản vay ngân hàng** giúp bạn quản lý các khoản vay tại ngân hàng, bao gồm:
- Theo dõi số tiền vay, lãi suất, kỳ hạn
- Quản lý lịch trả nợ
- Tính toán lãi suất theo từng giai đoạn (nếu có)
- Quản lý phí phạt trả chậm
- Tất toán sớm (nếu cần)

## 2. Khi nào nên dùng

Sử dụng module này khi bạn có:
- Khoản vay tại ngân hàng
- Cần theo dõi lịch trả nợ
- Muốn tính toán lãi suất và phí phạt
- Cần nhắc nhở khi đến kỳ trả nợ

## 3. Các màn hình liên quan

- Danh sách khoản vay
- Thêm khoản vay mới (4 bước)
- Sửa khoản vay
- Chi tiết khoản vay và lịch trả nợ
- Tất toán sớm

## 4. Cách sử dụng chính

### 4.1 Thêm khoản vay mới (4 bước)

#### Bước 1: Thông tin cơ bản

1. Vào **Chức năng** → Chọn **Khoản vay ngân hàng**
2. Nhấn nút **+** (FAB)
3. Điền thông tin:
   - **Ngân hàng**: Chọn hoặc tạo ngân hàng mới
   - **Tên khoản vay**: (ví dụ: "Vay mua nhà")
   - **Số tiền vay**: Số tiền gốc
   - **Ngày giải ngân**: Ngày nhận tiền
   - **Kỳ hạn**: Số năm vay
   - **Loại lãi suất**: Lãi suất ưu đãi/thả nổi hoặc Lãi suất cố định
4. Nhấn **Tiếp theo**

#### Bước 2: Cấu hình lãi suất

**Nếu chọn "Lãi suất ưu đãi/thả nổi":**
- Bật **Có lãi suất ưu đãi** (nếu có)
- Nhập **Số tháng ưu đãi** và **Lãi suất ưu đãi**
- Thêm các giai đoạn lãi suất thả nổi:
  - Chọn năm và khoảng tháng
  - Nhập lãi suất (%/năm)
  - Chọn **Thả nổi** hoặc **Cố định**

**Nếu chọn "Lãi suất cố định":**
- Nhập **Lãi suất cố định** (%/năm)

Nhấn **Tiếp theo**

#### Bước 3: Cấu hình phí phạt

1. Bật **Có phí phạt trả chậm** (nếu có)
2. Thêm các giai đoạn phí phạt:
   - Chọn năm và khoảng tháng
   - Nhập **Tỷ lệ phạt** (%/năm)
3. Nhấn **Tiếp theo**

#### Bước 4: Xác nhận và lưu

1. Xem lại thông tin:
   - Tổng số tiền phải trả
   - Lịch trả nợ dự kiến
2. Nhấn **Lưu**

### 4.2 Xem chi tiết khoản vay

1. Vào danh sách khoản vay
2. Nhấn vào khoản vay
3. Xem thông tin:
   - Thông tin cơ bản
   - Lịch trả nợ
   - Số tiền đã trả / Còn lại
   - Lãi suất và phí phạt

### 4.3 Đánh dấu đã trả

1. Vào chi tiết khoản vay
2. Tìm kỳ trả nợ cần đánh dấu
3. Nhấn **Đánh dấu đã trả**
4. Điền số tiền thực tế (nếu khác)
5. Nhấn **Xác nhận**

### 4.4 Đánh dấu kỳ đã trả

1. Vào chi tiết khoản vay
2. Tìm kỳ trả nợ đến hạn (badge "Chưa trả")
3. Nhấn **Đánh dấu đã trả**
4. Điền thông tin:
   - **Ngày trả thực tế**: Ngày đã trả (mặc định = hôm nay)
   - **Lãi thực trả**: Lãi thực tế đã trả (mặc định = lãi theo kế hoạch)
   - **Ghi chú**: (tùy chọn)
5. Xem **Tổng thực trả** tự động tính (gốc + lãi thực trả)
6. Nhấn **Xác nhận**

### 4.5 Cập nhật lãi suất hiện tại

1. Vào chi tiết khoản vay (chỉ hiển thị nếu đang ở giai đoạn lãi suất thả nổi)
2. Nhấn **Cập nhật lãi suất hiện tại**
3. Điền thông tin:
   - **Lãi suất mới**: Lãi suất mới (%/năm)
   - **Ngày bắt đầu áp dụng**: Ngày bắt đầu áp dụng lãi suất mới (mặc định = ngày đầu kỳ hiện tại)
   - **Ghi chú**: (tùy chọn)
4. Nhấn **Lưu**
5. Các kỳ chưa trả từ kỳ hiện tại trở đi sẽ được cập nhật với lãi suất mới

### 4.6 Tất toán trước hạn

1. Vào chi tiết khoản vay
2. Nhấn **Tính số tiền tất toán**
3. **Bước 1 - Nhập thông tin trả trước:**
   - Chọn hình thức: **Trả một phần** hoặc **Tất toán toàn bộ**
   - Chọn ngày trả trước (mặc định = hôm nay)
   - Nhập số tiền trả trước (nếu trả một phần)
   - Xem **Lãi phạt trả trước hạn** tự động tính
4. Nhấn **Tiếp theo**
5. **Bước 2 - So sánh phương án:**
   - Xem so sánh giữa "Không trả trước" và "Trả trước"
   - Xem kết quả: Giảm lãi, rút ngắn thời gian
6. Nhấn **Xác nhận trả trước**

### 4.7 Sửa khoản vay

1. Vào chi tiết khoản vay
2. Nhấn **Sửa**
3. Chỉnh sửa các thông tin có thể sửa:
   - **Tên khoản vay**: Có thể sửa
   - **Ngân hàng**: Có thể đổi
   - **Ghi chú**: Có thể sửa
   - **Số tiền vay, Ngày giải ngân, Thời hạn, Lãi suất**: Chỉ có thể sửa nếu chưa trả kỳ nào
4. Nhấn **Lưu**

## 5. Ví dụ & minh hoạ giao diện

### LOAN-01: Tạo khoản vay mới (vay mua nhà với lãi suất ưu đãi)

**Mục tiêu**: Tạo một khoản vay mới để theo dõi khoản vay mua nhà, lãi suất ưu đãi, và lịch trả nợ hàng tháng.

**Các bước**:
1. Vào **Chức năng** → Chọn **Vay ngân hàng**
2. Nhấn nút **+** (FAB) để thêm khoản vay mới
3. **Bước 1 - Thông tin cơ bản:**
   - Chọn ngân hàng: Vietcombank
   - Nhập tên: "Vay mua nhà Times City"
   - Nhập số tiền vay: 2.000.000.000 đ
   - Chọn ngày giải ngân: 01/04/2023
   - Nhập thời hạn: 10 năm (tự tính = 120 kỳ)
   - Chọn thời gian thông báo: 10:00 và 19:00
   - Chọn kiểu lãi suất: "Dư nợ giảm dần"
   - Nhấn **Tiếp theo**
4. **Bước 2 - Cấu hình lãi suất:**
   - Bật "Có giai đoạn lãi suất ưu đãi"
   - Nhập: 6 tháng đầu @ 6.0%/năm
   - Thêm các giai đoạn tiếp theo:
     - Năm 1 (tháng 7-12): 9.0%/năm, thả nổi
     - Năm 2 (tháng 13-24): 9.5%/năm, thả nổi
     - Năm 3 trở đi: 10.0%/năm, thả nổi
   - Nhấn **Tiếp theo**
5. **Bước 3 - Cấu hình lãi phạt trả trước hạn:**
   - Bật "Có áp dụng lãi phạt khi trả trước hạn"
   - Nhập lãi phạt: Năm 1-3: 2.0%, Năm 4-5: 1.5%, Năm 6+: 1.0%
   - Nhấn **Tiếp theo**
6. **Bước 4 - Xác nhận:**
   - Xem lại tóm tắt thông tin
   - Nhấn **Tạo khoản vay**

**Kết quả**: Khoản vay được tạo thành công, lịch trả nợ 120 kỳ được tạo tự động, thông báo được lên lịch.

**Wireframe - Bước 1: Thông tin cơ bản**

```text
┌─────────────────────────────────────────┐
│ <  Thêm khoản vay                       │
├─────────────────────────────────────────┤
│ Tên khoản vay *                          │
│ [Vay mua nhà Times City]                 │
│                                          │
│ Ngân hàng *                              │
│ [Vietcombank ▼] [+ Tạo mới]              │
│                                          │
│ Số tiền vay *                            │
│ [2.000.000.000 đ]                        │
│                                          │
│ Ngày giải ngân *                         │
│ [01/04/2023] [📅]                        │
│                                          │
│ Thời hạn vay (năm) *                     │
│ [10] năm                                 │
│ Hint: App tự tính = 120 kỳ               │
│                                          │
│ Hiện thông báo lần 1 lúc *               │
│ [10:00] [🕐]                             │
│                                          │
│ Hiện thông báo lần 2 lúc *               │
│ [19:00] [🕐]                             │
│                                          │
│ Kiểu lãi suất *                          │
│ ● Dư nợ giảm dần                         │
│ ○ Lãi suất cố định toàn kỳ               │
│                                          │
│ [TIẾP TỤC] [HỦY]                        │
└─────────────────────────────────────────┘
```

---

### LOAN-02: Xem danh sách và chi tiết khoản vay

**Mục tiêu**: Xem tổng quan các khoản vay, lọc theo trạng thái, tìm kiếm, và xem chi tiết từng khoản vay.

**Các bước**:
1. Vào **Chức năng** → Chọn **Vay ngân hàng**
2. Xem màn hình danh sách với filter "Đang vay" (mặc định) và "Đã tất toán"
3. Chuyển đổi giữa các filter để xem tổng quan khác nhau
4. Sử dụng search bar: Nhập "Times City"
5. Nhấn vào khoản vay để xem chi tiết
6. Xem lịch trả nợ với các kỳ đã trả, kỳ hiện tại, và kỳ tương lai
7. Sử dụng search bar trong lịch trả nợ: Nhập "9/2024"

**Kết quả**: Danh sách hiển thị đúng theo filter, chi tiết khoản vay hiển thị đầy đủ thông tin và lịch trả nợ.

**Wireframe - Danh sách khoản vay**

```text
┌─────────────────────────────────────────┐
│ <  Quản lý vay ngân hàng                │
├─────────────────────────────────────────┤
│ [Đang vay] [Đã tất toán]               │
│                                          │
│ ┌─────────────────────────────────────┐  │
│ │ Dư nợ hiện tại: 1.645.000.000 đ  │  │
│ │ Tổng tiền vay ban đầu: 2.000.000.000 đ│ │
│ │ Lãi đã trả: 17.200.000 đ          │  │
│ │ Đang vay: 1 khoản                 │  │
│ └─────────────────────────────────────┘  │
│                                          │
│ [🔍 Tìm kiếm (tên khoản vay, ngân hàng)]│
│                                          │
│ ┌─────────────────────────────────────┐  │
│ │ [ICON] Vietcombank    [Đang vay]   │  │
│ │ Vay mua nhà Times City              │  │
│ │ Dư nợ: 1.645.000.000 đ              │  │
│ │ Vay ban đầu: 2.000.000.000 đ        │  │
│ │ Tiến độ: 8 / 120 kỳ                 │  │
│ │ Ngày kết thúc: 01/04/2033           │  │
│ └─────────────────────────────────────┘  │
│                                          │
│                                    [+]   │
└─────────────────────────────────────────┘
```

**Wireframe - Chi tiết khoản vay**

```text
┌─────────────────────────────────────────┐
│ <  Chi tiết khoản vay                  │
├─────────────────────────────────────────┤
│ [ICON] Vietcombank              [Sửa]  │
│ Vay mua nhà Times City                  │
│ [Đang vay]                              │
│                                          │
│ Vay ban đầu: 2.000.000.000 đ           │
│ Dư nợ hiện tại: 1.645.000.000 đ        │
│ Kỳ đã trả: 8 / 120                      │
│ Lãi đã trả: 17.200.000 đ                │
│ Lãi suất hiện tại: 9.0%/năm             │
│                                          │
│ [Cập nhật lãi suất] [Tính tất toán]    │
│                                          │
│ Lịch trả nợ                              │
│ [🔍 Tìm kiếm kỳ (VD: "5/2025")]         │
│                                          │
│ Kỳ 1 – 05/2023 [Đã trả]                 │
│ Tổng: 21.5tr • Gốc: 9.5tr • Lãi: 12tr  │
│                                          │
│ Kỳ 9 – 01/2024 [Chưa trả]               │
│ Gốc: 10.000.000 đ                       │
│ Lãi: 11.500.000 đ                       │
│ Tổng: 21.500.000 đ                      │
│ Hạn trả: 15/01/2024                     │
│ [Đánh dấu đã trả]                        │
│                                          │
│ Kỳ 10 – 02/2024 [Chưa đến hạn]          │
│ Tổng: 21.5tr • Gốc: 9.5tr • Lãi: 12tr  │
└─────────────────────────────────────────┘
```

---

### LOAN-03: Đánh dấu kỳ đã trả (ghi nhận đã trả nợ)

**Mục tiêu**: Đánh dấu một kỳ trả nợ là "Đã trả" sau khi đã thanh toán cho ngân hàng.

**Các bước**:
1. Vào chi tiết khoản vay
2. Tìm kỳ hiện tại (Kỳ 9) với badge "Chưa trả"
3. Nhấn **Đánh dấu đã trả**
4. Điền thông tin:
   - Ngày trả thực tế: 15/01/2024 (mặc định = hôm nay)
   - Lãi thực trả: 11.500.000 đ (mặc định = lãi theo kế hoạch)
   - Ghi chú: (tùy chọn)
5. Xem tổng thực trả tự động tính
6. Nhấn **Xác nhận**

**Kết quả**: Kỳ 9 được cập nhật thành "Đã trả", dư nợ giảm, kỳ đã trả tăng, tổng tiền hiện có giảm.

**Wireframe - Dialog đánh dấu đã trả**

```text
┌─────────────────────────────────────────┐
│ Đánh dấu đã trả                          │
├─────────────────────────────────────────┤
│ Kỳ 9 – 01/2024          [Chưa trả]      │
│                                          │
│ Hạn trả (theo kế hoạch): 15/01/2024     │
│ Gốc phải trả (cố định): 10.000.000 đ   │
│                                          │
│ Ngày trả thực tế *                       │
│ [15/01/2024] [📅]                        │
│                                          │
│ Lãi thực trả *                           │
│ [11.500.000 đ]                           │
│ Hint: Lãi theo kế hoạch: 11.500.000 đ   │
│                                          │
│ Tổng thực trả =                          │
│   10.000.000 đ (Gốc)                    │
│ + 11.500.000 đ (Lãi)                    │
│ ────────────────────────────────        │
│ = 21.500.000 đ                           │
│                                          │
│ Ghi chú (tùy chọn)                       │
│ [Trả thiếu 500k, được giảm lãi...]     │
│                                          │
│ [HỦY] [XÁC NHẬN]                        │
└─────────────────────────────────────────┘
```

---

### LOAN-04: Cập nhật lãi suất hiện tại (khi ngân hàng điều chỉnh lãi suất thả nổi)

**Mục tiêu**: Cập nhật lãi suất mới khi ngân hàng thông báo điều chỉnh lãi suất thả nổi.

**Các bước**:
1. Vào chi tiết khoản vay
2. Xem "Lãi suất hiện tại: 9.0%/năm"
3. Nhấn **Cập nhật lãi suất hiện tại** (chỉ hiển thị nếu đang ở giai đoạn thả nổi)
4. Điền thông tin:
   - Lãi suất mới: 10.5%/năm
   - Ngày bắt đầu áp dụng: 15/01/2024 (mặc định = ngày đầu kỳ hiện tại)
   - Ghi chú: "Ngân hàng điều chỉnh lãi suất theo quyết định mới"
5. Nhấn **Lưu**

**Kết quả**: Lãi suất hiện tại được cập nhật, các kỳ chưa trả từ kỳ hiện tại trở đi được cập nhật với lãi suất mới.

**Wireframe - Dialog cập nhật lãi suất**

```text
┌─────────────────────────────────────────┐
│ Cập nhật lãi suất hiện tại              │
├─────────────────────────────────────────┤
│ [ICON] Vietcombank                       │
│ Tên khoản vay: Vay mua nhà Times City    │
│ Kỳ hiện tại: Kỳ 9 – 01/2024             │
│ Trạng thái: [Đang vay]                   │
│ Giai đoạn: Thả nổi (sau ưu đãi)         │
│                                          │
│ Lãi suất hiện tại (đang áp dụng):       │
│ [9.0] %/năm (readonly)                   │
│                                          │
│ Lãi suất mới (%/năm) *                   │
│ [10.5] %/năm                             │
│                                          │
│ Ngày bắt đầu áp dụng *                   │
│ [15/01/2024] [📅]                        │
│                                          │
│ Ghi chú (tùy chọn)                       │
│ [Ngân hàng điều chỉnh lãi suất...]       │
│                                          │
│ • Lãi suất mới sẽ được áp dụng cho các  │
│   kỳ từ Kỳ hiện tại trở đi.             │
│ • Các kỳ đã trả trước đó không bị thay đổi.│
│                                          │
│ [HỦY] [LƯU]                             │
└─────────────────────────────────────────┘
```

---

### LOAN-05: Tất toán trước hạn (trả một phần để giảm lãi)

**Mục tiêu**: Tất toán một phần khoản vay trước hạn để giảm tổng lãi phải trả và rút ngắn thời gian vay.

**Các bước**:
1. Vào chi tiết khoản vay
2. Nhấn **Tính số tiền tất toán**
3. **Bước 1 - Nhập thông tin trả trước:**
   - Chọn hình thức: "Trả một phần"
   - Chọn ngày trả trước: 15/01/2024
   - Nhập số tiền trả trước: 800.000.000 đ
   - Xem lãi phạt tự động tính: 16.000.000 đ (2.0%)
   - Nhấn **Tiếp theo**
4. **Bước 2 - So sánh phương án:**
   - Xem so sánh giữa "Không trả trước" và "Trả trước 800.000.000 đ"
   - Xem kết quả: Giảm lãi 300.000.000 đ, rút ngắn 40 kỳ
   - Nhấn **Xác nhận trả trước**

**Kết quả**: Dư nợ giảm, lịch trả nợ được tái tính, số kỳ giảm, ngày kết thúc sớm hơn.

**Wireframe - Bước 1: Nhập thông tin trả trước**

```text
┌─────────────────────────────────────────┐
│ <  Tất toán trước hạn                    │
├─────────────────────────────────────────┤
│ [ICON] Vietcombank                        │
│ Tên khoản vay: Vay mua nhà Times City     │
│ Dư nợ hiện tại: 2.000.000.000 đ          │
│ Kỳ hiện tại: Kỳ 9 – 01/2024              │
│                                          │
│ Bạn muốn tất toán như thế nào?          │
│ ● Trả một phần                           │
│ ○ Tất toán toàn bộ                       │
│                                          │
│ Ngày trả trước *                         │
│ [15/01/2024] [📅]                        │
│                                          │
│ Số tiền trả trước *                      │
│ [800.000.000 đ]                          │
│                                          │
│ Mức phạt áp dụng: 2.0%                   │
│ Lãi phạt: 16.000.000 đ                   │
│                                          │
│ [TIẾP TỤC]                               │
└─────────────────────────────────────────┘
```

**Wireframe - Bước 2: So sánh phương án**

```text
┌─────────────────────────────────────────┐
│ <  So sánh phương án                     │
├─────────────────────────────────────────┤
│ PHƯƠNG ÁN A: Không trả trước            │
│ ────────────────────────────────────────│
│ Tổng lãi phải trả đến hiện tại:         │
│   520.000.000 đ                         │
│ Tổng lãi còn lại: 520.000.000 đ         │
│ Số kỳ còn lại: 112 kỳ                   │
│ Ngày kết thúc: 01/04/2033               │
│                                          │
│ PHƯƠNG ÁN B: Trả trước 800.000.000 đ   │
│ ────────────────────────────────────────│
│ Lãi phạt trước hạn: 16.000.000 đ        │
│ Tổng lãi phải trả đến hiện tại:         │
│   536.000.000 đ                         │
│ Tổng lãi còn lại: 220.000.000 đ         │
│ Số kỳ còn lại: 72 kỳ                    │
│ Ngày kết thúc: 01/04/2029               │
│                                          │
│ KẾT QUẢ SO SÁNH:                        │
│ • Giảm được tổng lãi: 300.000.000 đ    │
│ • Rút ngắn thời gian: 40 kỳ (~3.5 năm)  │
│                                          │
│ [XÁC NHẬN TRẢ TRƯỚC]                     │
└─────────────────────────────────────────┘
```

---

### LOAN-06: Sửa khoản vay (chỉnh sửa thông tin cơ bản)

**Mục tiêu**: Chỉnh sửa thông tin cơ bản của khoản vay (tên, ngân hàng, ghi chú) sau khi đã bắt đầu trả nợ.

**Các bước**:
1. Vào chi tiết khoản vay
2. Nhấn **Sửa** (chỉ sửa tên, ghi chú, ngân hàng)
3. Chỉnh sửa:
   - Tên khoản vay: "Vay mua nhà Times City - Căn A1-1201"
   - (Tùy chọn) Đổi ngân hàng: BIDV
   - Ghi chú: "Đã chuyển sang ngân hàng mới"
4. Xem các field bị disable: Số tiền vay, Ngày giải ngân, Thời hạn, Lãi suất
5. Nhấn **Lưu**

**Kết quả**: Thông tin cơ bản được cập nhật, các thông tin khác không thay đổi.

**Lưu ý**: Nếu khoản vay chưa trả kỳ nào, có thể sửa toàn bộ thông tin (số tiền, thời hạn, cấu hình lãi suất).

## 6. Logic & quy tắc

### 6.1 Lãi suất ưu đãi/thả nổi

- Có thể có giai đoạn ưu đãi (lãi suất thấp hơn)
- Sau giai đoạn ưu đãi, lãi suất thả nổi theo từng giai đoạn
- Mỗi giai đoạn có thể là **Thả nổi** (theo thị trường) hoặc **Cố định**

### 6.2 Phí phạt trả chậm

- Phí phạt được tính theo %/năm
- Có thể cấu hình khác nhau cho từng giai đoạn
- Phí phạt chỉ áp dụng khi trả chậm

### 6.3 Lịch trả nợ

- App tự động tạo lịch trả nợ dựa trên:
  - Số tiền vay
  - Lãi suất
  - Kỳ hạn
- Mỗi kỳ trả nợ bao gồm: Gốc + Lãi

### 6.4 Tất toán sớm

- Tính toán số tiền còn lại (gốc + lãi + phí phạt nếu có)
- Sau khi tất toán, khoản vay sẽ chuyển sang trạng thái "Đã tất toán"

### 6.5 Thông báo

- App gửi thông báo nhắc nhở khi đến kỳ trả nợ
- Thời gian thông báo có thể cấu hình cho từng khoản vay (`notificationTime1`, `notificationTime2`, mặc định 10:00 và 19:00)

## 7. Lưu ý quan trọng

- **Lãi suất phức tạp**: Module này hỗ trợ lãi suất thay đổi theo từng giai đoạn, cần cấu hình cẩn thận
- **Không thể xóa khi đã có lịch trả nợ**: Nếu đã có lịch trả nợ, bạn chỉ có thể tất toán, không thể xóa
- **Tất toán sớm**: Có thể phải trả thêm phí phạt, tùy chính sách ngân hàng
- **Lịch trả nợ**: Lịch trả nợ được tính tự động, bạn không thể sửa trực tiếp

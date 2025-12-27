# Ngân sách

## 1. Mục đích

Module **Ngân sách** giúp bạn lập kế hoạch và theo dõi chi tiêu hàng tháng, đảm bảo bạn không vượt quá ngân sách đã đặt ra. Module này tự động tính toán dựa trên:
- Thu nhập định kỳ của bạn
- Chi tiêu cố định của bạn
- Chi tiêu hàng ngày thực tế

## 2. Khi nào nên dùng

Sử dụng module này khi bạn muốn:
- Lập kế hoạch chi tiêu hàng tháng
- Kiểm soát không vượt quá ngân sách
- Theo dõi tỷ lệ tiết kiệm
- Xem phân tích chi tiêu theo danh mục
- So sánh ngân sách giữa các tháng

## 3. Các màn hình liên quan

- Lập ngân sách (lần đầu hoặc copy từ tháng trước)
- Xem tổng quan ngân sách
- Lịch sử ngân sách các tháng
- Gợi ý copy từ tháng trước

## 4. Cách sử dụng chính

### 4.1 Lập ngân sách lần đầu (Case A)

1. Vào **Chức năng** → Chọn **Ngân sách**
2. Nếu chưa có ngân sách, app sẽ tự động mở màn hình **Lập ngân sách**
3. App tự động tính toán và hiển thị:
   - **Thu nhập định kỳ**: Tổng từ tất cả thu nhập định kỳ đang hoạt động (readonly, hiển thị breakdown chi tiết)
   - **Chi tiêu định kỳ**: Tổng từ tất cả chi tiêu cố định đang hoạt động (readonly, hiển thị breakdown chi tiết)
   - **Ngân sách tổng (trước tiết kiệm)**: Tự động tính = Thu nhập định kỳ - Chi tiêu định kỳ
4. Nhập **Tỷ lệ tiết kiệm**: % tiết kiệm (0-100%, bắt buộc)
5. Xem **Số tiền tiết kiệm** và **Ngân sách chi tiêu** tự động tính
6. Nhấn **Lưu ngân sách**

### 4.2 Copy ngân sách từ tháng trước (Case C)

1. Vào **Chức năng** → Chọn **Ngân sách**
2. Nếu tháng hiện tại chưa có ngân sách nhưng tháng trước có, app sẽ hiển thị màn hình **Gợi ý copy ngân sách**
3. Chọn một trong các lựa chọn:
   - **Copy toàn bộ ngân sách tháng trước**: App tự động copy tỷ lệ tiết kiệm, tính lại thu nhập/chi tiêu cố định từ dữ liệu hiện tại, và tạo ngân sách ngay lập tức
   - **Sao chép & Điều chỉnh**: App chuyển đến màn hình lập ngân sách với tỷ lệ tiết kiệm đã điền sẵn từ tháng trước, bạn có thể điều chỉnh trước khi lưu
   - **Tạo ngân sách mới**: Chạy lại flow lập ngân sách từ đầu (Case A)
4. Nếu chọn "Sao chép & Điều chỉnh", điều chỉnh tỷ lệ tiết kiệm nếu cần
5. Nhấn **Lưu ngân sách**

**Lưu ý**: Khi copy, Thu nhập định kỳ và Chi tiêu định kỳ được tính lại từ dữ liệu recurring hiện tại (không copy từ tháng trước), chỉ tỷ lệ tiết kiệm được copy.

### 4.3 Xem tổng quan ngân sách (Case B)

1. Vào **Chức năng** → Chọn **Ngân sách**
2. Nếu tháng hiện tại đã có ngân sách, app sẽ mở màn hình **Tổng quan**
3. Xem các thông tin:
   - **Ngân sách chi tiêu**: Hạn mức chi tiêu đã đặt
   - **Đã dùng**: Số tiền đã chi (bao gồm chi tiêu hàng ngày và chênh lệch thu nhập/chi tiêu)
   - **Còn lại**: Số tiền còn lại trong ngân sách
   - **Tỷ lệ đã dùng**: % ngân sách đã sử dụng (với màu sắc cảnh báo)
   - **Thu nhập & Chi tiêu lệch so với kế hoạch**: Các khoản chênh lệch so với kế hoạch ban đầu
   - **Chi tiêu hàng ngày theo danh mục**: Phân tích chi tiết chi tiêu theo từng danh mục

### 4.4 Chỉnh sửa ngân sách tháng hiện tại

1. Ở màn hình **Tổng quan ngân sách**, nhấn nút **"Chỉnh sửa ngân sách"**
2. App hiển thị màn hình chỉnh sửa với:
   - **Thu nhập định kỳ** và **Chi tiêu định kỳ**: Giữ nguyên giá trị cũ (readonly)
   - **Tỷ lệ tiết kiệm**: Đã điền sẵn từ ngân sách hiện tại (có thể chỉnh sửa)
3. Thay đổi tỷ lệ tiết kiệm nếu cần
4. Xem số tiền tiết kiệm và ngân sách chi tiêu tự động cập nhật
5. Nhấn **"Lưu ngân sách"**

**Lưu ý**: Khi chỉnh sửa, Thu nhập định kỳ và Chi tiêu định kỳ không được tính lại (giữ nguyên snapshot cũ), chỉ tỷ lệ tiết kiệm và ngân sách chi tiêu được cập nhật.

### 4.5 Xem lịch sử ngân sách

1. Vào **Chức năng** → Chọn **Ngân sách**
2. Chọn **Lịch sử** từ menu
3. Xem danh sách ngân sách các tháng đã lập
4. Nhấn vào tháng để xem chi tiết

### 4.6 Xem chi tiết chi tiêu theo danh mục

1. Vào màn hình **Tổng quan ngân sách**
2. Cuộn xuống phần **Phân tích theo danh mục**
3. Nhấn vào một danh mục
4. Xem danh sách các khoản chi tiêu trong danh mục đó

## 5. Ví dụ & minh hoạ giao diện

### 5.1 BUDGET-01: Lập ngân sách lần đầu cho tháng hiện tại

**Mục tiêu**: Lập ngân sách lần đầu để app tự động tính toán và theo dõi chi tiêu hàng tháng dựa trên thu nhập và chi tiêu cố định.

**Các bước**:
1. Vào màn hình Chức năng, chọn "Quản lý ngân sách"
2. App tự động phát hiện chưa có ngân sách và hiển thị màn hình "Lập ngân sách"
3. Xem thông tin tự động tính: Thu nhập định kỳ, Chi tiêu định kỳ, Ngân sách tổng (trước tiết kiệm)
4. Nhập tỷ lệ tiết kiệm: 20
5. Xem số tiền tiết kiệm và ngân sách chi tiêu tự động tính
6. Nhấn nút "Lưu ngân sách"

**Kết quả**: Ngân sách đã được lưu cho tháng hiện tại, tự động chuyển đến màn hình "Tổng quan ngân sách".

**Minh hoạ giao diện**:

```text
[ Card: Lập ngân sách tháng 11/2025 ]
+------------------------------------------------+
||                                                |
|| Thu nhập định kỳ                30,000,000     |
||  • Lương của tôi (Monthly)      30,000,000     |
||                                                |
|| Chi tiêu định kỳ                22,900,000     |
||  • Tiền điện (Monthly)             850,000     |
||  • Tiền nước (Monthly)             420,000     |
||  • Đóng học cho BN (Monthly)     6,800,000     |
||  • Ăn sáng uống cà phê (Weekly x 4) 900,000    |
||  • Trả nợ vay mua nhà (Monthly) 10,500,000     |
||                                                |
|| (Dữ liệu này tự động lấy từ hệ thống)          |
+------------------------------------------------+

[ Card: Ngân sách tổng (trước tiết kiệm) ]
 ------------------------------------------------
||   30,000,000 (Thu nhập định kỳ)                |
|| - 22,900,000 (Chi tiêu định kỳ)                |
||-----------------------------------------------|
|| =  7,100,000 VND                               |
 ------------------------------------------------

[ Card: Tỷ lệ tiết kiệm ]
 ------------------------------------------------
|| Bạn muốn tiết kiệm bao nhiêu?                 |
||                                                |
|| Tỉ lệ tiết kiệm (%)                            |
|| [  Input (mandatory): 20  ]                    |
||                                                |
|| → Tương ứng: 1,420,000 đ                       |
 ------------------------------------------------

[ Card: Ngân sách chi tiêu ]
 ------------------------------------------------
||    7,100,000 (Ngân sách tổng (trước tiết kiệm))|
|| -  1,420,000 (Số tiền tiết kiệm)               |
||-----------------------------------------------|
|| =  5,680,000 VND                               |
||                                                |
|| (Gồm ăn uống, đi lại, cafe, mua sắm nhỏ...)   |
 ------------------------------------------------

[ Button ]
 -------------------------------
||          Lưu ngân sách        |
 -------------------------------
```

---

### 5.2 BUDGET-02: Xem tổng quan ngân sách tháng hiện tại

**Mục tiêu**: Xem tình hình chi tiêu so với ngân sách đã đặt, bao gồm các khoản đã dùng, còn lại, và phân tích theo danh mục.

**Các bước**:
1. Vào màn hình Chức năng, chọn "Quản lý ngân sách"
2. App tự động phát hiện đã có ngân sách và hiển thị màn hình "Tổng quan ngân sách"
3. Xem Card 1 - Ngân sách tháng: Ngân sách chi tiêu, Đã dùng, Còn lại, Tỷ lệ đã dùng
4. Xem Card 2 - Thu nhập & Chi tiêu lệch so với kế hoạch
5. Xem Card 3 - Chi tiêu hàng ngày theo danh mục
6. (Tùy chọn) Click vào "Ngân sách chi tiêu ›" để xem dialog chi tiết cách tính ngân sách

**Kết quả**: Hiển thị đầy đủ thông tin ngân sách tháng hiện tại với progress ring/bar và màu sắc phù hợp.

**Minh hoạ giao diện**:

```text
[ Card 1 – Ngân sách tháng 11/2025 ]
┌──────────────────────────────────────────────┐
│ Ngân sách tháng 11/2025                     │
│                                             │
│ Ngân sách chi tiêu ›      5.680.000 đ         │
│ Đã dùng                 886.000 đ           │
│  • Chi tiêu hằng ngày            1.200.000 đ |   
│  • Chênh lệch thu nhập      -4.000.000 đ     |
│  • Chênh lệch chi tiêu       +200.000 đ      |
│ Còn lại                 2.600.000 đ         │
│                                             │
│                    74.6%                    │
│   (Bạn đã dùng 74.6% ngân sách chi tiêu tháng này)
│   (Bạn sắp dùng hết ngân sách chi tiêu tháng này)
│                                             │
│                               [Xem lịch sử]│
└──────────────────────────────────────────────┘

[ Card 2 – Thu nhập & Chi tiêu lệch so với kế hoạch ]
┌──────────────────────────────────────────────┐
│ Thu nhập & Chi tiêu lệch so với kế hoạch    │
│                                              │
│ Thu nhập định kỳ                            │
│  • Lương của tôi                 +2.000.000 đ│
│    (12.000.000 đ > 10.000.000 đ)             │
│                                              │
│ Chi tiêu định kỳ                            │
│  • Đóng học cho BN              -100.000 đ  │
│    (7.100.000 đ > 7.000.000 đ)               │
│                                              │
│ Tổng chênh lệch thu nhập:        +6.000.000 đ│
│ Tổng chênh lệch chi tiêu:        -200.000 đ  │
└──────────────────────────────────────────────┘

[ Card 3 – Chi tiêu hàng ngày theo danh mục ]
┌──────────────────────────────────────────────┐
│ Chi tiêu hàng ngày theo danh mục            │
│ (Ăn uống, đi lại, cafe, mua sắm nhỏ...)     │
│                                             │
│ Tổng chi tiêu hàng ngày: 1.200.000 đ        │
│                                             │
│ Ăn uống           600.000 đ   40% [█████----]│
│ Đi lại            300.000 đ   20% [███------]│
│ Cafe              200.000 đ   15% [██-------]│
│ Mua sắm nhỏ       100.000 đ   5%  [█--------]│
└──────────────────────────────────────────────┘
```

---

### 5.3 BUDGET-03: Chỉnh sửa ngân sách tháng hiện tại

**Mục tiêu**: Điều chỉnh tỷ lệ tiết kiệm để thay đổi ngân sách chi tiêu cho tháng hiện tại.

**Các bước**:
1. Ở màn hình "Tổng quan ngân sách", nhấn nút "Chỉnh sửa ngân sách"
2. App hiển thị màn hình chỉnh sửa (giống màn hình lập ngân sách)
3. Xem thông tin hiện tại: Thu nhập định kỳ, Chi tiêu định kỳ (giữ nguyên giá trị cũ)
4. Thay đổi tỷ lệ tiết kiệm thành 25
5. Xem số tiền tiết kiệm và ngân sách chi tiêu tự động cập nhật
6. Nhấn nút "Lưu ngân sách"

**Kết quả**: Ngân sách được cập nhật, quay lại màn hình "Tổng quan ngân sách" với các giá trị mới.

**Minh hoạ giao diện**: Tương tự như BUDGET-01 (màn hình lập ngân sách), nhưng các giá trị Thu nhập định kỳ và Chi tiêu định kỳ là readonly và giữ nguyên từ ngân sách cũ.

---

### 5.4 BUDGET-04: Copy ngân sách từ tháng trước khi bước sang tháng mới

**Mục tiêu**: Tái sử dụng ngân sách của tháng trước để tiết kiệm thời gian lập ngân sách mới, với tùy chọn điều chỉnh nếu cần.

**Các bước**:
1. Vào màn hình Chức năng, chọn "Quản lý ngân sách"
2. App tự động phát hiện tháng hiện tại chưa có ngân sách nhưng tháng trước có, hiển thị màn hình "Gợi ý copy ngân sách"
3. Chọn "Sao chép & Điều chỉnh"
4. App chuyển đến màn hình lập ngân sách với tỷ lệ tiết kiệm đã điền sẵn từ tháng trước
5. (Tùy chọn) Điều chỉnh tỷ lệ tiết kiệm nếu cần
6. Nhấn nút "Lưu ngân sách"

**Kết quả**: Ngân sách mới được tạo cho tháng hiện tại, tự động chuyển đến màn hình "Tổng quan ngân sách".

**Minh hoạ giao diện**:

```text
[ SCREEN ]  Ngân sách tháng 12/2025
┌──────────────────────────────────────────────┐
│ Tháng 12/2025 chưa có ngân sách              │
│                                              │
│ Bạn muốn tạo ngân sách tháng mới như thế nào?│
├──────────────────────────────────────────────┤
│                                              │
│ 📝 Sao chép & Điều chỉnh ›                  │
│    Hint: Sao chép ngân sách tháng 11/2025 và điều chỉnh |
│                                              │
├──────────────────────────────────────────────┤
│                                              │
│ ➕ Tạo ngân sách mới ›             			│
│   Hint: Chạy lại flow Lập Ngân Sách			│
│                                              │
└──────────────────────────────────────────────┘
```

Sau khi chọn "Sao chép & Điều chỉnh", màn hình lập ngân sách sẽ hiển thị tương tự BUDGET-01, nhưng tỷ lệ tiết kiệm đã được điền sẵn từ tháng trước.

## 6. Logic & quy tắc

### 6.1 Các trường hợp (Cases)

- **Case A**: Lập ngân sách lần đầu (chưa có ngân sách tháng nào)
- **Case B**: Tháng hiện tại đã có ngân sách → Xem tổng quan
- **Case C**: Tháng hiện tại chưa có, nhưng tháng trước có → Gợi ý copy

### 6.2 Tự động tính toán

- **Thu nhập định kỳ**: Tổng từ tất cả `recurring_income` đang hoạt động
- **Chi tiêu cố định**: Tổng từ tất cả `recurring_expense` đang hoạt động
- **Chi tiêu hàng ngày**: Tổng từ `daily_expense` trong tháng
- **Ngân sách tổng**: Thu nhập định kỳ + Thu nhập thêm
- **Tiết kiệm**: Ngân sách tổng × Tỷ lệ tiết kiệm

### 6.3 Tích hợp với các module khác

- Khi xác nhận thu nhập định kỳ → Tự động cập nhật ngân sách
- Khi xác nhận chi tiêu cố định → Tự động cập nhật ngân sách
- Chi tiêu hàng ngày được tính vào ngân sách tự động

### 6.4 Cảnh báo vượt ngân sách

- App sẽ hiển thị cảnh báo khi chi tiêu vượt quá ngân sách
- Cảnh báo hiển thị ở màn hình Home và trong thông báo

### 6.5 Snapshot

- Khi lập ngân sách, app tạo snapshot của các khoản thu/chi để lưu lại trạng thái tại thời điểm đó
- Snapshot được dùng để so sánh và phân tích

## 7. Lưu ý quan trọng

- **Mỗi tháng một ngân sách**: Bạn cần lập ngân sách cho mỗi tháng
- **Chỉnh sửa ngân sách**: Bạn có thể chỉnh sửa ngân sách tháng hiện tại bằng cách thay đổi tỷ lệ tiết kiệm. Thu nhập định kỳ và Chi tiêu định kỳ sẽ giữ nguyên (snapshot) để đảm bảo tính chính xác
- **Tự động cập nhật**: Ngân sách tự động cập nhật khi bạn xác nhận thu nhập/chi tiêu
- **Copy từ tháng trước**: Tính năng copy giúp bạn tiết kiệm thời gian lập ngân sách

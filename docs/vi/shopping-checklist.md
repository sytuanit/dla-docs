# Mua sắm (checklist)

## 1. Mục đích

Module **Mua sắm (checklist)** giúp bạn tạo **danh sách mua sắm** (tên checklist, các mục hàng), **đánh dấu đã mua** khi đi chợ, **mở nhanh** để dùng trên điện thoại, **sửa** / **tạo bản sao** từ checklist có sẵn, và **xóa** khi không cần. Checklist có thể được **gắn với bước chuẩn bị** trong module **Dịp đặc biệt** — khi đó app **không cho xóa** checklist đang được dùng.

## 2. Khi nào nên dùng

- Chuẩn bị đi siêu thị / chợ với danh sách rõ ràng.
- Muốn tái sử dụng danh sách cho các dịp giống nhau (sao chép checklist).
- Đã liên kết checklist với **Dịp đặc biệt** — khi đó checklist là một phần kế hoạch chuẩn bị.

## 3. Các màn hình liên quan

- **Chức năng** → **Mua sắm (checklist)** — danh sách các checklist
- **Tạo / Sửa checklist** — đặt tên, thêm/sửa/xóa từng mục
- **Dùng checklist** — màn hình tích chọn từng mục, thêm nhanh, reset
- **Dịp đặc biệt** — chọn checklist khi thêm bước chuẩn bị (liên kết ngoài phạm vi file này nhưng ảnh hưởng quy tắc xóa)

## 4. Cách sử dụng chính

### 4.1 Tạo checklist mới

1. Vào **Chức năng** → **Mua sắm (checklist)**.
2. Nhấn **+** (FAB) để tạo mới.
3. Nhập **tên checklist** (ví dụ: “Đi chợ tuần này”).
4. Thêm các **mục** (tên hàng); có thể chỉnh thứ tự / sửa / xóa từng mục tùy màn hình tạo.
5. **Lưu** để quay lại danh sách.

### 4.2 Mở và dùng checklist khi mua sắm

1. Trên danh sách, **chạm vào một checklist** để vào màn **dùng checklist**.
2. Tích từng mục khi đã bỏ vào giỏ (đã mua).
3. **Thêm mục nhanh** — ô nhập nhanh (nếu có) để bổ sung món phát sinh.
4. **Reset** — bỏ hết đánh dấu đã mua (app hỏi xác nhận); dùng khi muốn dùng lại cùng một danh sách cho lần sau.

### 4.3 Sửa checklist

1. Trên thẻ checklist, nhấn **Sửa ›** (hoặc điều hướng tương đương).
2. Sửa tên hoặc các mục → **Lưu**.

### 4.4 Tạo bản sao

1. Chọn chức năng **sao chép / tạo từ bản có** (theo nút trên thẻ) — app mở màn tạo với **dữ liệu đã điền sẵn** từ checklist nguồn.
2. Đổi tên nếu cần → **Lưu**.

### 4.5 Xóa checklist

1. Nhấn **xóa** trên thẻ checklist.
2. Nếu checklist **đang được dùng bởi Dịp đặc biệt**, app **không cho xóa** và hiển thị thông báo lỗi.
3. Nếu không có liên kết, xác nhận xóa — checklist và các mục bị xóa.

### 4.6 Tìm kiếm

1. Dùng ô **Tìm kiếm checklist...** trên đầu danh sách.
2. Danh sách lọc theo tên (không phân biệt hoa thường theo cách chuẩn hoá của app).

## 5. Ví dụ & minh hoạ giao diện

### 5.1 SHOP-01: Checklist đi chợ

**Mục tiêu**: Tạo checklist “Tết dương” với các mục cơ bản rồi dùng khi đi siêu thị.

**Các bước**:
1. Mua sắm (checklist) → **+** → tên `Tết dương`
2. Thêm mục: `Bánh kẹo`, `Nước ngọt`, `Khăn giấy`
3. Lưu → chạm checklist → tích từng mục khi mua xong

**Minh hoạ giao diện**:

```text
[ Tìm kiếm checklist..._____________________ ]

┌────────────────────────────────────────────┐
│ Tết dương                    Sửa ›    [x] │
│ Gồm 3 mục                                 │
│ ○ ○ ○  0/3 đã mua                         │
└────────────────────────────────────────────┘

                                              [ + ]
```

### 5.2 SHOP-02: Màn hình dùng checklist

```text
Checklist mua sắm: Tết dương

[ Reset ]

☑ Bánh kẹo
☐ Nước ngọt
☐ Khăn giấy

[ Thêm mục nhanh...____________________]
```

## 6. Logic & quy tắc

- **Từng mục** có trạng thái đã mua / chưa mua; trên danh sách có thể hiển thị **tổng số mục** và **số đã hoàn thành**.
- **Reset** — đặt lại tất cả mục về chưa mua (có hộp thoại xác nhận).
- **Liên kết Dịp đặc biệt** — khi checklist được gắn vào bước chuẩn bị của một dịp, **xóa checklist** sẽ bị chặn cho đến khi gỡ liên kết trong module Dịp đặc biệt.
- **Sao chép** — tạo checklist mới từ dữ liệu cũ, không xóa bản gốc.

## 7. Lưu ý quan trọng

- **Premium**: **Mua sắm (checklist)** thuộc nhóm Bếp & Ẩm thực; có thể có nhãn Premium trên màn **Chức năng**.
- Cần **internet** để mở tài liệu hướng dẫn trên web (theo spec app “Hướng dẫn sử dụng”); bản thân checklist hoạt động trong app như bình thường sau khi dữ liệu đã tải.

# Món ăn

## 1. Mục đích

Module **Món ăn** giúp bạn lưu trữ **công thức nấu ăn** (tên món, nguyên liệu, cách chế biến), gắn **loại đạm**, **đánh giá sao**, và tổ chức món theo **bộ sưu tập**. Dữ liệu dùng chung với module **Thực đơn** khi bạn chọn món cho từng bữa trong tuần.

## 2. Khi nào nên dùng

- Bạn muốn có một “sổ tay” món ăn cá nhân, tra cứu nhanh khi nấu.
- Bạn muốn nhóm món theo chủ đề (ví dụ: món cuối tuần, món cho trẻ) bằng **bộ sưu tập**.
- Bạn chuẩn bị dùng **Thực đơn** — cần có ít nhất một vài món đã tạo để gán vào các bữa.

## 3. Các màn hình liên quan

- **Chức năng** → nhóm **Bếp & Ẩm thực** → **Món ăn** (danh sách món)
- Tab **Món ăn** / tab **Bộ sưu tập** trên cùng màn hình danh sách
- **Thêm món ăn** / **Sửa món ăn** (form chi tiết)
- **Chi tiết bộ sưu tập** (danh sách món trong bộ, thêm món vào bộ)

## 4. Cách sử dụng chính

### 4.1 Mở danh sách và tìm kiếm

1. Vào **Chức năng** → **Món ăn** (trong phần Bếp & Ẩm thực).
2. Ở tab **Món ăn**, dùng ô **Tìm món ăn...** để lọc theo tên (kết quả cập nhật khi gõ).
3. Chuyển sang tab **Bộ sưu tập** để xem các bộ đã tạo; có ô tìm riêng cho bộ.

### 4.2 Thêm món mới

1. Nhấn nút **+** (FAB) ở góc dưới.
2. Điền **Tên món** (bắt buộc).
3. (Tuỳ chọn) **Loại đạm** — có thể nhập nhiều loại, cách nhau bởi dấu phẩy (ví dụ: Bò, Hải sản).
4. **Đánh giá** — chạm sao để đánh giá món.
5. **Nguyên liệu** — thêm ít nhất một dòng: tên nguyên liệu (bắt buộc), số lượng (tuỳ chọn). Có thể thêm nhiều dòng.
6. **Cách chế biến** — mô tả các bước nấu (tuỳ chọn nhưng nên có để sau này đọc lại).
7. **Bộ sưu tập** — gắn món vào một hoặc nhiều bộ đã có (tuỳ chọn).
8. Nhấn **Lưu**.

### 4.3 Sửa / xóa món

1. Trên danh sách, chạm vào một món để mở chi tiết chỉnh sửa.
2. Sửa các trường như khi tạo mới, rồi **Lưu** / **Cập nhật** (theo nhãn app).
3. **Xóa món**: dùng nút xoá trên màn hình (app sẽ cảnh báo nếu món đang được dùng trong **thực đơn** — xóa sẽ gỡ món khỏi thực đơn liên quan).

### 4.4 Bộ sưu tập

1. Tab **Bộ sưu tập** → **Tạo bộ sưu tập mới**, nhập tên → xác nhận.
2. Chạm vào một bộ để xem món trong bộ; có thể **Thêm món vào bộ sưu tập** (chọn từ danh sách món chưa có trong bộ).
3. **Đổi tên** / **Xóa bộ** — từ dòng bộ; xóa bộ **không** xóa món ăn, chỉ gỡ liên kết.

## 5. Ví dụ & minh hoạ giao diện

### 5.1 RECIPE-01: Tạo món và gán bộ sưu tập

**Mục tiêu**: Có một món “Canh chua cá” để sau này gán vào thực đơn và lọc theo bộ “Món Việt”.

**Các bước**:
1. Chức năng → **Món ăn** → **+**
2. Tên: `Canh chua cá`, đạm: `Cá`, thêm nguyên liệu: `Cá`, `Cà chua`, `Đậu bắp`…
3. Ghi **Cách chế biến** vài dòng
4. Chọn bộ **Món Việt** (hoặc tạo bộ trước) → **Lưu**

**Kết quả**: Món xuất hiện ở tab **Món ăn**; trong tab **Bộ sưu tập**, bộ “Món Việt” hiển thị đúng số món.

**Minh hoạ giao diện**:

```text
[ Tab: Món ăn ]  [ Tab: Bộ sưu tập ]

[ Tìm món ăn...___________________________ ]

┌────────────────────────────────────────────┐
│ Canh chua cá                        [ x ] │
│ ★★★★☆   ·   Loại đạm: Cá                  │
│ 5 nguyên liệu  ·  Bộ sưu tập: Món Việt    │
└────────────────────────────────────────────┘

                                              [ + ]
```

### 5.2 RECIPE-02: Tìm món khi danh sách dài

**Mục tiêu**: Lọc nhanh món có tên chứa “canh”.

**Các bước**: Gõ `canh` vào ô tìm — danh sách chỉ còn món khớp.

**Minh hoạ giao diện**:

```text
[ Tìm món ăn...  canh_____________________ ]

┌────────────────────────────────────────────┐
│ Canh chua cá                        [ x ] │
└────────────────────────────────────────────┘
┌────────────────────────────────────────────┐
│ Canh rau củ                         [ x ] │
└────────────────────────────────────────────┘
```

## 6. Logic & quy tắc

- **Tối thiểu một nguyên liệu** — app không cho lưu món nếu chưa có ít nhất một nguyên liệu hợp lệ.
- **Món trong thực đơn** — nếu xóa món đang dùng trong kế hoạch bữa ăn, app cảnh báo; đồng ý sẽ gỡ món khỏi các ô thực đơn tương ứng.
- **Bộ sưu tập** — là nhãn gom nhóm; cùng một món có thể thuộc nhiều bộ.
- **Đánh giá sao** — lưu theo món; có thể chỉnh lại trên danh sách (chạm sao).

## 7. Lưu ý quan trọng

- **Premium**: Mục **Món ăn** (cùng nhóm Bếp & Ẩm thực) có thể hiển thị nhãn Premium trên màn **Chức năng** — cần gói phù hợp để dùng đầy đủ.
- Nội dung hướng dẫn dành cho người dùng cuối; không mô tả đường dẫn file hay cấu trúc cơ sở dữ liệu trong app.

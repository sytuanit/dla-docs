# Thực đơn

## 1. Mục đích

Module **Thực đơn** (lên kế hoạch bữa ăn **theo tuần**) giúp bạn gán **món đã có** trong **Món ăn** vào các ô **Sáng / Trưa / Tối** cho từng ngày (Thứ 2 → Chủ nhật), đánh dấu **ngày không nấu**, xem **tổng hợp tuần** (đạm, món lặp lại), và **sao chép** từ một tuần đã có để tiết kiệm thời gian.

## 2. Khi nào nên dùng

- Bạn muốn lên menu cả tuần trước khi đi chợ.
- Bạn muốn thống nhất “hôm nay ăn gì” giữa các thành viên.
- Bạn đã có **ít nhất một món** trong module **Món ăn** (app yêu cầu khi tạo thực đơn mới).

## 3. Các màn hình liên quan

- **Chức năng** → **Thực đơn** — danh sách các **thực đơn tuần** (trạng thái: sắp tới / đang diễn ra / đã qua)
- **Tạo thực đơn tuần** — chọn ngày bắt đầu tuần (7 ngày: Thứ 2 → Chủ nhật), tuỳ chọn sao chép từ tuần trước
- **Chi tiết thực đơn** — lưới theo ngày và bữa; thêm món, món mua ngoài, ngày nghỉ nấu; Tổng hợp tuần; Tuần trước

## 4. Cách sử dụng chính

### 4.1 Tạo thực đơn tuần mới

1. Vào **Chức năng** → **Thực đơn**.
2. Nhấn **Tạo thực đơn tuần** (hoặc nút tương đương khi danh sách trống).
3. Chọn **Ngày bắt đầu tuần** (một ngày trong khoảng 7 ngày Thứ 2–CN; app gợi ý tuần là 7 ngày liên tiếp).
4. (Tuỳ chọn) Bật **Sao chép thực đơn từ tuần đã tạo** và chọn một tuần nguồn — nội dung bữa sẽ được chép sang (tuỳ chỉnh sau).
5. Nếu **tuần mới trùng ngày** với thực đơn đã có, app báo lỗi trùng — cần chọn ngày khác hoặc xóa/sửa thực đơn cũ.
6. Xác nhận tạo — mở màn **chi tiết thực đơn**.

**Lưu ý**: Nếu chưa có món nào trong **Món ăn**, app không cho tạo thực đơn mới (thông báo yêu cầu tạo món trước).

### 4.2 Thêm món vào từng bữa

1. Trong **chi tiết thực đơn**, chọn một ô **Sáng / Trưa / Tối** của một ngày.
2. App mở **Chọn món** — tìm kiếm món trong danh sách **Món ăn**; chạm để chọn.
3. (Tuỳ chọn) Dùng **Thêm món mua ngoài** (tên tự do, ví dụ: Phở, Bún bò) cho bữa không nấu tại nhà.
4. Lặp lại cho các ô còn lại.

### 4.3 Ngày không nấu (day off)

1. Chọn **Không nấu cho ngày này** trên ngày tương ứng.
2. (Tuỳ chọn) Nhập **Lý do** — app cảnh báo: mọi món đã gán trong ngày đó sẽ bị xóa khỏi thực đơn.
3. Có thể **Bật lại nấu ăn** để bỏ trạng thái nghỉ.

### 4.4 Tổng hợp và tuần trước

1. **Tổng hợp tuần** — xem thống kê: loại đạm, món nấu nhiều lần, món chỉ xuất hiện một lần, v.v. (theo nhãn trên app).
2. **Tuần trước** — mở tổng hợp hoặc tham chiếu tuần liền kề (theo luồng app).

### 4.5 Xóa thực đơn

1. Từ danh sách thực đơn, dùng thao tác xóa (biểu tượng / menu) trên một tuần.
2. Xác nhận — tuần đó bị xóa.

**Giới hạn**: Khi đã có **12 thực đơn** gần nhất, tạo thêm có thể kích hoạt thông báo giới hạn (tuần cũ nhất có thể bị xóa — theo nội dung hộp thoại app).

## 5. Ví dụ & minh hoạ giao diện

### 5.1 MEAL-01: Tạo tuần và thêm ba bữa

**Mục tiêu**: Lên thực đơn cho tuần đang diễn ra, có ít nhất một món cho Thứ 3 trưa.

**Các bước**:
1. Thực đơn → **Tạo thực đơn tuần** → chọn ngày bắt đầu phù hợp
2. Vào **Trưa** của **Thứ ba** → **Thêm món** → chọn “Canh chua cá”
3. **Lưu** / thoát theo luồng app

**Minh hoạ giao diện**:

```text
[ Thực đơn tuần: 03/01 – 09/01 ]     [🟢 Đang diễn ra]

        T2      T3      T4   ...
Sáng    [+]     [+]     [+]
Trưa    [+]   [Canh chua] [+]
Tối     [+]     [+]     [+]
```

### 5.2 MEAL-02: Ngày đi ăn ngoài

**Mục tiêu**: Thứ 7 không nấu — ghi nhận bằng ngày nghỉ hoặc món mua ngoài.

**Các bước**: Trên **Thứ bảy** → **Không nấu cho ngày này** (lý do: “Đi tiệc”) **hoặc** thêm **Món mua ngoài** vào ô bữa.

## 6. Logic & quy tắc

- **Một tuần = 7 ngày** gắn với khoảng ngày bắt đầu / kết thúc; trạng thái **sắp tới / đang diễn ra / đã qua** tính theo ngày hôm nay.
- **Không trùng khoảng ngày** với thực đơn khác đã lưu.
- **Món trong app** luôn lấy từ **Món ăn**; **món ngoài** là text tự do, có nhãn phân biệt “Mua ngoài” trên giao diện.
- **Giới hạn 12 thực đơn** — khi đạt đỉnh, app có thể đề xuất xóa tuần cũ nhất để tạo mới (xem chi tiết trong hộp thoại).

## 7. Lưu ý quan trọng

- **Premium**: **Thực đơn** thuộc nhóm Bếp & Ẩm thực; có thể có nhãn Premium trên màn **Chức năng**.
- Cần **có món trong** module **Món ăn** trước khi tạo thực đơn mới.
- Nếu hành vi không chắc chắn trên phiên bản app của bạn, dựa vào nhãn nút và thông báo trên màn hình.

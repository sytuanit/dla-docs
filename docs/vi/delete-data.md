# Yêu cầu xóa dữ liệu — Trợ lý đời sống (Daily Life Assistant)

**Daily Life Assistant / Trợ lý đời sống** (nhà phát triển: Havasoft) cho phép bạn xóa dữ liệu trong app **mà không cần xóa tài khoản cloud** (đăng nhập email). Làm theo các bước dưới đây.

**Cập nhật lần cuối:** Tháng 5/2026

---

## Cách 1 — Xóa từng phần dữ liệu (trong app)

Dùng khi bạn chỉ muốn xóa một số mục.

1. Mở **Daily Life Assistant** trên thiết bị.
2. Vào màn hình mục cần xóa (thu, chi, việc cần làm, món ăn, mục tiêu, v.v.).
3. Chọn **Xóa** / vuốt để xóa (tùy màn hình).
4. Xác nhận.

**Dữ liệu bị xóa:** chỉ mục bạn chọn.

**Dữ liệu giữ lại:** tài khoản (nếu đã đăng nhập), các dữ liệu khác, trạng thái Premium trên máy.

**Lưu giữ:** xóa ngay trong app; nếu dùng đồng bộ cloud, thay đổi được đồng bộ lên máy chủ (Supabase) khi có mạng.

---

## Cách 2 — Xóa toàn bộ dữ liệu app nhưng giữ tài khoản

Dùng khi muốn xóa sạch dữ liệu và bắt đầu lại, **không** xóa tài khoản email.

1. Mở **Daily Life Assistant**.
2. Vào **Cài đặt**.
3. Mở mục **Sao lưu & dữ liệu**.
4. Chọn **Xóa dữ liệu app** / **Dọn dữ liệu**.
5. Đọc thông báo và xác nhận.

**Dữ liệu bị xóa:**

- Toàn bộ sổ và chi tiết trên máy (thu, chi, ngân sách, tiết kiệm, nợ, mục tiêu, việc cần làm, món ăn, thực đơn, checklist mua sắm, v.v.)
- Nếu đã đăng nhập cloud và dùng đồng bộ: bản sao tương ứng trên máy chủ cloud

**Dữ liệu giữ lại:**

- **Tài khoản cloud** (email) — vẫn đăng nhập trừ khi bạn đăng xuất
- Trạng thái **Premium** lưu trên máy (nếu có)
- Lịch sử thanh toán do **Google Play** / **App Store** quản lý (không nằm trong app)

**Lưu giữ:** xóa ngay trên app; bản mirror cloud được xóa khi thao tác wipe hoàn tất. Chúng tôi không giữ bản sao riêng để khôi phục sau khi wipe.

**Lưu ý:** Nếu bạn là **thành viên** sổ chia sẻ của người khác, có thể bị hạn chế cho đến khi rời sổ.

---

## Cách 3 — Xóa dữ liệu trên máy (gỡ cài đặt)

1. Gỡ cài đặt **Daily Life Assistant** khỏi thiết bị.

**Dữ liệu bị xóa:** dữ liệu chỉ lưu trên thiết bị đó.

**Dữ liệu giữ lại:** dữ liệu trên cloud nếu trước đó đã bật đồng bộ và đăng nhập (cho đến khi bạn dùng Cách 2 khi đang đăng nhập, hoặc Cách 4).

---

## Cách 4 — Yêu cầu xóa qua email

Nếu cần hỗ trợ xóa dữ liệu cloud không xóa được trong app, hoặc muốn **xóa hẳn tài khoản cloud (email)**, liên hệ:

- **Email:** [cuong.hungduong87@gmail.com](mailto:cuong.hungduong87@gmail.com?subject=Daily%20Life%20Assistant%20-%20Data%20deletion%20request)
- **Tiêu đề:** `Daily Life Assistant - Data deletion request`
- **Ghi rõ:** email đăng ký cloud (nếu có), muốn xóa gì (một phần hay toàn bộ tài khoản), nền tảng (Android / iOS).

Chúng tôi phản hồi trong vòng **30 ngày**. Xóa tài khoản trên backend sau khi xác minh yêu cầu; không lưu thông tin đăng nhập đã xóa ngoài nghĩa vụ pháp lý hoặc bảo mật.

---

## Dữ liệu app không kiểm soát

- **File sao lưu** bạn xuất ra Google Drive, iCloud, v.v. — xóa tại nơi bạn đã lưu.
- Lịch sử mua **Google Play** — quản lý trong tài khoản Google.

---

## Liên quan

- [Chính sách bảo mật](./privacy.md)
- [Điều khoản sử dụng](./terms.md)

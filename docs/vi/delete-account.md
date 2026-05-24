# Yêu cầu xóa tài khoản — Trợ lý đời sống (Daily Life Assistant)

**Daily Life Assistant / Trợ lý đời sống** (nhà phát triển: Havasoft) cho phép bạn yêu cầu xóa **tài khoản cloud** (đăng nhập email) và dữ liệu liên quan trên máy chủ.

**Cập nhật lần cuối:** Tháng 5/2026

---

## Trước khi yêu cầu xóa tài khoản

Tài khoản cloud là **tùy chọn**. Bạn có thể dùng app chỉ trên máy mà không cần tài khoản.

Nếu chỉ muốn xóa dữ liệu app nhưng **giữ** đăng nhập, xem [Yêu cầu xóa dữ liệu](./delete-data.md) (Cài đặt → **Xóa dữ liệu app**).

---

## Cách yêu cầu xóa tài khoản

Hiện chưa có nút “Xóa tài khoản” trong app — xử lý qua email.

1. **Chuẩn bị trong app (khuyến nghị)**
   - Nếu bạn là **thành viên** sổ chia sẻ: **Cài đặt → Chia sẻ sổ → Rời khỏi sổ**.
   - **Đăng xuất** tài khoản cloud trong **Cài đặt** (nên làm).
   - Gỡ app **không** tự xóa tài khoản cloud.

2. **Gửi email yêu cầu xóa**
   - **Gửi tới:** [cuong.hungduong87@gmail.com](mailto:cuong.hungduong87@gmail.com?subject=Daily%20Life%20Assistant%20-%20Account%20deletion%20request)
   - **Tiêu đề:** `Daily Life Assistant - Account deletion request`
   - **Nội dung cần có:**
     - **Email** của tài khoản cloud cần xóa
     - Xác nhận muốn **xóa vĩnh viễn tài khoản**
     - Nền tảng: **Android** hoặc **iOS**
     - Nếu bạn là **chủ sổ** chia sẻ: ghi rõ để xử lý teardown sổ

3. **Xác minh**
   - Chúng tôi có thể phản hồi để xác nhận. Vui lòng trả lời nếu được yêu cầu.

4. **Hoàn tất**
   - Sau xác minh, tài khoản và dữ liệu backend liên quan được xóa. Chúng tôi xác nhận qua email khi xong.

**Thời hạn mục tiêu:** phản hồi trong **30 ngày**; hoàn tất xóa **sớm nhất có thể** sau xác minh (thường trong **30 ngày** kể từ yêu cầu hợp lệ).

---

## Dữ liệu bị xóa

Khi tài khoản cloud bị xóa, chúng tôi xóa (hoặc ẩn danh nếu pháp luật yêu cầu):

- **Đăng nhập cloud** (email / auth)
- **Hồ sơ / mirror user** trên backend (Supabase)
- **Dữ liệu sổ** trên server (thu, chi, ngân sách, tiết kiệm, nợ, mục tiêu, việc cần làm, món ăn, thực đơn, checklist, v.v.)
- **Sổ chia sẻ** bạn **sở hữu** (sau teardown chủ sổ), và **tư cách thành viên** sổ đã tham gia
- **Yêu cầu tham gia** và trạng thái chia sẻ gắn với tài khoản

Dữ liệu **chỉ trên máy** mất khi gỡ app hoặc **Xóa dữ liệu app**; xóa tài khoản tập trung vào dữ liệu **server** gắn email.

---

## Dữ liệu giữ lại

| Dữ liệu | Lý do |
|--------|--------|
| Lịch sử mua / gói **Google Play / App Store** | Do Google / Apple quản lý |
| **File sao lưu** bạn xuất ra Drive, iCloud, v.v. | Bạn tự xóa tại nơi lưu |
| **Log tối thiểu** | Chỉ nếu luật hoặc chống lạm dụng yêu cầu; không dùng để khôi phục tài khoản |

**Premium trên máy:** có thể còn trên thiết bị cho đến khi xóa dữ liệu app hoặc cài lại; không gắn tài khoản cloud có thể khôi phục sau khi xóa.

---

## Lưu giữ sau khi xóa

- Thông tin đăng nhập và dữ liệu app đã xóa **không** được giữ để dùng lại sản phẩm.
- Sao lưu và thanh toán ngoài app thuộc chính sách **Google/Apple** hoặc nơi bạn lưu file.

---

## Liên hệ

- **Email hỗ trợ:** [cuong.hungduong87@gmail.com](mailto:cuong.hungduong87@gmail.com)
- **Xóa dữ liệu, giữ tài khoản:** [delete-data.md](./delete-data.md)
- **Chính sách bảo mật:** [privacy.md](./privacy.md)

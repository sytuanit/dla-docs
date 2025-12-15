# Cài đặt

## 1. Mục đích

Module **Cài đặt** cho phép bạn cấu hình ứng dụng theo nhu cầu cá nhân, bao gồm:
- Ngôn ngữ và tiền tệ
- Thông báo
- Danh mục (categories)
- Sao lưu và phục hồi dữ liệu
- Bảo mật (mật khẩu, Face ID)

## 2. Khi nào nên dùng

Sử dụng module này khi bạn muốn:
- Thay đổi ngôn ngữ hoặc tiền tệ
- Bật/tắt thông báo
- Quản lý danh mục (thêm, sửa, xóa, đặt mặc định)
- Sao lưu hoặc phục hồi dữ liệu
- Thay đổi mật khẩu hoặc bật Face ID

## 3. Các màn hình liên quan

- Màn hình cài đặt chính
- Cài đặt cơ bản
- Chọn ngôn ngữ
- Chọn tiền tệ
- Quản lý danh mục
- Sao lưu dữ liệu
- Phục hồi dữ liệu
- Đổi mật khẩu
- Bật Face ID / Fingerprint

## 4. Cách sử dụng chính

### 4.1 Thay đổi ngôn ngữ

1. Vào **Cài đặt** → **Hiển thị & Ngôn ngữ** → **Ngôn ngữ**
2. Chọn ngôn ngữ muốn dùng
3. App sẽ tự động reload với ngôn ngữ mới

### 4.2 Thay đổi tiền tệ

1. Vào **Cài đặt** → **Hiển thị & Ngôn ngữ** → **Tiền tệ**
2. Chọn loại tiền tệ
3. Tất cả số tiền sẽ được hiển thị theo đơn vị mới

### 4.3 Bật/tắt thông báo

1. Vào **Cài đặt** → **Thông báo**
2. Bật/tắt switch **Thông báo**
3. Nếu bật, bạn sẽ nhận thông báo nhắc nhở về:
   - Thu nhập định kỳ đến kỳ
   - Chi tiêu cố định đến kỳ
   - Tài khoản tiết kiệm đáo hạn
   - Dịp đặc biệt sắp đến

### 4.4 Quản lý danh mục

1. Vào **Cài đặt** → **Danh mục**
2. Chọn loại danh mục muốn quản lý:
   - Thu nhập định kỳ
   - Thu nhập thêm
   - Chi tiêu cố định
   - Chi tiêu hàng ngày
3. Thêm/Sửa/Xóa danh mục
4. Đặt danh mục mặc định (cho chi tiêu hàng ngày)

### 4.5 Sao lưu dữ liệu

1. Vào **Cài đặt** → **Sao lưu & Dữ liệu** → **Sao lưu**
2. Chọn nơi lưu (File system)
3. Nhấn **Sao lưu**
4. File backup sẽ được tạo

### 4.6 Phục hồi dữ liệu

1. Vào **Cài đặt** → **Sao lưu & Dữ liệu** → **Phục hồi**
2. Chọn file backup
3. Xác nhận phục hồi
4. **Lưu ý**: Phục hồi sẽ ghi đè dữ liệu hiện tại

## 5. Minh hoạ giao diện (Wireframe)

### 5.1 Màn hình Cài đặt chính

```text
┌─────────────────────────────────────────┐
│  ← Quay lại    Cài đặt                   │
├─────────────────────────────────────────┤
│  Hiển thị & Ngôn ngữ                     │
│  ┌───────────────────────────────────┐ │
│  │ Ngôn ngữ                           │ │
│  │ Tiếng Việt                    →    │ │
│  │                                    │ │
│  │ Tiền tệ                            │ │
│  │ VND (₫)                      →     │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Thông báo                              │
│  ┌───────────────────────────────────┐ │
│  │ Thông báo                    [ON]  │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Sao lưu & Dữ liệu                      │
│  ┌───────────────────────────────────┐ │
│  │ Sao lưu                      →    │ │
│  │                                    │ │
│  │ Phục hồi                      →    │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Danh mục                               │
│  ┌───────────────────────────────────┐ │
│  │ Quản lý danh mục              →    │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Bảo mật                                │
│  ┌───────────────────────────────────┐ │
│  │ Mật khẩu                      →    │ │
│  │                                    │ │
│  │ Face ID / Fingerprint         →    │ │
│  └───────────────────────────────────┘ │
└─────────────────────────────────────────┘
```

## 6. Logic & quy tắc

### 6.1 Ngôn ngữ

- Hỗ trợ: Tiếng Việt, English, 日本語
- Thay đổi ngôn ngữ sẽ reload toàn bộ app
- Danh mục hệ thống sẽ tự động dịch theo ngôn ngữ mới

### 6.2 Tiền tệ

- Mỗi ngôn ngữ có tiền tệ mặc định (ví dụ: VND cho tiếng Việt)
- Bạn có thể chọn tiền tệ khác
- Tất cả số tiền sẽ được format theo tiền tệ đã chọn

### 6.3 Thông báo

- Thông báo chỉ hoạt động khi app được cấp quyền
- Thời gian thông báo: 4PM và 7PM
- Có thể tắt thông báo cho từng loại riêng (trong tương lai)

### 6.4 Danh mục

- Danh mục hệ thống không thể xóa, chỉ có thể tắt
- Danh mục người dùng có thể xóa (nếu chưa được sử dụng)
- Mỗi loại danh mục độc lập (thu nhập định kỳ, chi tiêu hàng ngày, v.v.)

## 7. Lưu ý quan trọng

- **Sao lưu thường xuyên**: Nên sao lưu dữ liệu định kỳ để tránh mất dữ liệu
- **Phục hồi sẽ ghi đè**: Phục hồi sẽ thay thế toàn bộ dữ liệu hiện tại
- **Mật khẩu**: Nếu quên mật khẩu, bạn có thể reset (sẽ xóa dữ liệu)

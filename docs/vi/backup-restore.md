# Sao lưu & Phục hồi

## 1. Mục đích

Module **Sao lưu & Phục hồi** giúp bạn:
- Sao lưu toàn bộ dữ liệu ứng dụng ra file
- Phục hồi dữ liệu từ file backup
- Bảo vệ dữ liệu khỏi mất mát do lỗi thiết bị hoặc cài đặt lại app

## 2. Khi nào nên dùng

Sử dụng module này khi bạn muốn:
- Sao lưu dữ liệu trước khi cài đặt lại app
- Chuyển dữ liệu sang thiết bị mới
- Phục hồi dữ liệu sau khi mất dữ liệu
- Tạo bản sao lưu định kỳ

## 3. Các màn hình liên quan

- Màn hình sao lưu
- Màn hình phục hồi

## 4. Cách sử dụng chính

### 4.1 Sao lưu dữ liệu

1. Vào **Cài đặt** → **Sao lưu & Dữ liệu** → **Sao lưu**
2. Xem thông tin:
   - Số lượng bản ghi sẽ được sao lưu
   - Kích thước file dự kiến
3. Nhấn **Sao lưu**
4. Chọn vị trí lưu file (File system)
5. File backup sẽ được tạo với tên: `dla-backup-YYYY-MM-DD-HHmmss.json`
6. Lưu file này ở nơi an toàn (cloud, máy tính, v.v.)

### 4.2 Phục hồi dữ liệu

1. Vào **Cài đặt** → **Sao lưu & Dữ liệu** → **Phục hồi**
2. Chọn file backup từ file system
3. Xem thông tin file:
   - Ngày tạo backup
   - Số lượng bản ghi
   - Kích thước file
4. **Cảnh báo**: Phục hồi sẽ ghi đè toàn bộ dữ liệu hiện tại
5. Nhấn **Phục hồi**
6. Xác nhận phục hồi
7. Chờ quá trình phục hồi hoàn tất
8. App sẽ tự động reload

## 5. Minh hoạ giao diện (Wireframe)

### 5.1 Màn hình Sao lưu

```text
┌─────────────────────────────────────────┐
│  ← Quay lại    Sao lưu dữ liệu          │
├─────────────────────────────────────────┤
│  Thông tin sao lưu                       │
│                                         │
│  ┌───────────────────────────────────┐ │
│  │ Số lượng bản ghi                    │ │
│  │ 1,234 bản ghi                       │ │
│  │                                    │ │
│  │ Kích thước dự kiến                  │ │
│  │ ~2.5 MB                             │ │
│  │                                    │ │
│  │ Dữ liệu sẽ được sao lưu:           │ │
│  │ • Thu nhập định kỳ                  │ │
│  │ • Chi tiêu cố định                  │ │
│  │ • Chi tiêu hàng ngày                │ │
│  │ • Ngân sách                         │ │
│  │ • Tiết kiệm                         │ │
│  │ • Khoản vay                         │ │
│  │ • Dịp đặc biệt                      │ │
│  │ • Danh mục                          │ │
│  └───────────────────────────────────┘ │
│                                         │
│  [Sao lưu]                              │
└─────────────────────────────────────────┘
```

### 5.2 Màn hình Phục hồi

```text
┌─────────────────────────────────────────┐
│  ← Quay lại    Phục hồi dữ liệu         │
├─────────────────────────────────────────┤
│  Chọn file backup                        │
│                                         │
│  [Chọn file...]                         │
│                                         │
│  Thông tin file                          │
│  ┌───────────────────────────────────┐ │
│  │ File: dla-backup-2024-11-15.json │ │
│  │                                    │ │
│  │ Ngày tạo: 15/11/2024 10:30        │ │
│  │                                    │ │
│  │ Số lượng bản ghi: 1,234           │ │
│  │                                    │ │
│  │ Kích thước: 2.5 MB                 │ │
│  └───────────────────────────────────┘ │
│                                         │
│  ⚠️ Cảnh báo                            │
│  Phục hồi sẽ ghi đè toàn bộ dữ liệu    │
│  hiện tại. Bạn có chắc chắn?           │
│                                         │
│  [Phục hồi] [Hủy]                       │
└─────────────────────────────────────────┘
```

## 6. Logic & quy tắc

### 6.1 Định dạng file backup

- File backup là JSON format
- Tên file: `dla-backup-YYYY-MM-DD-HHmmss.json`
- Chứa toàn bộ dữ liệu: users, categories, transactions, budgets, v.v.

### 6.2 Dữ liệu được sao lưu

- Tất cả bảng trong database
- Bao gồm cả dữ liệu hệ thống và dữ liệu người dùng
- Không bao gồm: cài đặt app, preferences (ngôn ngữ, tiền tệ)

### 6.3 Phục hồi

- Phục hồi sẽ xóa toàn bộ dữ liệu hiện tại
- Sau đó import dữ liệu từ file backup
- App sẽ tự động reload sau khi phục hồi xong

### 6.4 Validation

- App kiểm tra định dạng file trước khi phục hồi
- Kiểm tra version compatibility (nếu có)
- Hiển thị lỗi nếu file không hợp lệ

## 7. Lưu ý quan trọng

- **Sao lưu thường xuyên**: Nên sao lưu định kỳ (hàng tuần hoặc hàng tháng)
- **Lưu ở nhiều nơi**: Lưu file backup ở nhiều nơi (cloud, máy tính, USB)
- **Phục hồi sẽ mất dữ liệu hiện tại**: Đảm bảo bạn đã sao lưu dữ liệu hiện tại trước khi phục hồi
- **Không thể hoàn tác**: Sau khi phục hồi, không thể hoàn tác

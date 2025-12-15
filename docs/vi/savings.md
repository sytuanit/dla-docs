# Tiết kiệm

## 1. Mục đích

Module **Tiết kiệm** giúp bạn quản lý các tài khoản tiết kiệm tại ngân hàng, theo dõi số dư, lãi suất, và kỳ hạn. Module này hỗ trợ:
- Quản lý nhiều tài khoản tiết kiệm
- Theo dõi lãi suất và kỳ hạn
- Tự động tính lãi khi đến kỳ đáo hạn
- Rút tiền trước hạn (nếu cần)
- Gia hạn (rollover) tài khoản

## 2. Khi nào nên dùng

Sử dụng module này khi bạn có:
- Tài khoản tiết kiệm tại ngân hàng
- Cần theo dõi số dư và lãi suất
- Muốn nhắc nhở khi đến kỳ đáo hạn
- Cần quản lý nhiều tài khoản tiết kiệm

## 3. Các màn hình liên quan

- **SavingsList** - Danh sách tài khoản tiết kiệm
- **AddSavingsAccount** - Thêm tài khoản mới
- **EditSavingsAccount** - Sửa tài khoản
- **SavingsAccountDetail** - Chi tiết tài khoản
- **WithdrawSavingsAccount** - Rút tiền trước hạn

## 4. Cách sử dụng chính

### 4.1 Thêm tài khoản tiết kiệm

1. Vào **Chức năng** → Chọn **Tiết kiệm**
2. Nhấn nút **+** (FAB)
3. Điền thông tin:
   - **Ngân hàng**: Chọn hoặc tạo ngân hàng mới
   - **Số tiền gửi**: Số tiền ban đầu
   - **Lãi suất**: % lãi suất/năm
   - **Kỳ hạn**: Số tháng (ví dụ: 3, 6, 12 tháng)
   - **Ngày gửi**: Ngày bắt đầu gửi tiết kiệm
   - **Ghi chú**: Thông tin bổ sung (tùy chọn)
4. Nhấn **Lưu**

### 4.2 Xem chi tiết tài khoản

1. Vào danh sách tiết kiệm
2. Nhấn vào tài khoản
3. Xem thông tin:
   - Số dư hiện tại
   - Lãi suất và kỳ hạn
   - Ngày đáo hạn
   - Lãi dự kiến

### 4.3 Rút tiền trước hạn

1. Vào chi tiết tài khoản
2. Chọn **Rút tiền trước hạn**
3. Điền:
   - **Số tiền rút**: Số tiền muốn rút
   - **Lãi suất thực tế**: (nếu khác với lãi suất gốc)
4. Nhấn **Xác nhận**

### 4.4 Gia hạn (Rollover)

1. Vào chi tiết tài khoản
2. Khi đến ngày đáo hạn, chọn **Gia hạn**
3. Điều chỉnh (nếu cần):
   - **Lãi suất mới**: (nếu thay đổi)
   - **Kỳ hạn mới**: (nếu thay đổi)
4. Nhấn **Xác nhận**

## 5. Minh hoạ giao diện (Wireframe)

### 5.1 Màn hình Danh sách (SavingsList)

```text
┌─────────────────────────────────────────┐
│  ← Quay lại    Tiết kiệm                │
├─────────────────────────────────────────┤
│  [🔍 Tìm kiếm...]                        │
│  [Tất cả ▼] [Đang hoạt động] [Đã đáo hạn]│
├─────────────────────────────────────────┤
│  ┌───────────────────────────────────┐ │
│  │ VCB - Tiết kiệm 6 tháng            │ │
│  │ 50,000,000 đ                        │ │
│  │ Lãi suất: 6.5%/năm                  │ │
│  │ Đáo hạn: 15/05/2025                │ │
│  │ [Đang hoạt động]                    │ │
│  │                                    │ │
│  │ [Chi tiết] [Sửa] [Xóa]             │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Tổng: 50,000,000 đ                    │
├─────────────────────────────────────────┤
│                                    [+]   │
└─────────────────────────────────────────┘
```

### 5.2 Màn hình Chi tiết (SavingsAccountDetail)

```text
┌─────────────────────────────────────────┐
│  ← Quay lại    Chi tiết tiết kiệm       │
├─────────────────────────────────────────┤
│  VCB - Tiết kiệm 6 tháng                │
│                                         │
│  Số tiền gửi                            │
│  50,000,000 đ                           │
│                                         │
│  Lãi suất                               │
│  6.5% / năm                             │
│                                         │
│  Kỳ hạn                                 │
│  6 tháng                                │
│                                         │
│  Ngày gửi                               │
│  15/11/2024                             │
│                                         │
│  Ngày đáo hạn                           │
│  15/05/2025                             │
│                                         │
│  Lãi dự kiến                            │
│  1,625,000 đ                            │
│                                         │
│  [Rút tiền trước hạn] [Gia hạn]        │
│  [Sửa] [Xóa]                            │
└─────────────────────────────────────────┘
```

## 6. Logic & quy tắc

### 6.1 Tính lãi

- Lãi được tính theo công thức: `Số tiền × Lãi suất × (Kỳ hạn / 12)`
- Lãi được tính khi đáo hạn hoặc khi rút trước hạn

### 6.2 Trạng thái

- **Đang hoạt động**: Tài khoản chưa đến ngày đáo hạn
- **Đã đáo hạn**: Đã đến ngày đáo hạn, chưa gia hạn hoặc rút

### 6.3 Rút trước hạn

- Khi rút trước hạn, lãi suất có thể thay đổi (tùy chính sách ngân hàng)
- Bạn có thể rút một phần hoặc toàn bộ

### 6.4 Thông báo

- App gửi thông báo nhắc nhở khi đến ngày đáo hạn
- Thông báo hiển thị vào 4PM và 7PM (nếu bật thông báo)

## 7. Lưu ý quan trọng

- **Lãi suất**: Nhập lãi suất theo năm (%/năm)
- **Kỳ hạn**: Tính theo tháng
- **Ngày đáo hạn**: Tự động tính từ ngày gửi + kỳ hạn
- **Không thể xóa**: Tài khoản đã có giao dịch không thể xóa (chỉ có thể tắt)

## 8. Mapping kỹ thuật (for dev)

### 8.1 Routes / Route Names

- `SavingsList` - Danh sách
- `AddSavingsAccount` - Thêm mới
- `EditSavingsAccount` - Sửa (param: `savingsAccountId`)
- `SavingsAccountDetail` - Chi tiết (param: `savingsAccountId`)
- `WithdrawSavingsAccount` - Rút tiền (param: `savingsAccountId`)

### 8.2 Screen File Paths

- `src/screens/finance/SavingsListScreen.tsx`
- `src/screens/finance/AddSavingsAccountScreen.tsx`
- `src/screens/finance/EditSavingsAccountScreen.tsx`
- `src/screens/finance/SavingsAccountDetailScreen.tsx`
- `src/screens/finance/WithdrawSavingsAccountScreen.tsx`

### 8.3 Services / Repos File Paths

- `src/data/repo/savings.repository.ts` - `savingsAccountRepo`, `savingsBankRepo`
- `src/modules/finance/services/savings.service.ts` - `rolloverSavingsAccount`, `withdrawSavingsAccount`
- `src/modules/finance/hooks/useSavingsList.ts` - Custom hook cho list

### 8.4 DB Tables / Models

- `savings_account` - Bảng tài khoản tiết kiệm
  - `id`, `user_id`, `bank_id`, `amount`, `interest_rate`, `term_months`, `start_date`, `maturity_date`, `status`, `note`
- `savings_bank` - Bảng ngân hàng
  - `id`, `user_id`, `name`, `code`, `is_active`

### 8.5 i18n Keys

- `savings.list_title` - "Tiết kiệm"
- `savings.add_title` - "Thêm tài khoản tiết kiệm"
- `savings.detail.title` - "Chi tiết tiết kiệm"
- `savings.bank` - "Ngân hàng"
- `savings.amount` - "Số tiền gửi"
- `savings.interest_rate` - "Lãi suất"
- `savings.term_months` - "Kỳ hạn"
- Và nhiều keys khác trong `src/i18n/locales/vi.json` dưới key `savings`


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

- **BankDebtList** - Danh sách khoản vay
- **AddBankDebt** - Thêm khoản vay mới (4 bước)
- **EditBankDebt** - Sửa khoản vay
- **BankDebtDetail** - Chi tiết khoản vay và lịch trả nợ
- **EarlySettlement** - Tất toán sớm

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

### 4.4 Tất toán sớm

1. Vào chi tiết khoản vay
2. Chọn **Tất toán sớm**
3. Điền:
   - **Ngày tất toán**: Ngày muốn tất toán
   - **Số tiền tất toán**: Số tiền sẽ trả
4. Xem thông tin:
   - Số tiền gốc còn lại
   - Lãi suất phải trả
   - Phí phạt (nếu có)
   - Tổng số tiền
5. Nhấn **Xác nhận tất toán**

## 5. Minh hoạ giao diện (Wireframe)

### 5.1 Màn hình Danh sách (BankDebtList)

```text
┌─────────────────────────────────────────┐
│  ← Quay lại    Khoản vay ngân hàng      │
├─────────────────────────────────────────┤
│  [🔍 Tìm kiếm...]                        │
│  [Tất cả ▼] [Đang vay] [Đã tất toán]    │
├─────────────────────────────────────────┤
│  ┌───────────────────────────────────┐ │
│  │ VCB - Vay mua nhà                  │ │
│  │ 1,000,000,000 đ                    │ │
│  │ Lãi suất: 8.5%/năm                 │ │
│  │ Kỳ hạn: 20 năm                      │ │
│  │ Còn lại: 950,000,000 đ             │ │
│  │ [Đang vay]                         │ │
│  │                                    │ │
│  │ [Chi tiết] [Sửa] [Xóa]             │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Tổng nợ: 1,000,000,000 đ              │
│  Đã trả: 50,000,000 đ                  │
│  Còn lại: 950,000,000 đ                │
├─────────────────────────────────────────┤
│                                    [+]   │
└─────────────────────────────────────────┘
```

### 5.2 Màn hình Thêm (Bước 1 - Thông tin cơ bản)

```text
┌─────────────────────────────────────────┐
│  ← Quay lại    Thêm khoản vay (1/4)     │
├─────────────────────────────────────────┤
│  Ngân hàng *                             │
│  [VCB ▼] [+ Tạo mới]                     │
│                                         │
│  Tên khoản vay *                         │
│  [Vay mua nhà]                           │
│                                         │
│  Số tiền vay *                           │
│  [1,000,000,000] đ                       │
│                                         │
│  Ngày giải ngân *                        │
│  [15/11/2024]                            │
│                                         │
│  Kỳ hạn (năm) *                          │
│  [20]                                    │
│                                         │
│  Loại lãi suất *                         │
│  ● Lãi suất ưu đãi/thả nổi               │
│  ○ Lãi suất cố định                      │
│                                         │
│  [Tiếp theo] [Hủy]                       │
└─────────────────────────────────────────┘
```

### 5.3 Màn hình Chi tiết (BankDebtDetail)

```text
┌─────────────────────────────────────────┐
│  ← Quay lại    Chi tiết khoản vay       │
├─────────────────────────────────────────┤
│  VCB - Vay mua nhà                      │
│                                         │
│  Thông tin cơ bản                        │
│  ┌───────────────────────────────────┐ │
│  │ Số tiền vay: 1,000,000,000 đ      │ │
│  │ Ngày giải ngân: 15/11/2024        │ │
│  │ Kỳ hạn: 20 năm                    │ │
│  │ Lãi suất: 8.5%/năm                │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Tổng quan                               │
│  ┌───────────────────────────────────┐ │
│  │ Đã trả: 50,000,000 đ              │ │
│  │ Còn lại: 950,000,000 đ            │ │
│  │ Số kỳ đã trả: 5/240               │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Lịch trả nợ                             │
│  ┌───────────────────────────────────┐ │
│  │ 15/12/2024                         │ │
│  │ 10,000,000 đ                       │ │
│  │ ✅ Đã trả                          │ │
│  └───────────────────────────────────┘ │
│  ┌───────────────────────────────────┐ │
│  │ 15/01/2025                         │ │
│  │ 10,000,000 đ                       │ │
│  │ ⏳ Chờ thanh toán                  │ │
│  └───────────────────────────────────┘ │
│                                         │
│  [Tất toán sớm] [Sửa] [Xóa]             │
└─────────────────────────────────────────┘
```

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
- Thông báo hiển thị vào 4PM và 7PM (nếu bật thông báo)

## 7. Lưu ý quan trọng

- **Lãi suất phức tạp**: Module này hỗ trợ lãi suất thay đổi theo từng giai đoạn, cần cấu hình cẩn thận
- **Không thể xóa khi đã có lịch trả nợ**: Nếu đã có lịch trả nợ, bạn chỉ có thể tất toán, không thể xóa
- **Tất toán sớm**: Có thể phải trả thêm phí phạt, tùy chính sách ngân hàng
- **Lịch trả nợ**: Lịch trả nợ được tính tự động, bạn không thể sửa trực tiếp

## 8. Mapping kỹ thuật (for dev)

### 8.1 Routes / Route Names

- `BankDebtList` - Danh sách
- `AddBankDebt` - Thêm mới (param: `screen?: 1|2|3|4` để chọn bước ban đầu)
- `EditBankDebt` - Sửa (param: `debtId`, `screen?: 1|2|3|4`)
- `BankDebtDetail` - Chi tiết (param: `debtId`)
- `EarlySettlement` - Tất toán sớm (param: `debtId`)

### 8.2 Screen File Paths

- `src/screens/finance/BankDebtListScreen.tsx`
- `src/screens/finance/AddBankDebtScreen.tsx`
- `src/screens/finance/EditBankDebtScreen.tsx`
- `src/screens/finance/BankDebtDetailScreen.tsx`
- `src/screens/finance/EarlySettlementScreen.tsx`

### 8.3 Services / Repos File Paths

- `src/data/repo/bank-debt.repository.ts` - `bankDebtRepo`
- `src/data/repo/bank-debt-payment.repository.ts` - `bankDebtPaymentRepo`
- `src/data/repo/bank-debt-interest-config.repository.ts` - `bankDebtInterestConfigRepo`
- `src/data/repo/bank-debt-penalty-config.repository.ts` - `bankDebtPenaltyConfigRepo`
- `src/modules/finance/services/bank-debt.service.ts` - `generatePaymentSchedules`, `calculateEarlySettlement`
- `src/modules/finance/hooks/useBankDebtList.ts` - Custom hook cho list

### 8.4 DB Tables / Models

- `bank_debt` - Bảng khoản vay
  - `id`, `user_id`, `bank_id`, `name`, `principal_amount`, `disbursement_date`, `term_years`, `interest_type`, `status`
- `bank_debt_payment` - Bảng lịch trả nợ
  - `id`, `user_id`, `debt_id`, `due_date`, `principal_amount`, `interest_amount`, `penalty_amount`, `status`, `paid_at`
- `bank_debt_interest_config` - Bảng cấu hình lãi suất
  - `id`, `debt_id`, `year`, `start_month`, `end_month`, `interest_rate`, `is_floating`
- `bank_debt_penalty_config` - Bảng cấu hình phí phạt
  - `id`, `debt_id`, `year`, `start_month`, `end_month`, `penalty_rate`

### 8.5 i18n Keys

- `bank_debt.list_title` - "Khoản vay ngân hàng"
- `bank_debt.add_title` - "Thêm khoản vay"
- `bank_debt.detail.title` - "Chi tiết khoản vay"
- `bank_debt.step1.title` - "Thông tin cơ bản"
- `bank_debt.step2.title` - "Cấu hình lãi suất"
- `bank_debt.step3.title` - "Cấu hình phí phạt"
- `bank_debt.step4.title` - "Xác nhận"
- Và nhiều keys khác trong `src/i18n/locales/vi.json` dưới key `bank_debt`


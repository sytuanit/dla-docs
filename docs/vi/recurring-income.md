# Thu nhập định kỳ

## 1. Mục đích

Module **Thu nhập định kỳ** giúp bạn quản lý các nguồn thu nhập thường xuyên như:
- Lương hàng tháng
- Tiền cho thuê nhà
- Lương hưu
- Cổ tức đầu tư
- Các khoản thu nhập khác có tính chu kỳ

Module này tự động tạo các **kỳ phát sinh** (occurrences) dựa trên chu kỳ bạn đã cấu hình, và nhắc nhở bạn khi đến kỳ nhận tiền.

## 2. Khi nào nên dùng

Sử dụng module này khi bạn có:
- Thu nhập cố định theo chu kỳ (hàng tuần, 2 tuần, hoặc hàng tháng)
- Cần theo dõi và xác nhận khi đã nhận tiền
- Muốn tự động tính toán vào ngân sách hàng tháng

## 3. Các màn hình liên quan

- **RecurringIncomeList** - Danh sách thu nhập định kỳ
- **AddRecurringIncome** - Thêm thu nhập định kỳ mới
- **EditRecurringIncome** - Sửa thu nhập định kỳ
- **RecurringIncomeHistory** - Lịch sử các kỳ phát sinh

## 4. Cách sử dụng chính

### 4.1 Thêm thu nhập định kỳ mới

1. Vào **Chức năng** → Chọn **Thu nhập định kỳ**
2. Nhấn nút **+** (FAB) ở góc dưới bên phải
3. Điền thông tin:
   - **Danh mục**: Chọn hoặc tạo danh mục mới
   - **Số tiền**: Nhập số tiền thu nhập (có thể để trống, nhập sau khi xác nhận)
   - **Chu kỳ**: Chọn Hàng tuần / 2 tuần / Hàng tháng
   - **Ngày**: Chọn ngày trong chu kỳ (ví dụ: ngày 15 hàng tháng)
   - **Ngày bắt đầu**: (Chỉ cho chu kỳ 2 tuần) Chọn ngày bắt đầu nhận
   - **Ghi chú**: Thông tin bổ sung (tùy chọn)
4. Nhấn **Lưu**

### 4.2 Xác nhận đã nhận tiền

1. Vào danh sách thu nhập định kỳ
2. Tìm item có badge **"Chờ xác nhận"** (màu vàng)
3. Nhấn vào item để mở dialog xác nhận
4. Điền:
   - **Số tiền thực tế**: (nếu khác với dự kiến)
   - **Ghi chú**: (tùy chọn)
5. Nhấn **Xác nhận**

### 4.3 Sửa thu nhập định kỳ

1. Vào danh sách thu nhập định kỳ
2. Nhấn vào item cần sửa
3. Chọn **Sửa** từ menu
4. Cập nhật thông tin
5. Nhấn **Lưu**

### 4.4 Xem lịch sử

1. Vào danh sách thu nhập định kỳ
2. Nhấn vào item
3. Chọn **Lịch sử** để xem tất cả các kỳ phát sinh đã qua

### 4.5 Tắt/Bật thu nhập

1. Vào danh sách thu nhập định kỳ
2. Tìm item cần tắt/bật
3. Bật/tắt switch **Hoạt động** ở bên phải item

## 5. Minh hoạ giao diện (Wireframe)

### 5.1 Màn hình Danh sách (RecurringIncomeList)

```text
┌─────────────────────────────────────────┐
│  ← Quay lại    Thu nhập định kỳ         │
├─────────────────────────────────────────┤
│  [🔍 Tìm kiếm...]                        │
│  [Tất cả ▼] [Chờ xác nhận] [Đã xác nhận]│
├─────────────────────────────────────────┤
│  ┌───────────────────────────────────┐ │
│  │ Lương của tôi          [Hoạt động] │ │
│  │ 10,000,000 đ                      │ │
│  │ Hàng tháng - Ngày 15              │ │
│  │ Kỳ tiếp theo: 15/12/2024          │ │
│  │ [Chờ xác nhận]                    │ │
│  │                                    │ │
│  │ [Sửa] [Lịch sử] [Xóa]             │ │
│  └───────────────────────────────────┘ │
│                                         │
│  ┌───────────────────────────────────┐ │
│  │ Tiền cho thuê nhà    [Hoạt động] │ │
│  │ 5,000,000 đ                      │ │
│  │ Hàng tháng - Ngày 1              │ │
│  │ Kỳ tiếp theo: 01/01/2025        │ │
│  │ [Đã xác nhận]                    │ │
│  │                                    │ │
│  │ [Sửa] [Lịch sử] [Xóa]             │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Tổng: 15,000,000 đ/tháng              │
├─────────────────────────────────────────┤
│                                    [+]   │
└─────────────────────────────────────────┘
```

### 5.2 Màn hình Thêm/Sửa (AddRecurringIncome / EditRecurringIncome)

```text
┌─────────────────────────────────────────┐
│  ← Quay lại    Thêm thu nhập định kỳ     │
├─────────────────────────────────────────┤
│  Danh mục *                              │
│  [Lương của tôi ▼]                      │
│                                         │
│  Số tiền                                 │
│  [10,000,000] đ                         │
│  (Có thể để trống, nhập khi xác nhận)   │
│                                         │
│  Chu kỳ *                                │
│  ○ Hàng tuần                             │
│  ● Hàng tháng                            │
│  ○ 2 tuần                                │
│                                         │
│  Ngày *                                  │
│  [15]                                    │
│  (1-31 cho hàng tháng, 1-7 cho hàng tuần)│
│                                         │
│  Ngày bắt đầu                            │
│  [15/11/2024]                            │
│  (Chỉ cho chu kỳ 2 tuần)                │
│                                         │
│  Ghi chú                                 │
│  [Lương tháng 11/2024]                   │
│                                         │
│  [Lưu] [Hủy]                            │
└─────────────────────────────────────────┘
```

### 5.3 Dialog Xác nhận (ConfirmOccurrenceDialog)

```text
┌─────────────────────────────────────────┐
│  Xác nhận đã nhận                        │
├─────────────────────────────────────────┤
│  Lương của tôi                           │
│  Kỳ: 15/11/2024                         │
│                                         │
│  Số tiền dự kiến: 10,000,000 đ         │
│                                         │
│  Số tiền thực tế *                       │
│  [10,000,000] đ                         │
│                                         │
│  Ghi chú                                 │
│  [Đã nhận đủ]                            │
│                                         │
│  [Xác nhận] [Hủy]                       │
└─────────────────────────────────────────┘
```

### 5.4 Màn hình Lịch sử (RecurringIncomeHistory)

```text
┌─────────────────────────────────────────┐
│  ← Quay lại    Lịch sử - Lương của tôi   │
├─────────────────────────────────────────┤
│  ┌───────────────────────────────────┐ │
│  │ 15/11/2024                         │ │
│  │ 10,000,000 đ                       │ │
│  │ ✅ Đã xác nhận                     │ │
│  │ Ghi chú: Đã nhận đủ                 │ │
│  └───────────────────────────────────┘ │
│                                         │
│  ┌───────────────────────────────────┐ │
│  │ 15/10/2024                         │ │
│  │ 10,000,000 đ                       │ │
│  │ ✅ Đã xác nhận                     │ │
│  └───────────────────────────────────┘ │
│                                         │
│  ┌───────────────────────────────────┐ │
│  │ 15/09/2024                         │ │
│  │ 10,000,000 đ                       │ │
│  │ ❌ Đã hủy                          │ │
│  │ Lý do: Không nhận được             │ │
│  └───────────────────────────────────┘ │
└─────────────────────────────────────────┘
```

## 6. Logic & quy tắc

### 6.1 Chu kỳ và Ngày

- **Hàng tuần**: Chọn ngày trong tuần (1=Thứ 2, 7=Chủ nhật)
- **2 tuần**: Chọn ngày trong tuần + ngày bắt đầu cụ thể
- **Hàng tháng**: Chọn ngày trong tháng (1-31)

### 6.2 Tự động tạo kỳ phát sinh

- App tự động tạo **occurrence** (kỳ phát sinh) khi:
  - Thêm thu nhập mới
  - Đến ngày trong chu kỳ
  - Tháng mới bắt đầu

### 6.3 Trạng thái kỳ phát sinh

- **PENDING**: Chờ xác nhận (hiển thị badge vàng)
- **COMPLETED**: Đã xác nhận (hiển thị badge xanh)
- **CANCELLED**: Đã hủy (hiển thị badge đỏ)

### 6.4 Tích hợp với Ngân sách

- Khi xác nhận thu nhập, app tự động cập nhật ngân sách tháng hiện tại (nếu có)
- Thu nhập được tính vào "Thu nhập định kỳ" trong ngân sách

### 6.5 Thông báo

- App gửi thông báo nhắc nhở khi đến kỳ nhận tiền
- Thông báo hiển thị vào 4PM và 7PM (nếu bật thông báo)

## 7. Lưu ý quan trọng

- **Số tiền có thể để trống**: Nếu bạn chưa biết chính xác số tiền, có thể để trống và nhập khi xác nhận
- **Không thể xóa khi đã có occurrence**: Nếu đã có kỳ phát sinh, bạn chỉ có thể tắt (isActive = false), không thể xóa
- **Xác nhận muộn**: Bạn có thể xác nhận các kỳ đã qua, app sẽ tự động tính lại ngân sách
- **Thay đổi chu kỳ**: Khi sửa chu kỳ, các occurrence tương lai sẽ được tính lại

## 8. Mapping kỹ thuật (for dev)

### 8.1 Routes / Route Names

- `RecurringIncomeList` - Danh sách
- `AddRecurringIncome` - Thêm mới
- `EditRecurringIncome` - Sửa (param: `recurringIncomeId`)
- `RecurringIncomeHistory` - Lịch sử (param: `recurringIncomeId`)

### 8.2 Screen File Paths

- `src/screens/finance/RecurringIncomeListScreen.tsx`
- `src/screens/finance/AddRecurringIncomeScreen.tsx`
- `src/screens/finance/EditRecurringIncomeScreen.tsx`
- `src/screens/finance/RecurringIncomeHistoryScreen.tsx`
- `src/screens/finance/RecurringItemListScreen.tsx` (shared component)
- `src/screens/finance/AddRecurringItemScreen.tsx` (shared component)

### 8.3 Services / Repos File Paths

- `src/data/repo/recurring-income.repository.ts` - `recurringIncomeRepo`
- `src/data/repo/recurring-income-occurrence.repository.ts` - `recurringIncomeOccurrenceRepo`
- `src/data/repo/recurring-income-category.repository.ts` - `recurringIncomeCategoryRepo`
- `src/modules/finance/services/occurrence.service.ts` - `confirmIncomeOccurrence`, `cancelIncomeOccurrence`
- `src/modules/finance/services/budget.service.ts` - `recalculateBudgetIfExists`, `hasRecurringIncomeInCurrentMonth`
- `src/modules/finance/hooks/useRecurringIncomeList.ts` - Custom hook cho list

### 8.4 DB Tables / Models

- `recurring_income` - Bảng định nghĩa thu nhập định kỳ
  - `id`, `user_id`, `category_id`, `amount`, `cycle`, `cycle_day`, `start_date`, `note`, `is_active`
- `recurring_income_occurrence` - Bảng các kỳ phát sinh
  - `id`, `user_id`, `recurring_id`, `due_date`, `amount_snapshot`, `status`, `confirmed_at`, `note`
- `recurring_income_category` - Bảng danh mục
  - `id`, `user_id`, `name`, `type` (SYSTEM/USER), `is_active`
- `category_translation` - Bảng dịch danh mục (i18n)
  - `id`, `category_id`, `category_type`, `locale`, `name`

### 8.5 i18n Keys

- `recurring_income.add_title` - "Thêm thu nhập định kỳ"
- `recurring_income.edit_title` - "Sửa thu nhập định kỳ"
- `recurring_income.list_title` - "Thu nhập định kỳ"
- `recurring_income.category` - "Danh mục"
- `recurring_income.amount` - "Số tiền"
- `recurring_income.cycle` - "Chu kỳ"
- `recurring_income.cycle_day` - "Ngày"
- `recurring_income.start_date` - "Ngày bắt đầu"
- `recurring_income.note` - "Ghi chú"
- `recurring_income.next_due_date` - "Kỳ tiếp theo"
- `recurring_income.status.pending` - "Chờ xác nhận"
- `recurring_income.status.completed` - "Đã xác nhận"
- `recurring_income.status.cancelled` - "Đã hủy"
- `recurring_income.confirm_dialog.title` - "Xác nhận đã nhận"
- `recurring_income.confirm_dialog.actual_amount` - "Số tiền thực tế"
- Và nhiều keys khác trong `src/i18n/locales/vi.json` dưới key `recurring_income`


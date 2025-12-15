# Thu nhập thêm

## 1. Mục đích

Module **Thu nhập thêm** giúp bạn ghi nhận các khoản thu nhập không định kỳ, không có chu kỳ cố định như:
- Bán hàng online
- Freelance
- Thưởng
- Quà tặng tiền mặt
- Các khoản thu nhập bất thường khác

Khác với **Thu nhập định kỳ**, thu nhập thêm không có chu kỳ tự động, bạn phải nhập thủ công mỗi lần.

## 2. Khi nào nên dùng

Sử dụng module này khi bạn muốn:
- Ghi nhận các khoản thu nhập ngẫu nhiên, không định kỳ
- Theo dõi tổng thu nhập trong khoảng thời gian
- Phân tích xu hướng thu nhập thêm
- Tính vào ngân sách hàng tháng

## 3. Các màn hình liên quan

- **ExtraIncomeList** - Danh sách thu nhập thêm
- **AddExtraIncome** - Thêm thu nhập mới
- **EditExtraIncome** - Sửa thu nhập

## 4. Cách sử dụng chính

### 4.1 Thêm thu nhập thêm

1. Vào **Chức năng** → Chọn **Thu nhập thêm**
2. Nhấn nút **+** (FAB) ở góc dưới bên phải
3. Điền thông tin:
   - **Danh mục**: Chọn hoặc tạo danh mục mới
   - **Số tiền**: Nhập số tiền đã nhận
   - **Ngày**: Chọn ngày nhận tiền (mặc định là hôm nay)
   - **Ghi chú**: Mô tả chi tiết (tùy chọn)
4. Nhấn **Lưu**

### 4.2 Xem danh sách thu nhập

1. Vào **Chức năng** → Chọn **Thu nhập thêm**
2. Danh sách hiển thị theo layout bạn đã cấu hình (1, 2, 3, hoặc 4 cột)
3. Sử dụng **Tìm kiếm** để lọc theo danh mục hoặc ghi chú
4. Chọn **Bộ lọc thời gian**: Hôm nay / Tuần này / Tháng này / Tháng trước / Tùy chọn

### 4.3 Sửa thu nhập

1. Vào danh sách thu nhập thêm
2. Nhấn và giữ (long press) vào item cần sửa
3. Chọn **Sửa** từ menu
4. Cập nhật thông tin
5. Nhấn **Lưu**

### 4.4 Xóa thu nhập

1. Vào danh sách thu nhập thêm
2. Nhấn và giữ (long press) vào item cần xóa
3. Chọn **Xóa** từ menu
4. Xác nhận xóa

## 5. Minh hoạ giao diện (Wireframe)

### 5.1 Màn hình Danh sách (ExtraIncomeList)

```text
┌─────────────────────────────────────────┐
│  ← Quay lại    Thu nhập thêm            │
├─────────────────────────────────────────┤
│  [🔍 Tìm kiếm...]                        │
│  [Tháng này ▼] [Tuần này] [Hôm nay]     │
├─────────────────────────────────────────┤
│  ┌───────────────────────────────────┐ │
│  │ Bán hàng online                    │ │
│  │ 500,000 đ                          │ │
│  │ 15/11/2024                         │ │
│  │                                    │ │
│  │ [Sửa] [Xóa]                        │ │
│  └───────────────────────────────────┘ │
│                                         │
│  ┌───────────────────────────────────┐ │
│  │ Freelance                           │ │
│  │ 1,000,000 đ                        │ │
│  │ 14/11/2024                         │ │
│  │                                    │ │
│  │ [Sửa] [Xóa]                        │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Tổng: 1,500,000 đ                     │
├─────────────────────────────────────────┤
│                                    [+]   │
└─────────────────────────────────────────┘
```

### 5.2 Màn hình Thêm/Sửa (AddExtraIncome / EditExtraIncome)

```text
┌─────────────────────────────────────────┐
│  ← Quay lại    Thêm thu nhập thêm        │
├─────────────────────────────────────────┤
│  Danh mục *                              │
│  [Bán hàng online ▼]                     │
│                                         │
│  Số tiền *                               │
│  [500,000] đ                             │
│                                         │
│  Ngày *                                  │
│  [15/11/2024]                            │
│                                         │
│  Ghi chú                                 │
│  [Bán sản phẩm A]                        │
│                                         │
│  [Lưu] [Hủy]                            │
└─────────────────────────────────────────┘
```

## 6. Logic & quy tắc

### 6.1 Layout hiển thị

- Bạn có thể cấu hình số cột hiển thị: 1, 2, 3, hoặc 4 cột
- Layout được lưu trong cài đặt và áp dụng cho tất cả danh sách thu nhập thêm

### 6.2 Bộ lọc thời gian

- **Hôm nay**: Chỉ hiển thị thu nhập trong ngày
- **Tuần này**: Từ đầu tuần đến hôm nay
- **Tháng này**: Từ đầu tháng đến hôm nay
- **Tháng trước**: Toàn bộ tháng trước
- **Tùy chọn**: Chọn khoảng thời gian tùy ý

### 6.3 Tìm kiếm

- Tìm kiếm trong **tên danh mục** và **ghi chú**
- Không phân biệt hoa thường
- Tìm kiếm real-time khi gõ

### 6.4 Tích hợp với Ngân sách

- Thu nhập thêm được tính vào "Thu nhập thêm" trong ngân sách
- Giúp bạn theo dõi tổng thu nhập hàng tháng

## 7. Lưu ý quan trọng

- **Không có chu kỳ**: Thu nhập thêm không có chu kỳ tự động, bạn phải nhập thủ công mỗi lần
- **Có thể xóa**: Bạn có thể xóa bất kỳ thu nhập nào
- **Tích hợp ngân sách**: Thu nhập thêm tự động tính vào ngân sách tháng hiện tại

## 8. Mapping kỹ thuật (for dev)

### 8.1 Routes / Route Names

- `ExtraIncomeList` - Danh sách
- `AddExtraIncome` - Thêm mới
- `EditExtraIncome` - Sửa (param: `extraIncomeId`)

### 8.2 Screen File Paths

- `src/screens/finance/ExtraIncomeListScreen.tsx`
- `src/screens/finance/AddExtraIncomeScreen.tsx`
- `src/screens/finance/EditExtraIncomeScreen.tsx`

### 8.3 Services / Repos File Paths

- `src/data/repo/extra-income.repository.ts` - `extraIncomeRepo`, `extraIncomeCategoryRepo`
- `src/modules/finance/hooks/useExtraIncomeList.ts` - Custom hook cho list
- `src/services/layoutSettings.service.ts` - `getExtraIncomeLayout`, `setExtraIncomeLayout`
- `src/domain/finance/extra-income.utils.ts` - `formatOccurredDate`

### 8.4 DB Tables / Models

- `extra_income` - Bảng thu nhập thêm
  - `id`, `user_id`, `category_id`, `amount`, `occurred_at`, `note`, `created_at`, `updated_at`
- `extra_income_category` - Bảng danh mục
  - `id`, `user_id`, `name`, `type` (SYSTEM/USER), `is_active`
- `category_translation` - Bảng dịch danh mục (i18n)
  - `id`, `category_id`, `category_type` = 'extra_income', `locale`, `name`

### 8.5 i18n Keys

- `extra_income.list_title` - "Thu nhập thêm"
- `extra_income.add_title` - "Thêm thu nhập thêm"
- `extra_income.edit_title` - "Sửa thu nhập thêm"
- `extra_income.category` - "Danh mục"
- `extra_income.amount` - "Số tiền"
- `extra_income.date` - "Ngày"
- `extra_income.note` - "Ghi chú"
- Và nhiều keys khác trong `src/i18n/locales/vi.json` dưới key `extra_income`


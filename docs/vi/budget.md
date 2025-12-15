# Ngân sách

## 1. Mục đích

Module **Ngân sách** giúp bạn lập kế hoạch và theo dõi chi tiêu hàng tháng, đảm bảo bạn không vượt quá ngân sách đã đặt ra. Module này tự động tính toán dựa trên:
- Thu nhập định kỳ của bạn
- Chi tiêu cố định của bạn
- Chi tiêu hàng ngày thực tế

## 2. Khi nào nên dùng

Sử dụng module này khi bạn muốn:
- Lập kế hoạch chi tiêu hàng tháng
- Kiểm soát không vượt quá ngân sách
- Theo dõi tỷ lệ tiết kiệm
- Xem phân tích chi tiêu theo danh mục
- So sánh ngân sách giữa các tháng

## 3. Các màn hình liên quan

- **BudgetSetup** - Lập ngân sách (Case A & C)
- **BudgetOverview** - Xem tổng quan ngân sách (Case B)
- **BudgetHistory** - Lịch sử ngân sách các tháng
- **BudgetCopySuggestion** - Gợi ý copy từ tháng trước (Case C)

## 4. Cách sử dụng chính

### 4.1 Lập ngân sách lần đầu (Case A)

1. Vào **Chức năng** → Chọn **Ngân sách**
2. Nếu chưa có ngân sách, app sẽ tự động mở màn hình **Lập ngân sách**
3. App tự động tính toán:
   - **Thu nhập định kỳ**: Tổng từ tất cả thu nhập định kỳ đang hoạt động
   - **Chi tiêu cố định**: Tổng từ tất cả chi tiêu cố định đang hoạt động
4. Điều chỉnh (nếu cần):
   - **Thu nhập thêm dự kiến**: Nhập số tiền thu nhập thêm bạn dự kiến
   - **Tỷ lệ tiết kiệm**: Nhập % tiết kiệm (0-100%)
5. Nhấn **Lưu ngân sách**

### 4.2 Copy ngân sách từ tháng trước (Case C)

1. Vào **Chức năng** → Chọn **Ngân sách**
2. Nếu tháng trước có ngân sách, app sẽ hỏi có muốn copy không
3. Chọn **Copy từ tháng trước**
4. App tự động điền các giá trị từ tháng trước
5. Điều chỉnh nếu cần
6. Nhấn **Lưu ngân sách**

### 4.3 Xem tổng quan ngân sách (Case B)

1. Vào **Chức năng** → Chọn **Ngân sách**
2. Nếu tháng hiện tại đã có ngân sách, app sẽ mở màn hình **Tổng quan**
3. Xem các thông tin:
   - **Tổng thu nhập**: Thu nhập định kỳ + Thu nhập thêm
   - **Tổng chi tiêu**: Chi tiêu cố định + Chi tiêu hàng ngày
   - **Tiết kiệm**: Số tiền tiết kiệm
   - **Còn lại**: Số tiền còn lại sau khi trừ chi tiêu và tiết kiệm
   - **Thanh toán nợ**: Các khoản trả nợ ngân hàng
   - **Phân tích theo danh mục**: Chi tiết chi tiêu hàng ngày theo từng danh mục

### 4.4 Xem lịch sử ngân sách

1. Vào **Chức năng** → Chọn **Ngân sách**
2. Chọn **Lịch sử** từ menu
3. Xem danh sách ngân sách các tháng đã lập
4. Nhấn vào tháng để xem chi tiết

### 4.5 Xem chi tiết chi tiêu theo danh mục

1. Vào màn hình **Tổng quan ngân sách**
2. Cuộn xuống phần **Phân tích theo danh mục**
3. Nhấn vào một danh mục
4. Xem danh sách các khoản chi tiêu trong danh mục đó

## 5. Minh hoạ giao diện (Wireframe)

### 5.1 Màn hình Lập ngân sách (BudgetSetup)

```text
┌─────────────────────────────────────────┐
│  ← Quay lại    Lập ngân sách 11/2024    │
├─────────────────────────────────────────┤
│  Thu nhập định kỳ                        │
│  10,000,000 đ                            │
│  (Dữ liệu này tự động lấy từ hệ thống)  │
│                                         │
│  Chi tiêu cố định                        │
│  5,000,000 đ                             │
│  (Dữ liệu này tự động lấy từ hệ thống)  │
│                                         │
│  Thu nhập thêm dự kiến                   │
│  Bạn dự kiến thu nhập thêm mỗi tháng?   │
│  [2,000,000] đ                           │
│  (Gồm bán hàng online, freelance...)    │
│                                         │
│  Ngân sách tổng (trước tiết kiệm)       │
│  12,000,000 đ                            │
│                                         │
│  Tỷ lệ tiết kiệm (%)                     │
│  Bạn muốn tiết kiệm bao nhiêu?          │
│  [20] %                                  │
│  Tương ứng: 2,400,000 đ                 │
│                                         │
│  [Lưu ngân sách]                        │
└─────────────────────────────────────────┘
```

### 5.2 Màn hình Tổng quan (BudgetOverview)

```text
┌─────────────────────────────────────────┐
│  ← Quay lại    Tổng quan 11/2024        │
├─────────────────────────────────────────┤
│  ┌───────────────────────────────────┐ │
│  │ Tổng thu nhập                      │ │
│  │ 12,000,000 đ                       │ │
│  │                                    │ │
│  │ - Thu nhập định kỳ: 10,000,000 đ  │ │
│  │ - Thu nhập thêm: 2,000,000 đ      │ │
│  └───────────────────────────────────┘ │
│                                         │
│  ┌───────────────────────────────────┐ │
│  │ Tổng chi tiêu                      │ │
│  │ 7,500,000 đ                        │ │
│  │                                    │ │
│  │ - Chi tiêu cố định: 5,000,000 đ   │ │
│  │ - Chi tiêu hàng ngày: 2,500,000 đ │ │
│  │                                    │ │
│  │ [████████░░░░] 75%                │ │
│  └───────────────────────────────────┘ │
│                                         │
│  ┌───────────────────────────────────┐ │
│  │ Tiết kiệm                           │ │
│  │ 2,400,000 đ                        │ │
│  │ (20%)                              │ │
│  └───────────────────────────────────┘ │
│                                         │
│  ┌───────────────────────────────────┐ │
│  │ Còn lại                             │ │
│  │ 2,100,000 đ                        │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Phân tích theo danh mục                │
│  ┌───────────────────────────────────┐ │
│  │ Ăn ngoài: 800,000 đ               │ │
│  │ [████████░░] 32%                  │ │
│  └───────────────────────────────────┘ │
│  ┌───────────────────────────────────┐ │
│  │ Mua sắm: 500,000 đ                │ │
│  │ [█████░░░░░] 20%                  │ │
│  └───────────────────────────────────┘ │
│                                         │
│  [Lịch sử] [Sửa ngân sách]             │
└─────────────────────────────────────────┘
```

### 5.3 Màn hình Lịch sử (BudgetHistory)

```text
┌─────────────────────────────────────────┐
│  ← Quay lại    Lịch sử ngân sách        │
├─────────────────────────────────────────┤
│  ┌───────────────────────────────────┐ │
│  │ 11/2024                            │ │
│  │ Thu: 12,000,000 đ                  │ │
│  │ Chi: 7,500,000 đ                   │ │
│  │ Tiết kiệm: 2,400,000 đ             │ │
│  │ [Xem chi tiết]                     │ │
│  └───────────────────────────────────┘ │
│                                         │
│  ┌───────────────────────────────────┐ │
│  │ 10/2024                            │ │
│  │ Thu: 10,000,000 đ                  │ │
│  │ Chi: 6,000,000 đ                   │ │
│  │ Tiết kiệm: 2,000,000 đ             │ │
│  │ [Xem chi tiết]                     │ │
│  └───────────────────────────────────┘ │
└─────────────────────────────────────────┘
```

## 6. Logic & quy tắc

### 6.1 Các trường hợp (Cases)

- **Case A**: Lập ngân sách lần đầu (chưa có ngân sách tháng nào)
- **Case B**: Tháng hiện tại đã có ngân sách → Xem tổng quan
- **Case C**: Tháng hiện tại chưa có, nhưng tháng trước có → Gợi ý copy

### 6.2 Tự động tính toán

- **Thu nhập định kỳ**: Tổng từ tất cả `recurring_income` đang hoạt động
- **Chi tiêu cố định**: Tổng từ tất cả `recurring_expense` đang hoạt động
- **Chi tiêu hàng ngày**: Tổng từ `daily_expense` trong tháng
- **Ngân sách tổng**: Thu nhập định kỳ + Thu nhập thêm
- **Tiết kiệm**: Ngân sách tổng × Tỷ lệ tiết kiệm

### 6.3 Tích hợp với các module khác

- Khi xác nhận thu nhập định kỳ → Tự động cập nhật ngân sách
- Khi xác nhận chi tiêu cố định → Tự động cập nhật ngân sách
- Chi tiêu hàng ngày được tính vào ngân sách tự động

### 6.4 Cảnh báo vượt ngân sách

- App sẽ hiển thị cảnh báo khi chi tiêu vượt quá ngân sách
- Cảnh báo hiển thị ở màn hình Home và trong thông báo

### 6.5 Snapshot

- Khi lập ngân sách, app tạo snapshot của các khoản thu/chi để lưu lại trạng thái tại thời điểm đó
- Snapshot được dùng để so sánh và phân tích

## 7. Lưu ý quan trọng

- **Mỗi tháng một ngân sách**: Bạn cần lập ngân sách cho mỗi tháng
- **Không thể sửa ngân sách đã lập**: Bạn chỉ có thể xem, không thể sửa ngân sách đã lập (để đảm bảo tính chính xác)
- **Tự động cập nhật**: Ngân sách tự động cập nhật khi bạn xác nhận thu nhập/chi tiêu
- **Copy từ tháng trước**: Tính năng copy giúp bạn tiết kiệm thời gian lập ngân sách

## 8. Mapping kỹ thuật (for dev)

### 8.1 Routes / Route Names

- `BudgetSetup` - Lập ngân sách (param: `mode?: 'copy' | 'new'`, `previousMonthBudget?: Budget`)
- `BudgetOverview` - Tổng quan (có thể truy cập từ Home hoặc Functions)
- `BudgetHistory` - Lịch sử
- `BudgetCopySuggestion` - Gợi ý copy (internal, không có route riêng)

### 8.2 Screen File Paths

- `src/screens/finance/BudgetSetupScreen.tsx`
- `src/screens/finance/BudgetOverviewScreen.tsx`
- `src/screens/finance/BudgetHistoryScreen.tsx`
- `src/screens/finance/BudgetCopySuggestionScreen.tsx`

### 8.3 Services / Repos File Paths

- `src/modules/finance/services/budget.service.ts` - `checkBudgetStatus`, `saveBudget`, `getBudgetOverview`, `calculatePlanIncome`, `calculatePlanExpense`
- `src/data/repo/budget.repository.ts` - `budgetRepo`
- `src/data/repo/budget-item-snapshot.repository.ts` - `budgetItemSnapshotRepo`
- Tích hợp với:
  - `recurringIncomeRepo`, `recurringExpenseRepo`
  - `dailyExpenseRepo`
  - `bankDebtRepo`, `bankDebtPaymentRepo`

### 8.4 DB Tables / Models

- `budget` - Bảng ngân sách
  - `id`, `user_id`, `month` (YYYY-MM), `additional_income`, `savings_percentage`, `created_at`, `updated_at`
- `budget_item_snapshot` - Bảng snapshot các khoản thu/chi
  - `id`, `budget_id`, `item_type` (INCOME/EXPENSE), `item_name`, `amount`, `cycle`, `times`, `order`

### 8.5 i18n Keys

- `finance.budget_management` - "Ngân sách"
- `finance.budget_setup.setup.title` - "Lập ngân sách tháng {{month}}"
- `finance.budget_setup.overview.title` - "Tổng quan ngân sách {{month}}"
- `finance.budget_setup.history.title` - "Lịch sử ngân sách"
- `finance.budget_setup.setup.fixed_income` - "Thu nhập định kỳ"
- `finance.budget_setup.setup.fixed_expense` - "Chi tiêu cố định"
- `finance.budget_setup.setup.additional_income_label` - "Bạn dự kiến thu nhập thêm mỗi tháng là?"
- `finance.budget_setup.setup.savings_label` - "Bạn muốn tiết kiệm bao nhiêu?"
- Và nhiều keys khác trong `src/i18n/locales/vi.json` dưới key `finance.budget_setup`


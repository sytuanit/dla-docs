# Mục tiêu tài chính

## 1. Mục đích

Module **Mục tiêu tài chính** giúp bạn:
- Đặt mục tiêu tài chính (ví dụ: mua nhà, mua xe)
- Lập kế hoạch tài chính để đạt mục tiêu
- Đánh giá các giả định tài chính
- So sánh các kịch bản vay
- Theo dõi tiến độ đạt mục tiêu

## 2. Khi nào nên dùng

Sử dụng module này khi bạn muốn:
- Lập kế hoạch cho một mục tiêu tài chính lớn
- Đánh giá khả năng vay để mua tài sản
- So sánh các phương án tài chính
- Theo dõi tiến độ tiết kiệm

## 3. Các màn hình liên quan

- **CreateFinancialGoal** - Tạo mục tiêu tài chính (3 bước)
- **FinancialGoalDetail** - Chi tiết mục tiêu và các kế hoạch
- **ViewLoanPlan** - Xem kế hoạch vay
- **AssumptionEvaluation** - Đánh giá giả định
- **AssumptionAndLoanEvaluation** - Đánh giá giả định và vay

## 4. Cách sử dụng chính

### 4.1 Tạo mục tiêu tài chính (3 bước)

#### Bước 1: Kế hoạch tài chính

1. Vào **Chức năng** → Chọn **Mục tiêu tài chính**
2. Nhấn nút **+** (FAB)
3. Điền thông tin:
   - **Thu nhập hàng tháng**: Tổng thu nhập dự kiến
   - **Chi tiêu cố định**: Tổng chi tiêu cố định
   - **Chi tiêu sinh hoạt**: Chi tiêu sinh hoạt hàng tháng
   - **Số dư hiện tại**: Số tiền hiện có
4. Xem dự báo:
   - Sau 12 tháng
   - Sau 24 tháng
   - Sau 36 tháng
5. Nhấn **Tiếp theo**

#### Bước 2: Mục tiêu

1. Điền thông tin mục tiêu:
   - **Tên mục tiêu**: (ví dụ: "Mua nhà")
   - **Số tiền mục tiêu**: Số tiền cần để đạt mục tiêu
   - **Số tiền trả trước**: Số tiền đặt cọc/trả trước
   - **Số dư ban đầu**: Số tiền đã có sẵn
2. Xem thông tin:
   - Số tiền còn thiếu
   - Thời gian ước tính để đạt mục tiêu
3. Nhấn **Tiếp theo**

#### Bước 3: Tạo kế hoạch

1. Chọn loại kế hoạch:
   - **Chỉ vay**: Đánh giá khả năng vay
   - **Chỉ giả định**: Đánh giá giả định tài chính
   - **Giả định và vay**: Kết hợp cả hai
2. Nhấn **Tạo kế hoạch**
3. Điền thông tin chi tiết cho từng loại kế hoạch
4. Nhấn **Lưu**

### 4.2 Xem chi tiết mục tiêu

1. Vào danh sách mục tiêu tài chính
2. Nhấn vào mục tiêu
3. Xem thông tin:
   - Thông tin mục tiêu
   - Các kế hoạch đã tạo
   - Tiến độ đạt mục tiêu

### 4.3 Tạo kế hoạch mới

1. Vào chi tiết mục tiêu
2. Nhấn **Tạo kế hoạch mới**
3. Chọn loại kế hoạch
4. Điền thông tin và lưu

### 4.4 Xem kế hoạch vay

1. Vào chi tiết mục tiêu
2. Nhấn vào một kế hoạch vay
3. Xem:
   - Lịch trả nợ
   - Tổng số tiền phải trả
   - So sánh với các kế hoạch khác

## 5. Minh hoạ giao diện (Wireframe)

### 5.1 Màn hình Tạo mục tiêu (Bước 1 - Kế hoạch tài chính)

```text
┌─────────────────────────────────────────┐
│  ← Quay lại    Tạo mục tiêu (1/3)       │
├─────────────────────────────────────────┤
│  Kế hoạch tài chính                     │
│                                         │
│  Thu nhập hàng tháng *                   │
│  [12,000,000] đ                          │
│                                         │
│  Chi tiêu cố định *                      │
│  [5,000,000] đ                           │
│                                         │
│  Chi tiêu sinh hoạt *                    │
│  [3,000,000] đ                           │
│                                         │
│  Số dư hiện tại *                        │
│  [50,000,000] đ                          │
│                                         │
│  Dự báo                                  │
│  ┌───────────────────────────────────┐ │
│  │ Sau 12 tháng: 98,000,000 đ         │ │
│  │ Sau 24 tháng: 146,000,000 đ        │ │
│  │ Sau 36 tháng: 194,000,000 đ        │ │
│  └───────────────────────────────────┘ │
│                                         │
│  [Tiếp theo] [Hủy]                      │
└─────────────────────────────────────────┘
```

### 5.2 Màn hình Chi tiết (FinancialGoalDetail)

```text
┌─────────────────────────────────────────┐
│  ← Quay lại    Mục tiêu: Mua nhà        │
├─────────────────────────────────────────┤
│  Thông tin mục tiêu                      │
│  ┌───────────────────────────────────┐ │
│  │ Số tiền mục tiêu: 2,000,000,000 đ │ │
│  │ Số tiền trả trước: 400,000,000 đ  │ │
│  │ Số dư ban đầu: 50,000,000 đ       │ │
│  │ Còn thiếu: 350,000,000 đ          │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Tiến độ                                 │
│  [████░░░░░░] 14%                        │
│                                         │
│  Các kế hoạch                            │
│  ┌───────────────────────────────────┐ │
│  │ Kế hoạch vay 1                     │ │
│  │ Vay 1,600,000,000 đ                │ │
│  │ Lãi suất: 8.5%/năm                 │ │
│  │ [Xem chi tiết]                     │ │
│  └───────────────────────────────────┘ │
│  ┌───────────────────────────────────┐ │
│  │ Giả định tài chính 1                │ │
│  │ Tăng thu nhập 20%                  │ │
│  │ [Đánh giá]                         │ │
│  └───────────────────────────────────┘ │
│                                         │
│  [Tạo kế hoạch mới] [Sửa] [Xóa]         │
└─────────────────────────────────────────┘
```

## 6. Logic & quy tắc

### 6.1 Tính toán dự báo

- Dự báo dựa trên:
  - Thu nhập - Chi tiêu cố định - Chi tiêu sinh hoạt = Tiết kiệm/tháng
  - Số dư hiện tại + (Tiết kiệm/tháng × Số tháng)

### 6.2 Mục tiêu

- Số tiền còn thiếu = Số tiền trả trước - Số dư ban đầu
- Thời gian ước tính = Số tiền còn thiếu / Tiết kiệm/tháng

### 6.3 Kế hoạch vay

- Tính toán dựa trên:
  - Số tiền vay
  - Lãi suất
  - Kỳ hạn
  - Tạo lịch trả nợ tự động

### 6.4 Giả định tài chính

- Đánh giá các giả định như:
  - Tăng/giảm thu nhập
  - Tăng/giảm chi tiêu
  - Thay đổi lãi suất
- Xem ảnh hưởng đến khả năng đạt mục tiêu

## 7. Lưu ý quan trọng

- **Dự báo chỉ mang tính tham khảo**: Dựa trên giả định thu nhập và chi tiêu ổn định
- **Có thể tạo nhiều kế hoạch**: Bạn có thể tạo nhiều kế hoạch để so sánh
- **Kế hoạch vay**: Tự động tính toán lịch trả nợ dựa trên thông tin vay

## 8. Mapping kỹ thuật (for dev)

### 8.1 Routes / Route Names

- `CreateFinancialGoal` - Tạo mục tiêu (3 bước)
- `FinancialGoalDetail` - Chi tiết (param: `goalId`)
- `ViewLoanPlan` - Xem kế hoạch vay (param: `scenarioId`)
- `AssumptionEvaluation` - Đánh giá giả định (param: `assumptionId`)
- `AssumptionAndLoanEvaluation` - Đánh giá kết hợp (param: `goalId`)

### 8.2 Screen File Paths

- `src/screens/finance/CreateFinancialGoalScreen.tsx`
- `src/screens/finance/FinancialGoalDetailScreen.tsx`
- `src/screens/finance/ViewLoanPlanScreen.tsx`
- `src/screens/finance/AssumptionEvaluationScreen.tsx`
- `src/screens/finance/AssumptionAndLoanEvaluationScreen.tsx`

### 8.3 Services / Repos File Paths

- `src/data/repo/financial-goal.repository.ts` - `financialGoalRepo`
- `src/data/repo/loan-scenario.repository.ts` - `loanScenarioRepo`
- `src/data/repo/financial-assumption.repository.ts` - `financialAssumptionRepo`
- `src/modules/finance/services/planning-assumptions.service.ts` - `calculateAverageFinancialData`

### 8.4 DB Tables / Models

- `financial_goal` - Bảng mục tiêu tài chính
  - `id`, `user_id`, `name`, `target_amount`, `down_payment`, `initial_balance`, `income`, `fixed_expense`, `living_expense`
- `loan_scenario` - Bảng kế hoạch vay
  - `id`, `goal_id`, `principal_amount`, `interest_rate`, `term_years`, `monthly_payment`
- `financial_assumption` - Bảng giả định tài chính
  - `id`, `goal_id`, `assumption_type`, `value`, `description`

### 8.5 i18n Keys

- `finance.planning_assumptions_module.goal_detail.title` - "Mục tiêu tài chính"
- `finance.planning_assumptions_module.create_goal.step1.title` - "Kế hoạch tài chính"
- `finance.planning_assumptions_module.create_goal.step2.title` - "Mục tiêu"
- `finance.planning_assumptions_module.create_goal.step3.title` - "Tạo kế hoạch"
- Và nhiều keys khác trong `src/i18n/locales/vi.json` dưới key `finance.planning_assumptions_module`


# 路由設計：個人記帳本

這份文件定義了系統中所有的 URL 路由（Routes），包含每個路由的 HTTP 請求方法、負責處理的邏輯以及對應的 HTML 模板。

## 1. 路由總覽表格

| 功能 | HTTP 方法 | URL 路徑 | 對應模板 | 說明 |
| --- | --- | --- | --- | --- |
| 首頁 (當月總覽與新增) | GET | `/` | `templates/index.html` | 顯示當月總收入、總支出與新增收支表單 |
| 建立收支紀錄 | POST | `/records` | — | 接收首頁表單資料，存入 DB 後重導向至首頁 |
| 歷史收支明細 | GET | `/records` | `templates/history.html` | 顯示所有的收支紀錄列表 |
| 編輯紀錄頁面 | GET | `/records/<int:record_id>/edit`| `templates/edit.html` | 顯示特定一筆收支紀錄的編輯表單 |
| 更新收支紀錄 | POST | `/records/<int:record_id>/update`| — | 接收編輯表單資料，更新 DB 後重導向至歷史明細 |
| 刪除收支紀錄 | POST | `/records/<int:record_id>/delete`| — | 刪除指定的收支紀錄，完成後重導向至歷史明細 |

## 2. 每個路由的詳細說明

### 首頁 (`GET /`)
- **輸入**：無
- **處理邏輯**：
  1. 呼叫 `RecordModel.get_all()` 獲取資料。
  2. 篩選出「當月」的紀錄，計算出總收入、總支出與結餘。
- **輸出**：渲染 `index.html` 並傳遞計算結果。

### 建立收支紀錄 (`POST /records`)
- **輸入**：表單欄位（`type`, `date`, `amount`, `category`, `description`）
- **處理邏輯**：
  1. 驗證表單資料是否齊全與格式是否正確。
  2. 呼叫 `RecordModel.create(...)` 寫入資料庫。
- **輸出**：重新導向 (`redirect`) 到首頁 `/`。
- **錯誤處理**：若資料有誤，回傳錯誤訊息並重導回首頁。

### 歷史收支明細 (`GET /records`)
- **輸入**：無
- **處理邏輯**：呼叫 `RecordModel.get_all()` 取得所有歷史紀錄。
- **輸出**：渲染 `history.html` 並傳遞資料列表。

### 編輯紀錄頁面 (`GET /records/<int:record_id>/edit`)
- **輸入**：URL 參數 `record_id`
- **處理邏輯**：呼叫 `RecordModel.get_by_id(record_id)` 取得該筆資料。
- **輸出**：渲染 `edit.html` 並傳遞該筆紀錄資料填入表單預設值。
- **錯誤處理**：若找不到該 `record_id`，回傳 404 頁面或重導向。

### 更新收支紀錄 (`POST /records/<int:record_id>/update`)
- **輸入**：URL 參數 `record_id` 與表單欄位（更新後的 `type`, `date` 等）
- **處理邏輯**：呼叫 `RecordModel.update(...)` 更新該筆資料。
- **輸出**：重新導向 (`redirect`) 到歷史明細頁 `/records`。

### 刪除收支紀錄 (`POST /records/<int:record_id>/delete`)
- **輸入**：URL 參數 `record_id`
- **處理邏輯**：呼叫 `RecordModel.delete(record_id)` 刪除該筆資料。
- **輸出**：重新導向 (`redirect`) 到歷史明細頁 `/records`。

## 3. Jinja2 模板清單

所有 HTML 模板檔案將存放在 `app/templates/` 目錄下：

1. `base.html`：**共用版型**，包含全域的 CSS 引入、導覽列（首頁、歷史明細等連結）。
2. `index.html`：繼承 `base.html`，顯示當月記帳總表與**新增收支表單**。
3. `history.html`：繼承 `base.html`，顯示所有收支的表格或列表。
4. `edit.html`：繼承 `base.html`，顯示單筆紀錄的**編輯表單**。

## 4. 路由骨架程式碼

程式碼骨架已產出至 `app/routes/` 目錄，使用 Flask Blueprint 實作，詳細內容請參考對應檔案。

# Wiki 文件 schema

此 Wiki 的 Markdown 筆記使用 YAML frontmatter，讓人和 LLM 都能辨識文件類型、來源和版本。GitHub 可直接瀏覽相對連結；本地筆記軟體也能讀取 Markdown。

| 欄位 | 用途 |
|---|---|
| `id` | 固定 ID：來源 S1–S5、概念 W1–W5、統整 T1。 |
| `type` | `source_note`、`concept`、`synthesis`。 |
| `title` | 顯示名稱。 |
| `source_ids` | 支持本文的原始來源 ID 陣列。 |
| `updated` | 最後整理日期。 |
| `status` | `verified`、`needs_review`。 |

每條可用事實以 `S1-F1` 等 ID 標記；概念頁必須寫出對應事實 ID。若兩篇資料說法不同，保留各自的主張與限定語，不能因為需要簡報而強行合併。推論必須明標「教學歸納」；無根據的說法寫在「不採用」而非簡報主文。

## 資料路徑

`raw/papers/Sx-*.md` → `wiki/papers/Sx-*.md` → `wiki/concepts/*.md` → `wiki/syntheses/lesson-outline.md` → `slides.html`

查詢與 QA 紀錄分別放在 `tasks/slide-query.md`、`tasks/qa-runs.md`；每輪 ingest 追加到 `log.md`。

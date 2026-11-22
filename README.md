# 聖誕節入門｜第十週作業

本專案依照 `instruction.md` 製作：以五篇資料建立**多檔案聖誕節 LLM Wiki**，再根據 Wiki 製作 10 頁教學型 HTML 簡報。另附 `AGENTS.md` 工作規格、分批 ingest 的 Git 紀錄、loop / graph、一次執行的檢查紀錄與反思。沒有使用 Antigravity。

## 直接瀏覽

- [線上成果首頁](https://peter-owo.github.io/week10hw/)
- [成果首頁](index.html)
- [LLM Wiki 展示頁](wiki.html)／[多檔案 Wiki 入口](wiki/index.md)
- [教學 HTML 簡報](slides.html)
- [製作流程與反思](process.html)／[完整紀錄](process.md)
- [可複製的繳交內容](submission.md)

下載專案後雙擊 `index.html` 即可離線瀏覽；外部來源連結需要網路。簡報可用左右方向鍵、頁面底部按鈕切換，也可透過瀏覽器列印為 PDF。

## 資料來源與對應

| Wiki | 內容 | 簡報 |
|---|---|---|
| W1 | 節日意義與 12 月 25 日 | 第 2–3 頁 |
| W2 | 聖誕樹與 19 世紀習俗 | 第 4 頁 |
| W3 | 聖誕老人形象的演變 | 第 5 頁 |
| W4 | Las Posadas | 第 6 頁 |
| W5 | 聖誕紅與文化傳播 | 第 7 頁 |

五篇原始資料的標題、連結和擷取方式分別列在 [`raw/papers/`](raw/papers/)。每篇有自己的 [`wiki/papers/`](wiki/papers/) 閱讀筆記，再形成 [`wiki/concepts/`](wiki/concepts/) 概念頁；[簡報查詢紀錄](wiki/tasks/slide-query.md) 記下逐頁使用哪些主張。`wiki.md` 是方便快速閱讀的單檔摘要，不是 Wiki 本體。所有 HTML、CSS、JavaScript 均為本專案內容，不依賴框架或線上字型。

## LLM Wiki 目錄架構

```text
AGENTS.md              AI 工作規格、檢查與循環規則
raw/papers/            5 篇來源卡（S1–S5）
wiki/index.md          知識庫入口
wiki/schema.md         筆記 frontmatter 與 ID 規格
wiki/log.md            分批 ingest 與修正紀錄
wiki/papers/           5 篇逐篇閱讀筆記
wiki/concepts/         5 個概念頁（W1–W5）
wiki/syntheses/        教學簡報大綱
wiki/tasks/            Wiki 查詢、QA 規格與執行紀錄
```

在初版網站後，本次重構以 1–2 篇一批提交來源與 Wiki 筆記：第一批 `d51e46e`（S1–S2）、第二批 `c95291c`（S3–S4）、第三批 `f303b01`（S5）。

## 專案檔案

| 檔案 | 用途 |
|---|---|
| `index.html` | 成果入口 |
| `wiki.html` | 可搜尋的 Wiki 頁面 |
| `slides.html` | 教學簡報 |
| `process.html` | 流程與反思網頁 |
| `AGENTS.md` | AI 使用 Wiki 與產生簡報的工作規格 |
| `raw/papers/` | 五篇資料的來源卡 |
| `wiki/` | 分層、多檔案知識庫 |
| `wiki.md` | 單檔閱讀摘要 |
| `process.md` | graph、實際執行、檢查紀錄與反思 |
| `submission.md` | 線上繳交欄位可用文字 |

作者的學校、學號、系級與姓名尚未提供，因此繳交標題在 `submission.md` 留有待填欄位。

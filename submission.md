# 可複製到線上作業欄位的繳交內容

> **請先把標題中的個人資料填上。**目前沒有提供學校、學號、系級與姓名，因此不代填。

## 繳交標題

`【學校簡稱】 【學號】 【系級簡稱】 【姓名】 聖誕節入門`

## 繳交內容

**LLM Wiki 主題與介紹**：聖誕節入門。先討論初學者需要回答的問題，再分三批 ingest 5 篇資料：S1–S2、S3–S4、S5。`raw/papers/` 保存來源卡，`wiki/papers/` 保存逐篇閱讀筆記，`wiki/concepts/` 保存 W1–W5 五個概念頁；另有 `AGENTS.md`、schema、ingest 日誌、簡報查詢與 QA 紀錄。主題涵蓋節日意義、日期、聖誕樹、聖誕老人、Las Posadas 與聖誕紅。

**LLM Wiki 成果**：[互動展示頁](https://peter-owo.github.io/week10hw/wiki.html)；[多檔案 Wiki 入口](https://github.com/peter-owo/week10hw/blob/main/wiki/index.md)；[完整 Wiki 目錄](https://github.com/peter-owo/week10hw/tree/main/wiki)；[AI 工作規格 AGENTS.md](https://github.com/peter-owo/week10hw/blob/main/AGENTS.md)。

**教學 HTML 簡報**：[聖誕節是什麼？10 頁教學簡報](https://peter-owo.github.io/week10hw/slides.html)。

**Loop / graph**：討論需求並寫入 `AGENTS.md` → 分批搜尋與建立 `raw/papers/` 來源卡 → 寫入 `wiki/papers/` 閱讀筆記 → 檢查主張和限定語 → 建立 `wiki/concepts/` → 查詢 Wiki 並寫簡報大綱 → 產生 HTML → 執行程式與內容檢查。來源不合格時返回搜尋；Wiki 主張缺乏依據時返回來源或筆記；簡報內容超出 Wiki 時返回統整稿；介面問題則修正 HTML。完整流程見[流程頁](https://peter-owo.github.io/week10hw/process.html)。

**一次實際執行與檢查紀錄**：5 篇來源以 1–2 篇一批匯入，Git commit 為 `d51e46e`、`c95291c`、`f303b01`。檢查 W1 時把「12 月 25 日」限定為慶祝日期，沒有寫成已證實生日；W3 避免聖誕老人單一起源論；W4 限定 Las Posadas 的適用地區。第一次執行 `python validate.py` 找到 QA 紀錄檔缺漏，補上後第二次通過；第三輪又以可讀全文交叉查核 S1、S4 的關鍵說法，重新執行仍通過。S1、S4 的主要來源對自動開啟有限制，已在來源卡明示。詳細紀錄見[QA 輪次](https://github.com/peter-owo/week10hw/blob/main/wiki/tasks/qa-runs.md)與[process.md](https://github.com/peter-owo/week10hw/blob/main/process.md)。

**反思**：最常出錯的是 `raw → wiki/papers` 的摘要節點，容易把不確定或地方性的事寫成絕對結論。我把事實檢查前移到來源卡與逐篇筆記之間，加入「來源是否直接支持？語氣是否過度肯定？」的檢查閘門；不通過就回到來源或筆記。這次也把原本的單檔摘要重構為 `raw → papers → concepts → syntheses` 的 Wiki graph。

**程式與全部成果**：[GitHub 專案](https://github.com/peter-owo/week10hw)。

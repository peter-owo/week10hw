# 實際 QA 輪次紀錄

檢查規格見 [`qa-plan.md`](qa-plan.md)。記錄本次多檔案重構後實際執行的檢查，不把未操作的項目寫成通過。

## 第 1 輪｜結構檢查失敗

- **執行**：`python validate.py`。
- **結果**：`FAIL`。缺少 `wiki/tasks/qa-runs.md`，且 `qa-plan.md`、`tasks/README.md` 對它的兩個相對連結因此失效。
- **定位**：問題在 Wiki 工作紀錄層，不在來源內容或簡報頁面。
- **修正**：建立本檔記錄實際輪次；其餘已通過項目不重寫。

## 第 2 輪｜結構與程式檢查通過

- **執行**：再次執行 `python validate.py`。
- **結果**：`PASS: 5 raw sources, 5 reading notes, 5 concept pages, traceable claims, Wiki architecture, 10 slides, local links and JavaScript syntax`。
- **實際覆蓋**：五張來源卡、五篇閱讀筆記與五個概念頁均存在；每層都有 `Sx-F1` 至 `Sx-F3` 追溯 ID；Markdown 相對連結存在；10 頁簡報中，第 2–7 頁都有對應 Wiki W 編號與原始來源連結；四個 HTML 頁面的相對連結與內嵌 JavaScript 語法通過。
- **人工內容抽查**：第 3 頁的 336 年與「慶祝日期不等於確切生日」對應 W1；第 5 頁兩角色融合對應 W3；第 6 頁用「西班牙與許多拉丁美洲地區」對應 W4；第 7 頁植物原生地和英文名稱對應 W5。第 8 頁為大綱 T1 明標的教學歸納；第 9 頁的錯誤選項對應 W1、W4 的限定語。
- **未涵蓋**：自動程式不能證明所有歷史主張的學術正確性；S1、S4 的來源網站對自動開啟回傳 403，這兩張來源卡只使用館方搜尋索引摘要。

## 第 3 輪｜針對來源限制補查

- **問題**：第 2 輪通過程式檢查，但 S1、S4 只能取得館方搜尋索引摘要，來源完整性仍可加強。
- **修正**：在 S1 來源卡與閱讀筆記加入可讀全文的[利物浦大學歷史系文章](https://www.liverpool.ac.uk/history/blog/2023/first-noel/)交叉檢查四世紀羅馬日期；在 S4 加入可讀全文的[美國國會圖書館文章](https://blogs.loc.gov/law/2011/12/a-state-mandated-christmas-bonus/)交叉檢查墨西哥 posadas 的九晚安排。兩個主要來源的擷取限制仍明示，沒有假稱讀到全文。
- **重新執行**：`python validate.py` 再次輸出 `PASS: 5 raw sources, 5 reading notes, 5 concept pages, traceable claims, Wiki architecture, 10 slides, local links and JavaScript syntax`。
- **範圍**：這輪只補查來源卡與相關閱讀筆記，簡報沒有新增主張，因此不重寫已通過的頁面。

## 停止判斷

結構、來源追溯、連結、頁數和程式檢查已通過；第 1 輪的紀錄檔缺漏在第 2 輪修復，第 3 輪補強了來源交叉查核，符合 `AGENTS.md` 的停止條件。視覺渲染另有瀏覽器截圖證據，詳見 [`../../process.md`](../../process.md)。

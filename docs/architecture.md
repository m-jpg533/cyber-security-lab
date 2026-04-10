# 🧠 系統架構說明（Architecture）

本專案為一個**資安教學模擬平台**，展示基本的 C2（Command & Control）架構。

---

## 🏗️ 整體架構

Client（模擬電腦） → C2 Server（Flask） → SOC Dashboard（監控）

---

## 🔄 資料流程

1️⃣ Client 每 5 秒向 Server 請求指令

* API：`/get_command`

2️⃣ Server 回傳指令（例如：info）

3️⃣ Client 執行指令並回報資料

* API：`/report`

4️⃣ Server 儲存 Client 狀態

5️⃣ SOC 面板讀取資料

* API：`/clients`

---

## 🧩 系統組成

### 🟢 C2 Server

* 使用 Flask 建立 API
* 負責：

  * 指令分發
  * Client 管理
  * 資料接收

---

### 🤖 Client Simulator

* 模擬受控電腦
* 功能：

  * 定期請求指令
  * 回報系統資訊

---

### 📊 SOC Dashboard

* Web 介面
* 顯示：

  * 在線 Client
  * 回報資料
  * 控制指令

---

## ⚠️ 安全聲明

本專案僅用於學習與測試用途，
請勿用於未授權環境或任何非法行為。

---

## 🚀 未來擴展

* 🔐 Token 驗證
* 📡 WebSocket 即時通訊
* 📊 圖表分析
* 🧠 多指令隊列

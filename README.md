# openai_ner
隱私保護與醫學數據標準化競賽：解碼臨床病例、讓數據說故事

## 環境
* 作業系統：Windows 11 專業版 Insider Preview
* CPU：12th Gen Intel(R) Core(TM) i9-12900   2.40 GHz
* RAM : 32.0 GB
* 程式語言：Python 3.11.5
* 文字編輯器 : vscode 1.84.2


# model 8NYtED1H
## score 
| Coding Type | Precision | Recall | F-measure | Support |
|-------------|----------:|:------:|----------:|--------:|
| MEDICALRECORD | 0.7856389 | 0.995984 | 0.8783943 | 747 |
| PATIENT | 0.993007 | 0.9916201 | 0.9923131 | 716 |
| IDNUM | 0.983932 | 0.9820755 | 0.9830028 | 2120 |
| DATE | 0.9737719 | 0.9511997 | 0.9623534 | 2459 |
| DOCTOR | 0.965736 | 0.9149384 | 0.9396512 | 3327 |
| STREET | 0.9884393 | 0.994186 | 0.9913044 | 344 |
| CITY | 0.986376 | 0.9705094 | 0.9783784 | 373 |
| STATE | 0.9969605 | 0.9879518 | 0.9924357 | 332 |
| ZIP | 1 | 0.9943343 | 0.9971591 | 353 |
| TIME | 0.9251102 | 0.893617 | 0.9090909 | 470 |
| DEPARTMENT | 0.8968059 | 0.8711217 | 0.8837772 | 419 |
| HOSPITAL | 0.8926746 | 0.8747913 | 0.8836425 | 1198 |
| DURATION | 0.7142857 | 0.8333333 | 0.7692307 | 12 |
| ORGANIZATION | 0.7010309 | 0.9189189 | 0.7953216 | 74 |
| AGE | 0.9591837 | 0.9215686 | 0.9400001 | 51 |
| SET | 0.6666667 | 0.4 | 0.5 | 5 |
| LOCATION-OTHER | 1 | 0.1666667 | 0.2857143 | 6 |
| URL | 0 | 0 | 0 | 0 |
| ROOM | 0 | 0 | 0 | 0 |
| PHONE | 0 | 0 | 0 | 1 |
| Micro-avg. F| 0.9486346 | 0.9428 | 0.9457083 | 13007 |
| Macro-avg. F| 0.7714809 | 0.7331408 | 0.7518224 | 13007 |
|-------------|----------:|:------:|----------:|----------:|
|-------------|----------:|:------:|----------:|----------:|
| Temporal Type | Precision | Recall | F-measure | Support |
|-------------|----------:|:------:|----------:|----------:|
| DATE | 0.8648995 | 0.8226922 | 0.843268 | 2459 |
| TIME | 0.8428571 | 0.7531915 | 0.7955056 | 470 |
| DURATION | 1 | 0.8333333 | 0.9090909 | 12 |
| SET | 1 | 0.4 | 0.5714286 | 5 |
| Micro-avg.| 0.8621436 | 0.8109301 | 0.835753 | 2946 |
| Macro-avg.| 0.9269391 | 0.7023042 | 0.7991357 | 2946 |
|-------------|----------:|:------:|----------:|----------:|


# 使用說明

## 比賽輸出
### clone
```
git clone https://github.com/Chou-po-chen/openai_ner.git
cd openai_ner
```
### 放置比賽資料
手動複製比賽提供opendid_test資料夾 至 openai_ner資料夾內
手動新建比賽提供.output資料夾 至 openai_ner資料夾內


### run
```
python main.py
```
即可在./.output/answer.txt 取得 answer.txt


## Train
* 開啟train\train.ipynb

* 更改訓練檔案路徑
```
client.files.create(
  file=open(rf"YOUR PATH", "rb"),
  purpose="fine-tune"
)
```
* 執行file upload


* 設定訓練模型 和 FILE ID
```
client.fine_tuning.jobs.create(
  training_file="YOUR FILE ID", 
  model="MODLE ID"
)
```
* 執行train


## 產生訓練資料
* 開啟 lab\gen_train_data.ipynb
* 設定 以下 PAHT 
```
DATA_DIR   = 
ANSWER_DIR = 
ANS_TXT_FILE = 
```
* 執行所有即可

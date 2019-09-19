# EOTRTS
English oral training robot tutor system


nao_server的完成版，分離出個別輔導練習的功能，使用NAO機器人輔助學生的英語口語能力，對應nao-client的Tutor_Audio，伺服器端主要開發語言為Python 2.7.15，機器人為Python 2.7.3，其中功能有帳號登入、單字練習、課文朗讀練習、課文朗讀錄音辨識、會話練習，以下為程式碼大概介紹。

1. server.py
    主要功能為接收訊息並處理，為系統功能主體，接收訊息並透過database module的功能回傳或紀錄相對應的資料，並透過其他module做相應的資料處理

2. word_error_rate
    此module為系統的辨識正確率計算的library，改寫自jiwer這個library，主要為語法修改成Python2(原library為Python3)。

3. database
    有DBMain、DBMail、DBGui三個py檔，DBMain為主要的database，負責找尋學生、單字、閱讀測驗資料，並記錄學生的課文朗讀錄音及會話練習的辨識結果。

4. cloud
    有upload_cloud及cloud_speech兩個py檔，cloud_speech的功能為上傳以及辨識雲端上的錄音檔，upload_cloud使用到cloud_speech, word_error_rate及wav_read的功能，辨識學生錄音檔的結果、計算正確率及語速。

5. wav_read
    讀取wav檔，因機器人回傳的是wav檔，需要取得檔案時間來計算語速，以及wav檔頻率來使upload_cloud方便使用cloud_speech的功能，因雲端辨識需要有該音檔頻率及聲道才能進行辨識。

6. file_processing
    接收機器人傳送過來的聲音檔，並根據其學號儲存至該學號之資料夾，如無該學生之資料夾，則新增一個資料夾，儲存的位置在record裡。

7. mail_transfer
    傳送學生的課文朗讀語音及會話練習辨識結果，透過SMTP傳送，使用的帳號需先設定存取權限才能透過SMTP傳送email，其中有一些html語法。

8. gui
    本系統除了機器人之外也能透過gui來取得結果，錄下課文朗讀的音檔以及會話練習的音檔，用gui選擇即可接收到email。
    
9. library
    本系統所用到的library，這邊只有網路上需要找一下或者要改寫的，像是jiwer。
    
10. venv
    本系統的虛擬Python環境

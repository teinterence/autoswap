```txt
**************************************************
******      Author: TerenceSyu              ******
******      Email:  teinterence@gmail.com   ******
******      Handle: TerenceSyu              ******
******      For internal use only           ******
**************************************************
```

# AUTO SWAP
本專案是將星際公民翻譯完成的ini文件，自動將其部分內容更改回英文版，因為有些公民在日常操作已經習慣英文版介面，只想翻譯部分任務劇情等內容  

## 功能說明
``swap.py`` => 替換 飛船名稱、個人物品名稱、飛船HUD介面 回英文版  
``swap_flightHUD.py`` => 僅替換 飛船HUD介面 回英文版  

## 使用方法
1. 將翻譯過後的檔案命名為 ``global.ini`` 英文原檔為 ``global_en.ini`` 並置於 ``swap.py``相同目錄下  
2. 在該目錄下使用終端機運行 ``python swap.py`` 即可  

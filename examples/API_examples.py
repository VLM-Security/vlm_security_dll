import os
import sys

from vlm_security_dll.vlm_activator import VLM_security

if __name__ == '__main__':
    # 使用測試編號
    vlm_obj = VLM_security.auth_trial()

    # 使用自己的產品編號
    vlm_obj = VLM_security(r"C:\Windows\VAuth.dll", "your product code")

    # 初始化
    # 大於等於0表示成功。（連接了某台伺服器並返回伺服器編號），小於0表示連接失敗。失敗時應提示使用者無法連接驗證服務器並退出程序
    result = vlm_obj.init()

    # 獲取校驗碼，調用Auth並返回成功後調用此函數可獲取返回的校驗碼。
    return_value = vlm_obj.get_code()

    # 取插件的版本號，如果你使用的是普通dll版，此功能函數請參考: 純Dll接口說明-取插件版本。
    # 返回插件版本號
    return_value = vlm_obj.get_ver()

    # 驗證碼模式，驗證註冊碼是否有效。
    # 試用卡：是産品編號，則當作測試 用卡處理。0 成功 -1 失敗 -2 註冊碼被禁用 -3 綁定機器超出數量 -4 註冊碼已在線 -5 已過期
    return_value = vlm_obj.auth('your register code')

    # 使用者模式，驗證使用者是否有效
    # 0 成功 -1 失敗 -2 註冊碼被禁用 -3 綁定機器超限 -4 註冊碼已在線 -5 已過期 -6 使用者餘額不足 -7 使用者無效
    return_value = vlm_obj.user_auth("user", "password")

    # 加密 string encrypt(BYTE type, string src, string key)
    # type byte 加密算法 0 表示AES算法，1表示MD5算法，src string GUID字串，需要加密的字串，key string 加密鍵值 type 為1(MD5)加密時此參數無意義
    # 加密結果，GUID格式的字串
    return_value = vlm_obj.Encrypt(0,'str', '456')

    # 解密 string decrypt(BYTE type, string src, string key)
    # type byte 加密算法 0 表示AES算法，1表示MD5算法，src string GUID字串，需要加密的字串，key string 加密鍵值 type 為1(MD5)加密時此參數無意義
    # 解密結果，GUID格式的字串
    return_value = vlm_obj.decrypt(0,'str', '456')

    # 取卡或使用者的使用到期時間。測試卡無到期時間
    return_value = vlm_obj.get_validity()

    # 使用者註冊，user_register(string user, string pwd,int type, int bind, int multi,int point)
    # int 0 成功 ；-1 失敗 ；-8 使用者名重複
    vlm_obj.user_register("user", 'pwd', type=1, bind=1, multi=1, point=1000)

    # 使用者密碼修改change_password(string Old,string New)
    # 0 表示成功 非0失敗
    return_value = vlm_obj.change_password("test456", "test789")

    # 檢查是否到了無效狀態，這函數是為無法回響COM事件的語言比如易語言裡使用的，每隔幾秒調用一次，在可以回響COM事件的語言裡無需此函數，回響OnInvalid事件即可。
    # Bool true:有效 false:無效
    return_value = vlm_obj.is_valid()

    # 對此機器進行解綁操作，在驗證成功後方可調用。
    # 0:成功 非0失敗
    return_value = vlm_obj.unbind()

    # 扣除時間，Vbox.deduct_point(int point）
    # 返回剩餘計數
    return_value = vlm_obj.deduct_point(int=10)

    # 扣取點數，Vbox.deduct_hour(int hour)
    # 返回剩餘計數，不能傳小數（比如：0.5）
    return_value = vlm_obj.deduct_hour(int=5)


    # 調用此函數VLM將停止工作，用於關閉Process前調用（必須調用否則有機率卡死）
    vlm_obj.release()

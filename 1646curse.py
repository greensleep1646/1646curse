import pywhatkit as kit

try:
    kit.sendwhatmsg("+90**********", "BU BİR OTOMATİK MESAJDIR", 19,40)
except Exception as e:
    print("Hata oluştu:", str(e))

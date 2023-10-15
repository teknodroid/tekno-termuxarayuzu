newName = input("[+] Yeni Adı Girin : ")
newName = '"'+newName+'"'
file  = open('/data/data/com.termux/files/home/.zshrc','r')
allLines = []
i = 0;pos= 0
for line in file.readlines():
    if "TNAME=" in line:
        pos = i
    allLines.append(line)
    i+=1
allLines[pos]="TNAME="+newName+"\n"
file.close()
file = open('/data/data/com.termux/files/home/.zshrc','w')
file.writelines(allLines)
file.close()
print("Başarıyla güncellendi, değişiklikleri görmek için yeniden başlatın")

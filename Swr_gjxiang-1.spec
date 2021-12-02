# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['Swr_gjxiang.py','UI.py','Class_shenwr.py'],
             pathex=['D:\\Swr_Pyhton\\SWR_gongjuxiang',
             'C:\\Windows\\System32\\downlevel',
             'C:\\Users\\shenwr\\AppData\\Local\\Programs\\Python\\Python38\\Lib\\site-packages\\PyQt5',
             'C:\\Users\\shenwr\\AppData\\Local\\Programs\\Python\\Python38\\Lib\\site-packages\\PyQt5\\Qt5\\bin',
             'C:\\Users\\shenwr\\AppData\\Local\\Programs\\Python\\Python38\\Lib\\site-packages\\PyQt5\\Qt5\\plugins',
             'C:\\Users\\shenwr\\AppData\\Local\\Programs\\Python\\Python38\\Lib\\site-packages\\PyQt5\\Qt5\\plugins\\platforms'],
             binaries=[],
             datas=[],
             hiddenimports=['os','sys','math','ffmpeg','PyQt5.QtWidgets','UI','Class_shenwr','PyQt5'],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='Swr_gjxiang',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None,
          icon ='D:\\Swr_Pyhton\\SWR_gongjuxiang\\swr.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Swr_gjxiang')

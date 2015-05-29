# -*- mode: python -*-
a = Analysis(['F:\\info', 'git\\pythondev\\test\\goagent_enhanced\\goagent_iplist_enhanced\\goagent_enhanced_win.py'],
             pathex=['E:\\Program Files\\python\\Lib\\PyInstaller-2.1'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='info.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True )

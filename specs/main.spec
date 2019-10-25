# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['main.py','E:\\pycharm-project\\头脑风暴\\common\\insert.py','E:\\pycharm-project\\头脑风暴\\common\\check_sql_1.py',
'E:\\pycharm-project\\头脑风暴\\common\\combine.py','E:\\pycharm-project\\头脑风暴\\common\\check_sql_2.py'],
             pathex=['E:\\pycharm-project\\头脑风暴'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
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
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='main')

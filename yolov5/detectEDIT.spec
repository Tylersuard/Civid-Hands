# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['detectEDIT.py'],
             pathex=['C:\\Users\\tyler\\Desktop\\Covid-HANDS\\yolov5'],
             binaries=[],
             datas=[('yolov5s.pt', 'yolov5s'), ('413825__henlord__chicken-growl-guttural.wav', '413825__henlord__chicken-growl-guttural.wav'), ('168016__ultradust__chipmunk-voice-say-cheese.wav', '168016__ultradust__chipmunk-voice-say-cheese.wav')],
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
          name='detectEDIT',
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
               name='detectEDIT')

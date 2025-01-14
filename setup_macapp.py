"""
This is a setup.py script generated by py2applet

Usage:
    python setup_macapp.py py2app
"""

from setuptools import setup

APP = ['discodos/cmd/open_shell_mac.py']
DATA_FILES = ['assets/discodos_cmds_v0.3_white.png']
OPTIONS = {
    'iconfile': 'assets/discodos_7-v6_big_fat_D.icns',
    #'argv_emulation': 'true',
    #'emulate_shell_environment': 'true',
    'verbose': 'true',
    'plist': {
        'CFBundleVersion': '1.0.1',
        'CFBundleShortVersionString': '1.0.1',
        'CFBundleName': 'DiscoDOS',
        'CFBundleDisplayName': 'DiscoDOS',
        'CFBundleGetInfoString': 'DiscoDOS is the geekiest DJ tool on the planet',
        'CFBundleIdentifier': 'net.jojotodos.discodos',
        'NSAppleScriptEnable': 'true',
        'NSAppleScriptEnabled': 'true',
        'NSHumanReadableCopyright': 'J0J0 Todos (jt@peek-a-boo.at) - GPL v3'
    },
    'includes': 'applescript'
}
REQUIRES = ['py2app']

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=REQUIRES,
)

# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 18:49:48 2017

@author: admin
"""

# импорт необходимых модулей
import sys
from cx_Freeze import setup, Executable

# так как мы являемся петушками-молодцами, использующими последнюю версию python, то ошибка "KeyError: 'TCL_Library'" неминуема. Этот кусок кода позволит нам искусственно дать интерпретатору то, чего он хочет, предварительно создав в Program Files папку с названием "Python35" и скопировав в неё папку "tcl" из директории, в которой установлен python
import os 
os.environ['TCL_LIBRARY'] = "C:\Program Files\Python36\\tcl\\tcl8.6" 
os.environ['TK_LIBRARY'] = "C:\Program Files\Python36\\tcl\\tk8.6"

# объявите словарь с ключами packages и excludes, ключами которых являются ВСЕ ИСПОЛЬЗУЕМЫЕ В ВАШЕЙ ИГРЕ МОДУЛИ и ВСЕ НЕОБХОДИМЫЕ РЕСУРСЫ (шрифты, текстовые файлы, картинки, музыка) соответственно
build_exe_options = {"packages": ["pygame", "sys", "math","os"],
                     "excludes": ['asyncio', 'backports', 'cffi', 'chardet', 'cloudpickle', 'matplotlib', 
                                  'PyQt5', 'wx',  'urllib', 'ipython_genutils', 'IPython', 'http', 'notebook','numpy',
                                  'OpenSS','packaging','PIL','prompt_toolkit','pycparser','pydoc_data','idna',
                                  'ipykernel','IPython','ipython_genutils','jinja2','json','jsonschema',
                                  'jupyter_client','jupyter_core','lib2to3','logging','markupsafe','mpl_toolkits',
                                  'multiprocessing','nbconvert','nbformat','nose','xml','OpenGL','email',
                                  'distutils','tkinter'
                                  ]}

# вызовите функцию setup и передайте ей следующие аргументы:
setup( name = "STR", 
version = "0.2", 
description = "STR", 
options = {"build_exe": build_exe_options}, 
executables = [Executable("STR.py",base = "Win32GUI")])

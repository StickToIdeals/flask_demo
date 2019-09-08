# -*- coding: utf-8 -*-
import os
import subprocess
import platform
import sys


class aapt():

    def __init__(self):
        if platform.system() == 'Windows':
            aapt_path = os.path.join(os.getcwd(), 'Tools', 'aapt.exe')
            try:
                subprocess.Popen([aapt_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                self.aapt_path = aapt_path
            except OSError:
                pass
        else:
            aapt_path = os.path.join(os.getcwd(), 'Tools', 'aapt')
            try:
                subprocess.Popen([aapt_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                self.aapt_path = aapt_path
            except OSError:
                print('暂未支持非Windows系统使用')

    def run(self, raw_command):
        command = '{} {}'.format(self.aapt_path, raw_command)
        print('执行：%s ' % command)
        (output, err) = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True).communicate()
        if output != b'':
            return output.decode('utf-8')
        raise Exception(err.decode('utf-8'))


class aapt_tools():

    def __init__(self):
        if sys.version_info.major != 3:
            print('请使用Python3')
            exit(1)
        try:
            from app.libs.read_apk.common.aapt import aapt
        except Exception as ex:
            print(ex)
            print('请将脚本放在项目根目录中运行')
            print('请检查项目根目录中的 common 文件夹是否存在')
            exit(1)
        self._aapt = aapt()

    def badging(self, apkPath=None):
        command = ' d badging ' + str(apkPath)
        return self._aapt.run(command)
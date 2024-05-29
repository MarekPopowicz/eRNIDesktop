import os
import base64
import tkinter as tk
from tkinter import filedialog
from utils import info_boxes
import shutil
from PyQt5.QtWidgets import QFileDialog


def copy_file(src, dst):
    if shutil.copy(src, dst):
        return True


def create_folder(path):
    isDir = os.path.isdir(path)
    if not isDir:
        try:
            os.mkdir(path)
            return True
        except:
            return False
    else:
        return isDir


def open_folder(path, create=False):
    if not create:
        try:
            path = os.path.realpath(path)
            os.startfile(path)
            return True
        except:
            return False
    else:
        if create_folder(path):
            try:
                path = os.path.realpath(path)
                os.startfile(path)
                return True
            except:
                return False
        else:
            return False


def get_file(path):
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(initialdir=path)
    return file_path


def base64_encode(data):
    data_bytes = data.encode('utf-8')
    base64_bytes = base64.b64encode(data_bytes)
    data_encoded = base64_bytes.decode('utf-8')
    return data_encoded


def base64_decode(data):
    base64_bytes = data.encode('utf-8')
    data_bytes = base64.b64decode(base64_bytes)
    data_decoded = data_bytes.decode('utf-8')
    return data_decoded


def read_encoded(file):
    try:
        data = []
        if os.path.isfile(file):
            with open(file, encoding='utf8') as f:
                while True:
                    line = f.readline()
                    if not line:
                        break
                    data.append(base64_decode(line))
            return data
        else:
            info_boxes.informationBox('Informacja', f' Nie udało się odczytać pliku: {file}')
            return None
    except Exception as err:
        info_boxes.criticalBox("Błąd", f"Unexpected {err=}, {type(err)=}")
        raise


def read_file(file):
    if os.path.isfile(file):
        with open(file, encoding='utf8') as f:
            contents = f.read()
            return contents
    else:
        return None


def read_line(file):
    try:
        data = []
        if os.path.isfile(file):
            with open(file, encoding='utf8') as f:
                while True:
                    line = f.readline().strip()
                    if not line:
                        break
                    data.append(line)
            return data
        else:
            info_boxes.informationBox('Informacja', f' Nie udało się odczytać pliku: {file}')
            return None
    except Exception as err:
        info_boxes.criticalBox("Błąd", f"Unexpected {err=}, {type(err)=}")
        raise


def write_file(file, content):
    try:
        f = open(file, "w", encoding='utf8')
        f.write(content)
        f.close()
        return True
    except:
        return False


# single choice
def openFileNameDialog(self):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                              "All Files (*);;Python Files (*.py)", options=options)
    if fileName:
        return fileName


# multiple choice
def openFileNamesDialog(self):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    files, _ = QFileDialog.getOpenFileNames(self, "QFileDialog.getOpenFileNames()", "",
                                            "All Files (*);;Python Files (*.py)", options=options)
    if files:
        return files


def saveFileDialog(self, path):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    fileName, _ = QFileDialog.getSaveFileName(self, "Zapisz jako", path,
                                              "All Files (*);;htm Files (*.htm)", options=options)
    if fileName:
        return fileName
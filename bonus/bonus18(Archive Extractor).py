import zipfile

import FreeSimpleGUI as sg

from bonus.zip_extractor import extract_archive

from zip_extractor import extract_archive

sg.theme('DarkAmber')

label1 = sg.Text("Select archvie")
input1 = sg.Input()
choose_button1 = sg.FileBrowse("Choose", key= "archive")

label2 = sg.Text("Select dest dir: ")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key= "folder")

extract_button = sg.Button("Extract", key= "Extract")
exit_button = sg.Button("Exit", key= "Exit")
output_box = sg.Text(key="output", text_color= "Green",)

window = sg.Window("Archive Extractor", layout=[[label1, input1, choose_button1],
                                              [label2, input2, choose_button2],
                                              [extract_button, output_box, exit_button]]
                                              )
while True:
    event, values = window.read()
    match event:
        case "Extract":
            archivepath = values["archive"]
            dest_dir = values["folder"]
            extract_archive(archivepath, dest_dir)
            window["output"].update(value="Archive extracted successfully!")
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break
window.read()
window.close()
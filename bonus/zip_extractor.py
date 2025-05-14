import zipfile


def extract_archive(archive_path, dest_dir):
    with zipfile.ZipFile(archive_path, 'r') as archive:
        archive.extractall(dest_dir)


if __name__ == "__main__":
    extract_archive(r"C:\Users\Dawi\Desktop\Udmey Python\PythonProject(app1)\bonus\compressed.zip",
                    r"C:\Users\Dawi\Desktop\Udmey Python\PythonProject(app1)\bonus\files")

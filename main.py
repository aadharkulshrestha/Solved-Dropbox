import os
import dropbox
from dropbox.files import WriteMode
#
class TransferData:
    def __init__(self,access_token):
        self.access_token =  access_token
#
    def upload_file(self, file_from, file_to):
        print("up")
        dbx = dropbox.Dropbox(self.access_token)


        for root, dirs, files in os.walk(file_from):
            print("files ", files)
            for filename in files:
                print("Filename", filename)
                local_path = os.path.join(root, filename)
                print("Local path ", local_path)


                relative_path = os.path.relpath(local_path, file_from)
                print("Relative path ", relative_path)
                dropbox_path = os.path.join(file_to, relative_path)
                print("Dropbox path ", dropbox_path)


                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = 'xJl78eLpn_0AAAAAAAAAAdKnCBaHxL_OvyWuJJgab7pge6kCos-EcaY-dml6016K'
    transferData = TransferData(access_token)

    file_from = str(input("Enter the folder path to transfer : -"))
    file_to = input("enter the full path to upload to dropbox:- ")

    # API v2
    transferData.upload_file(file_from,file_to)
    print("file has been moved !!!")

main()

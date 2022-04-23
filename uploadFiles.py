import dropbox
import os

class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token

    def upload_files(self,file_from,file_to,local_path):
        dbx=dropbox.Dropbox(self.access_token)

        for root,dirs,files in os.walk(file_from):
            relative_path=os.path.relpath(local_path,file_from)
            dropbox_path=os.path.join(file_to,relative_path)

            d= open(file_from,"rb")
            dbx.files_upload(d.read(), file_to)


def main():
    access_token="sl.BGSNlcIILu880byg92W2rVG2KP-T-sMJECph125uwhJmhro7aXhiXEtjJ1Dls6SHQK_IYgfqpVaknV0Mgt_2n4mixLcUId33c-sqaQu6M7MjE6yF42cR-gBSlVkOTqVdWp1Fz_g"

    transfer_data=TransferData(access_token)

    file_from=input("enter your file location which you want save on dropbox:")
    file_to=input(" enter destination path :")

    transfer_data.upload_files(file_from,file_to)
    print("your file has been moved to the dropbox")


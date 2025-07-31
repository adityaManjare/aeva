import os , shutil
from fastapi import UploadFile,HTTPException,status
from typing import List


doc_directory = "test_data"
os.makedirs(doc_directory, exist_ok=True)


def upload_doc(i:List[UploadFile]):
    for file in i:
            if not file.filename.endswith(".pdf"):
                raise HTTPException(status_code=status.WS_1003_UNSUPPORTED_DATA,detail="Please upload pdf file only")
            # filepath = f"{doc_directory}\{file.filename}" # this will work only for windows but linux machine uses different slash "/"
            filepath = os.path.join(doc_directory, file.filename)

            with open( filepath,"wb") as newfile:
                shutil.copyfileobj(file.file, newfile)  #Because file is an UploadFile object, not a file stream.
                newfile.close()
    return {"message": f"Uploaded {file.filename} successfully."}

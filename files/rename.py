import os 

os.chdir(r"C:\Users\ivardoshvili\Videos\py-general\files")

for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    f_title = file_name[:4]
    f_num = file_name[4:]
    new_name = f"{f_num.strip()}{f_title.strip()}{file_ext.strip()}"

    os.rename(f, new_name)

    
    
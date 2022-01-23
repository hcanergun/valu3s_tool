import os

if __name__ == "__main__":

    # get the latest file name from ./ui/..
    files = os.listdir("./ui")
    filename = files[-1]

    try:
        print(f"'{filename}' is going to be converted !!")

        # designer.exe output file (filename.ui) is converting to python file (filename.ui).
        os.system(
            f"C:/Users/zeker/OneDrive/Masaüstü/RV_Tool/tool/venv/Scripts/pyuic5.exe -x C:/Users/zeker/OneDrive/Masaüstü/RV_Tool/tool/ui/{filename} -o tool_gui.py")

        print(f"'{filename}' is SUCCESSFULY converted !!")
    except:
        print(f"There is an error occured while '{filename}' is converting !!")

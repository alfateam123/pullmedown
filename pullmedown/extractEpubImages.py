from __future__ import print_function
import os
import shutil
try:
  import epub
except ImportError:
  print("Ehm, you need \"epub\" module. grab it at https://pypi.python.org/pypi/epub/0.5.2")

def main():
  for act_path, dirs, files in os.walk("epubs"):
    for file_ in files:
      with epub.open_epub("epubs/"+file_) as book:
        try:
          os.mkdir(file_+"_folder")
        except OSError:
          print(file_+"_folder", "already exists, overwriting...")
          shutil.rmtree(file_+"_folder")
        print("epubs/"+file_)
        images = (name for name in book.namelist() if name.endswith("jpg") or name.endswith("png"))
        for imagename in images:
          imagename = imagename.replace("OEBPS/", "", 1)#epub, pls
          book.extract_item(imagename, to_path=file_+"_folder")
          if "cover" in imagename:
            print(imagename)
            os.rename(file_+"_folder/OEBPS/"+imagename, file_+"_folder/OEBPS/"+imagename.replace("cover", "001_cover"))
        os.rename(file_+"_folder/OEBPS/images", file_+"_folder/images")
        os.rmdir(file_+"_folder/OEBPS")
        os.system("python generate_cbz.py \""+file_+"_folder/images/\"")
        os.rename(file_+"_folder/images/.cbz", file_+"_folder/images/"+file_+".cbz")

if __name__ == '__main__':
    main()

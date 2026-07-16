import os
import shutil

try:
    path = os.path.expanduser('~/.gemini/antigravity-ide/brain/206a606d-4cc9-49c8-8f6a-882532568f17')
    print("Files in brain:", os.listdir(path))
    for f in os.listdir(path):
        if 'default_panorama' in f:
            src = os.path.join(path, f)
            dst = './panorama.png'
            shutil.copy(src, dst)
            print("Successfully copied to:", dst)
            break
except Exception as e:
    print("Error:", e)

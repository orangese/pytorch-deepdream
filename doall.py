import subprocess
import os
cmd = """python3 deepdream.py --model_name FACENET --layers final_block8 --pyramid_size 5 --pyramid_ratio 1.2 --num_gradient_ascent_iterations 10 --input {}"""

p = "/Users/ryan/Documents/stanford/classes/arthist186b/home_media/"
for path in os.listdir(p):
    if "beach" not in path:
        d = os.path.join(p, path)
        r = subprocess.Popen(cmd.format(d).split())
        r.wait()

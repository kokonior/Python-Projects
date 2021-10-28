import time, sys
def loading():
    print("Loading...")
    for i in range(0, 100):
        time.sleep(0.1)
        width = (i + 1) // 4
        bar = "[" + "#" * width + " " * (25 - width) + "]"
        sys.stdout.write(u"\u001b[1000D" +  bar)
        sys.stdout.flush()
    print()
    
loading()
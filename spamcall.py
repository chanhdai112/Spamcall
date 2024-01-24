import re

def change_text_color(text, color_code):
    return f"\033[1;{color_code}m{text}\033[0m"

# Chuỗi ban đầu
original_string = """
   ██╗  ██╗███████╗ █████╗ ████████╗    ████████╗ ██████╗  ██████╗ ██╗
   ██║  ██║██╔════╝██╔══██╗╚══██╔══╝    ╚══██╔══╝██╔═══██╗██╔═══██╗██║       
   ███████║█████╗  ███████║   ██║          ██║   ██║   ██║██║   ██║██║
   ██╔══██║██╔══╝  ██╔══██║   ██║          ██║   ██║   ██║██║   ██║██║
   ██║  ██║███████╗██║  ██║   ██║          ██║   ╚██████╔╝╚██████╔╝███████╗
"""

# Thay thế chữ "heat tool" thành "ANH PHI TOOL" với màu xanh dương
changed_string = re.sub(r"heat tool", change_text_color("Buichanhdai", "34"), original_string)

print(changed_string)

import re
import sys

def update_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # We want to target specific links in the resume body.
    # The links have titles like: PyHazards, FORTIS Lab, OEM Controls, Sentiment Analysis
    # Let's use specific replacements to avoid hitting social links or nav links.
    
    replacements = [
        ("PyHazards: AI-Powered Hazard Prediction\n              Framework</a>", "PyHazards: AI-Powered Hazard Prediction\n              Framework 🔗</a>"),
        ("Research Assistant, FORTIS Lab at USC (PI: Prof. Yue Zhao)</a>", "Research Assistant, FORTIS Lab at USC (PI: Prof. Yue Zhao) 🔗</a>"),
        ("OEM Controls Automated Angle Test for\n              AS5</a>", "OEM Controls Automated Angle Test for\n              AS5 🔗</a>"),
        ("Large-Scale Sentiment Analysis on Amazon\n              Office Reviews</a>", "Large-Scale Sentiment Analysis on Amazon\n              Office Reviews 🔗</a>"),
        # Chinese versions:
        ("PyHazards：AI驱动的自然灾害预测框架</a>", "PyHazards：AI驱动的自然灾害预测框架 🔗</a>"),
        ("研究助理，南加州大学 FORTIS 实验室 (PI: Prof. Yue Zhao)</a>", "研究助理，南加州大学 FORTIS 实验室 (PI: Prof. Yue Zhao) 🔗</a>"),
        ("OEM Controls\n                            AS5传感器自动化角度测试</a>", "OEM Controls\n                            AS5传感器自动化角度测试 🔗</a>"),
        ("亚马逊办公产品评论大规模情感分析</a>", "亚马逊办公产品评论大规模情感分析 🔗</a>")
    ]
    
    for old, new in replacements:
        content = content.replace(old, new)
        
    with open(filepath, 'w') as f:
        f.write(content)

update_file('index.html')
update_file('index-zh.html')
print("Done")

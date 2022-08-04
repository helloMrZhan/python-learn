# 爬虫验证码识别
#
# 使用百度 paddle ocr 库可以识别验证码
#
# 安装paddle：pip install paddlepaddle==2.1.0
# 安装paddle ocr: pip install paddleocr==2.0.6
# 编写代码
# -*- coding: UTF-8 -*-
import re
from paddleocr import PaddleOCR

if __name__ == "__main__":
    ocr_client = PaddleOCR(
        use_angle_cls=True,
        lang="ch",
        use_space_char=True,
        use_zero_copy_run=True,
        use_mp=True,
        total_process_num=16,
        ir_optim=True,
        enable_mkldnn=True,
        rec_batch_num=1,
        max_batch_size=1
    )
    result = ocr_client.ocr('code.png', det=True, rec=True, cls=True)
    code_text = []
    for line in result:
        print(line)
        # 提取文本
        text = line[1][0]
        code_text.append(text)
    print(code_text)

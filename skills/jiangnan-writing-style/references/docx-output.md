# .docx 输出交付指南

## 适用场景

写完章节/片段后，以 Word 文档交付用户——适合中文小说排版。

## 前置步骤

```python
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
```

先安装依赖：
```bash
pip install python-docx
```

## 页面设置（A4）

```python
doc = Document()
section = doc.sections[0]
section.page_width = Cm(21.0)
section.page_height = Cm(29.7)
section.top_margin = Cm(2.54)
section.bottom_margin = Cm(2.54)
section.left_margin = Cm(3.17)
section.right_margin = Cm(3.17)
```

> A4 标准尺寸 21×29.7cm，上下边距 2.54cm，左右边距 3.17cm（Word 默认值）。
```python
style = doc.styles['Normal']
style.font.name = '宋体'
style.font.size = Pt(12)  # 小四
for attr in ['w:eastAsia', 'w:ascii', 'w:hAnsi']:
    style.element.rPr.rFonts.set(qn(attr), '宋体')
```

## 标题：宋体小二(18pt)，居中，段前段后空一行，固定18磅行距

```python
title_p = doc.add_paragraph()
title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
title_p.paragraph_format.space_before = Pt(18)
title_p.paragraph_format.space_after = Pt(18)

pPr = title_p._element.get_or_add_pPr()
sp = pPr.find(qn('w:spacing'))
if sp is None:
    sp = OxmlElement('w:spacing')
    pPr.append(sp)
sp.set(qn('w:line'), '360')       # 18pt * 20
sp.set(qn('w:lineRule'), 'exact')

run = title_p.add_run('第一章  灵压')
run.font.size = Pt(18)             # 小二
run.font.bold = False              # 小二通常不加粗
run.font.name = '宋体'
for attr in ['w:eastAsia', 'w:ascii', 'w:hAnsi']:
    run.element.rPr.rFonts.set(qn(attr), '宋体')
```

## 段落辅助函数：宋体小四、两端对齐、首行缩进2字符、固定18磅行距

```python
def add_para(text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY   # 两端对齐

    pPr = p._element.get_or_add_pPr()

    # 首行缩进2字符 (480 twips at 12pt)
    ind = pPr.find(qn('w:ind'))
    if ind is None:
        ind = OxmlElement('w:ind')
        pPr.append(ind)
    ind.set(qn('w:firstLine'), '480')

    # 固定值18磅行距
    sp = pPr.find(qn('w:spacing'))
    if sp is None:
        sp = OxmlElement('w:spacing')
        pPr.append(sp)
    sp.set(qn('w:line'), '360')
    sp.set(qn('w:lineRule'), 'exact')

    run = p.add_run(text)
    run.font.size = Pt(12)         # 小四
    run.font.name = '宋体'
    for attr in ['w:eastAsia', 'w:ascii', 'w:hAnsi']:
        run.element.rPr.rFonts.set(qn(attr), '宋体')
    return p
```

## 简体中文规范

- 全文使用简体中文，不出现日文汉字或繁体字
- 专有名词中的日文汉字需转简体：霊→灵、圧→压、鷹→鹰、歳→岁、熒→荧
- 日文假名注音删除，仅保留简体中文部分
- 对话使用中文双引号 ""，不得使用日文引号 「」
- 角色名使用全称（浅羽司，不是司），怪物名使用中文译名（无足女，不是 Teke Teke）
- 字体必须为宋体，不可使用游明朝等日文字体

## 编码细节

- python-docx 内部为 Unicode，中文字符直接传入字符串
- 保存路径用 raw string 处理 Windows 路径：
  ```python
  doc.save(r"C:\Users\Admin\Desktop\jn\第一章_灵压.docx")
  ```

## 字数统计与目标校验

```python
import re
full_text = "\n".join(texts)
cjk = len(re.findall(r'[\u4e00-\u9fff]', full_text))
print(f"汉字字数: {cjk}")
```

- 确认 cjk 在目标值的 ±10% 范围内
- 字数偏低：增加具体的画面细节和感官描写（光线、触感、气味、温度），不要填塞虚词
- 字数偏高：优先砍掉多余的场景铺垫和重复说明，保留最有力的画面和对话

## 自动质检

```bash
python scripts/validate_ai_patterns.py <章节纯文本文件>
```

脚本会自动扫描字数、破折号、虚词、AI句式、极短叙事段等指标。

## 完整调用流程

```
读设定文档 → 加载 jiangnan-writing-style（skill_view）→
按叙事协议技法引擎写作 → 组装 texts 数组 →
创建 Document → 设置页面/字体（宋体小四）→
设置标题（宋体小二居中）→ 循环 add_para →
保存 .docx → 运行 validate_ai_patterns.py 质检 → 交付
```

## 注意事项

- 生成后务必用 Python 统计汉字字数确认符合目标
- 分隔场景的「〇」不宜过多，一章 2~3 个分割为佳
- 交付前做 AI痕迹自检
- 正文段落中不要出现章节标题（如"第一章 灵压"）

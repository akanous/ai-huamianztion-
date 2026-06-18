# .docx 输出交付指南

## 适用场景

写完章节/片段后，以 Word 文档交付用户——适合中文小说排版。

## 前置步骤

```python
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
```

先安装依赖：
```bash
pip install python-docx
```

## 页面设置（A5文库本尺寸）

```python
doc = Document()
section = doc.sections[0]
section.page_width = Cm(14.8)
section.page_height = Cm(21.0)
section.top_margin = Cm(2.5)
section.bottom_margin = Cm(2.5)
section.left_margin = Cm(2.8)
section.right_margin = Cm(2.8)
```

## 全局字体设置（宋体）

```python
from docx.shared import Pt, Cm
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

style = doc.styles['Normal']
style.font.name = '宋体'
style.font.size = Pt(12)  # 小四
for attr in ['w:eastAsia', 'w:ascii', 'w:hAnsi']:
    style.element.rPr.rFonts.set(qn(attr), '宋体')


## 段落辅助函数

```python
def add_para(text, indent=True):
    p = doc.add_paragraph()
    p.paragraph_format.first_line_indent = Cm(0.75) if indent else Cm(0)
    p.paragraph_format.line_spacing = 1.2
    p.paragraph_format.space_after = Pt(4)
    run = p.add_run(text)
    run.font.size = Pt(10.5)
    run.font.name = '宋体'
    run.element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')
    run.element.rPr.rFonts.set(qn('w:ascii'), '宋体')
    run.element.rPr.rFonts.set(qn('w:hAnsi'), '宋体')
    return p
```

## 章节标题

```python
title = doc.add_paragraph()
title.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = title.add_run('第一章  灵压')
run.font.size = Pt(18)
run.font.bold = True
run.font.name = '宋体'
run.element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')
title.paragraph_format.space_after = Pt(20)
```

## 简体中文规范

- 全文使用简体中文，不出现日文汉字或繁体字
- 专有名词中的日文汉字需转简体：霊→灵、圧→压、鷹→鹰、歳→岁、熒→荧
- 日文假名注音删除，仅保留简体中文部分
- 对话使用中文双引号 `""`，不得使用日文引号 `「」`
- 字体必须为宋体，不可使用游明朝等日文字体

## 编码细节

- python-docx 内部为 Unicode，中文字符直接传入字符串
- 保存路径用 raw string 处理 Windows 路径：
  ```python
  doc.save(r"C:\Users\Admin\Desktop\jn\第一章_灵压.docx")
  ```

## 完整调用流程

```
读设定文档 → 加载 jiangnan-writing-style（skill_view）→
按叙事协议技法引擎写作 → 组装 texts 数组 →
创建 Document → 设置页面/字体（宋体）→ 循环 add_para →
保存 .docx → 告知用户路径
```

## 注意事项

- 生成后务必用 Python 统计汉字字数确认符合目标
- 分隔场景的「〇」不宜过多，一章 2~3 个分割为佳
- 交付前做 AI痕迹自检

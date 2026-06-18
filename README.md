# 江南写作风 · 小说创作技能包

> 写给想写出江南那种"少年感"文字的人。
> 也写给不想让自己的文字一眼被认出是AI的人。

一个融合了**江南（杨治）叙事技法**与**去AI写作痕迹（humanizer）** 的中文小说创作技能包。

> ⚠️ 本技能封装为 **SKILL.md 格式**，设计用于支持 SKILL.md 协议的 AI 编程助手（如 Hermes Agent、Claude Code、Cursor 等）。如果你使用的工具不支持加载 SKILL.md，可以直接阅读 `SKILL.md` 文件，将其中的流程和规范作为手动参考。

## 安装方法

### 方式一：Hermes Agent

```bash
# 1. 复制 SKILL.md 到 Hermes 技能目录
cp skills/jiangnan-writing-style/SKILL.md ~/.hermes/skills/creative/jiangnan-writing-style/

# 2. 复制参考文件（可选）
cp -r skills/jiangnan-writing-style/references ~/.hermes/skills/creative/jiangnan-writing-style/

# 3. 加载使用
skill_view(name='jiangnan-writing-style')
```

### 方式二：Claude Code / Cursor 等

将 `skills/jiangnan-writing-style/SKILL.md` 放入项目的 `.claude/skills/` 或对应目录，或在对话中直接引用该文件。

### 方式三：手动阅读

不依赖任何工具——打开 `skills/jiangnan-writing-style/SKILL.md` 直接阅读，按其中的流程和规范进行创作即可。

## 写作流程

```
Step 0: 心理锚定
Step 1: 配方提取（角色/信物/画面）
Step 2: 技法引擎（写稿）
Step 3: 写作规范执行（简体/宋体/去AI）
Step 4: 自我检视（扫描AI痕迹）
Step 5: 输出交付（生成docx）
Step 6: 质检清单
```

## 内容结构

```
skills/jiangnan-writing-style/
├── SKILL.md                          # 主技能文件（核心内容）
├── references/
│   ├── docx-output.md                # Word输出代码模板
│   └── humanizer-after-check.md      # AI痕迹扫描速查表
```

## 核心技法

### 叙事技法

- **反差构图**——同一个画面里放两个极端：热血和日常、战斗和饭团
- **信物系统**——用一个具体物件贯穿叙事
- **不完整闭合**——结局不把每一根线都系紧
- **缺失驱动**——故事由"失去什么"驱动，不是由"获得什么"驱动

### 去AI痕迹

| 模式 | 说明 |
|------|------|
| 破折号过度 | 一章不超过3个叙事破折号 |
| 比喻堆叠 | 同段不超过1个「像」 |
| 对话标签 | 上下文能看出谁在说就不加标签 |
| 虚词填充 | 删除「大约」「像是」「仿佛」「似乎」 |
| 节奏变化 | 插入1-2字极短段打破匀速 |

### 交付规范

- 字体：宋体（SimSun），10.5pt
- 语言：简体中文，无日文汉字/繁体字
- 排版：A5尺寸，行距1.2，首行缩进0.75cm
- 格式：Word (.docx)

## 创作伦理

- **缺失驱动**：结局是"失去"，不是"获得"
- **不跪下去**：拒绝爽文逻辑，保留少年式固执
- **修订伦理学**：不能用今天的成熟否认昨天的孤独
- **温暖底色**：再深的孤独也要留最后一道光
- **意象化回答**：意象 > 逻辑

## 来源

本技能包融合自以下项目：

- [jiangnan.skill](https://github.com/dmlin7777777/jiangnan.skill)（MIT协议）
- [humanizer](https://github.com/blader/humanizer)（MIT协议）

# 江南写作风 · 小说创作技能包

本技能包融合了两个现有技能，并做了针对性修改。

## 融合来源

| 技能 | 来源 | 版本 |
|------|------|------|
| jiangnan-skill | [dmlin7777777/jiangnan.skill](https://github.com/dmlin7777777/jiangnan.skill) | v2.0.3 |
| humanizer | [blader/humanizer](https://github.com/blader/humanizer) | v2.5.1 |

两者均遵循 MIT 协议。

## 修改内容

### 对 jiangnan-skill 的改动

- 补充了 Word 文档输出流程（python-docx 代码模板、A5页面设置、全局字体配置）
- 补充了输出规范（简体中文约束、宋体字体指定、日文汉字转简体规则）
- 增加了交付后 AI 痕迹扫描的引用和速查表
- 删除了原技能中与"龙族结局"强绑定的特定内容

### 对 humanizer 的改动

- 将 29 种 AI 写作模式中的高频项提炼为中文写作自查表
- 补充了中文语境下特有的 AI 痕迹模式（破折号过度、比喻堆叠、「不是……是……」句型等）
- 将英文示例和说明替换为中文写作场景适用的版本

### 新增内容

- 简体中文 + 宋体字体的排版规范（标题小二18pt、正文小四12pt、固定18磅行距）
- Word 文档生成代码模板（python-docx）
- 交付前六步质检清单
- 白描优先、比喻节制的句式规范
- 极短叙事段合并规则（禁止无意义单句独立成段）
- 无英文/日文专名要求（怪物名使用中文译名）
- 角色全称规范（不使用单名）
- 自动质检脚本：`scripts/validate_ai_patterns.py`
- 参考文件：`references/docx-output.md` 和 `references/humanizer-after-check.md`

## 文件结构

```
skills/jiangnan-writing-style/
├── SKILL.md                          # 主技能文件
├── scripts/
│   └── validate_ai_patterns.py       # AI痕迹自动质检脚本
├── references/
│   ├── docx-output.md                # Word输出代码模板
│   └── humanizer-after-check.md      # AI痕迹扫描速查表
```

## 安装

### Hermes Agent

```bash
cp -r skills/jiangnan-writing-style ~/.hermes/skills/creative/
```

### Claude Code / Cursor 等

将 `skills/jiangnan-writing-style/SKILL.md` 放入对应工具的 skills 目录，或直接在对话中引用。

## 许可证

MIT

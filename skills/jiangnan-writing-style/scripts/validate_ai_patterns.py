#!/usr/bin/env python3
"""validate_ai_patterns.py — 章节AI痕迹质检脚本

用法:
    python validate_ai_patterns.py <章节纯文本文件>

输出:
    逐项报告各项AI痕迹指标是否通过限制。
"""

import re
import sys


def validate(text: str) -> dict:
    result = {}
    lines = text.split('\n')

    # 汉字字数
    cjk = len(re.findall(r'[\u4e00-\u9fff]', text))
    result['汉字字数'] = cjk

    # 叙事破折号（排除对话内「——」）
    narrative_dashes = 0
    for m in re.finditer('——', text):
        before = text[max(0, m.start() - 3):m.start()]
        if '"' not in before:
            narrative_dashes += 1
    result['叙事破折号'] = (narrative_dashes, '≤3')

    # 对话破折号
    dialog_dashes = len(re.findall('——', text)) - narrative_dashes
    result['对话破折号'] = dialog_dashes

    # 虚词
    for word in ['大约', '像是', '仿佛', '似乎']:
        count = len(re.findall(word, text))
        result[f'「{word}」'] = (count, '0')

    # 「然后」「接着」
    ranhou = len(re.findall('然后', text))
    result['「然后」「接着」'] = (ranhou, '≤3')

    # AI模式「不是X。是Y」/「不是X，是Y」
    ai_not_shi = 0
    for line in lines:
        if '不是' in line and ('。是' in line or '，是' in line):
            ai_not_shi += 1
    result['AI「不是…是…」句式'] = (ai_not_shi, '≤2')

    # 极短叙事段：1-3汉字且非对话且非标题且非分隔符
    ultra_short = 0
    ultra_short_lines = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        cn = len(re.findall(r'[\u4e00-\u9fff]', stripped))
        is_dialog = '"' in stripped
        is_special = stripped in ('〇')
        if 1 <= cn <= 3 and not is_dialog and not is_special:
            ultra_short += 1
            ultra_short_lines.append(stripped)
    result['极短叙事段'] = (ultra_short, '≤2')
    result['极短叙事段_内容'] = ultra_short_lines

    return result


def main():
    if len(sys.argv) < 2:
        print('用法: python validate_ai_patterns.py <文本文件>')
        sys.exit(1)

    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        text = f.read()

    results = validate(text)
    all_pass = True

    print('=' * 50)
    print('AI 痕迹质检报告')
    print('=' * 50)
    print()

    print(f'汉字字数: {results["汉字字数"]}')
    print()

    for key in ['叙事破折号', '对话破折号', '「大约」', '「像是」', '「仿佛」', '「似乎」',
                 '「然后」「接着」', 'AI「不是…是…」句式', '极短叙事段']:
        val = results[key]
        if isinstance(val, tuple):
            actual, limit_str = val
            limit_val = int(limit_str.lstrip('≤'))
            ok = actual <= limit_val
            mark = '✅' if ok else '❌'
            print(f'{mark} {key}: {actual} (限制{limit_str})')
            if not ok:
                all_pass = False
        else:
            print(f'   {key}: {val}')

    if results['极短叙事段_内容']:
        print()
        print('极短叙事段详情:')
        for item in results['极短叙事段_内容']:
            print(f'  ⚡ "{item}"')
        print('  建议：合并到相邻段落中')

    print()
    if all_pass:
        print('✅ 全部通过')
    else:
        print('❌ 存在未通过项，请按SKILL.md规范修改后重新检查')

    sys.exit(0 if all_pass else 1)


if __name__ == '__main__':
    main()

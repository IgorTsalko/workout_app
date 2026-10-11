#!/usr/bin/env python3
"""Собирает страницу для claude.ai из index.html.

claude.ai сам оборачивает страницу в <!doctype html><head>…<body>, поэтому в файл для публикации
идут только <title>, <style> и содержимое <body>. Логика та же: index.html сам понимает,
открыт ли он на claude.ai (window.claude), и тогда хранит данные там и включает чат с тренером.

    python3 scripts/build_artifact.py out.html
"""
import re
import sys
from pathlib import Path

src = (Path(__file__).resolve().parent.parent / 'index.html').read_text(encoding='utf-8')
title = re.search(r'<title>.*?</title>', src, re.S).group(0)
style = re.search(r'<style>.*?</style>', src, re.S).group(0)
body = re.search(r'<body>(.*)</body>', src, re.S).group(1)
out = Path(sys.argv[1] if len(sys.argv) > 1 else 'artifact.html')
out.write_text(f'{title}\n{style}\n{body.strip()}\n', encoding='utf-8')
print(f'{out}: {out.stat().st_size // 1024} КБ')

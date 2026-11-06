#!/usr/bin/env python3
"""GeoLens 自检：结构完整性 + 两个强制脚本是否可达。

用法：python scripts/check.py
"""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV = dict(os.environ, PYTHONIOENCODING="utf-8")


def run(script, args):
    path = os.path.join(ROOT, "geo-sleuth", "scripts", script)
    if not os.path.isfile(path):
        return False, "缺少 " + path
    try:
        r = subprocess.run(
            [sys.executable, path] + args,
            cwd=ROOT,
            env=ENV,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=120,
        )
        out = (r.stdout or "") + (r.stderr or "")
        return r.returncode == 0, out
    except Exception as e:  # noqa: BLE001
        return False, repr(e)


def main():
    ok = True
    print("== GeoLens 自检 ==")
    print("根目录:", ROOT)

    # 1. 入口与关键文件
    required = [
        "SKILL.md", "INDEX.md", "README.md", "NOTICE.md", "LICENSE",
        os.path.join("region", "SKILL.md"),
        os.path.join("region", "references", "china", "中国通用.md"),
        os.path.join("docs", "_original", "original-wlmz-SKILL.md"),
        os.path.join("geo-sleuth", "scripts", "sweep.py"),
        os.path.join("geo-sleuth", "scripts", "kb_search.py"),
        os.path.join("geo-sleuth", "scripts", "triage.py"),
    ]
    for rel in required:
        hit = os.path.isfile(os.path.join(ROOT, rel))
        print(("  OK   " if hit else "  MISS ") + rel)
        ok &= hit
    with open(os.path.join(ROOT, "SKILL.md"), encoding="utf-8") as f:
        head = f.read(400)
    name_ok = "name: geolens" in head
    print(("  OK   " if name_ok else "  MISS ") + "SKILL.md name = geolens")
    ok &= name_ok

    # 2. 规模统计
    skills = []
    for base, dirs, files in os.walk(ROOT):
        if ".git" in dirs:
            dirs.remove(".git")
        skills += [os.path.join(base, f) for f in files if f == "SKILL.md"]
    md = sum(1 for base, dirs, files in os.walk(ROOT)
             if ".git" not in base
             for f in files if f.endswith(".md"))
    print("  统计: %d 个 SKILL.md / %d 个 .md 文件" % (len(skills), md))
    ok &= len(skills) >= 28

    # 3. 强制脚本
    good, out = run("sweep.py", ["白墙", "平顶", "竹林", "晨雾", "河"])
    sweep_ok = good and "27/27" in out
    print(("  OK   " if sweep_ok else "  FAIL ") + "sweep.py 覆盖率 27/27")
    if not sweep_ok:
        print(out[-800:])
    ok &= sweep_ok

    good, out = run("kb_search.py", ["白墙", "平顶", "徽派", "竹林"])
    kb_ok = good and "命中" in out
    print(("  OK   " if kb_ok else "  FAIL ") + "kb_search.py 分层检索")
    if not kb_ok:
        print(out[-800:])
    ok &= kb_ok

    print("== 结果:", "全部通过 ✅" if ok else "有失败项 ❌", "==")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())

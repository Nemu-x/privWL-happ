#!/usr/bin/env python3
import re
import sys
from pathlib import Path

import yaml  # pyyaml


def normalize_domain(d: str) -> str:
    d = d.strip()
    d = d.lstrip(".")
    return d.lower()


def main(inp: str, out_dir: str, list_name: str):
    p = Path(inp)
    data = yaml.safe_load(p.read_text(encoding="utf-8"))

    payload = data.get("payload", [])
    if not isinstance(payload, list):
        raise SystemExit("YAML: ожидаю ключ payload: [ ... ]")

    rules = []
    for item in payload:
        if not isinstance(item, str):
            continue
        s = item.strip()

        # Примеры Clash rule-provider:
        # DOMAIN-SUFFIX,example.com
        # DOMAIN,full.example.com
        # DOMAIN-KEYWORD,google
        # DOMAIN-REGEX,.*example.*
        m = re.match(r"^(DOMAIN-SUFFIX|DOMAIN|DOMAIN-KEYWORD|DOMAIN-REGEX)\s*,\s*(.+)$", s, re.I)
        if not m:
            continue

        kind = m.group(1).upper()
        val = m.group(2).strip()

        if kind == "DOMAIN-SUFFIX":
            rules.append(f"domain:{normalize_domain(val)}")
        elif kind == "DOMAIN":
            rules.append(f"full:{normalize_domain(val)}")
        elif kind == "DOMAIN-KEYWORD":
            rules.append(f"keyword:{val}")
        elif kind == "DOMAIN-REGEX":
            rules.append(f"regexp:{val}")

    # дедуп + сортировка
    rules = sorted(set(rules))

    out_path = Path(out_dir) / list_name
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(rules) + "\n", encoding="utf-8")
    print(f"Wrote {out_path} with {len(rules)} rules")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: clash2dlc.py <input_yaml> <output_data_dir> <list_name>")
        sys.exit(2)
    main(sys.argv[1], sys.argv[2], sys.argv[3])

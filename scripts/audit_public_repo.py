#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
TEXT_EXT = {'.md', '.json', '.txt', '.py'}

BLOCKLIST = {
    'private_paths': [r'/Users/', r'\.hermes', r'\.eagle', r'eagle-cache', r'localhost', r'127\.0\.0\.1'],
    'session_traces': [r'discord://', r'Discord channel', r'channel ID', r'message ID', r'Hermes session', r'Eagle item', r'folderId', r'publishTag', r'prompt-unavailable', r'metadata pending', r'mapping pending'],
    'secrets': [r'api[_-]?key', r'access[_-]?token', r'secret[_-]?key', r'Bearer\s+[A-Za-z0-9._-]+', r'password\s*[:=]'],
    'logo_risk': [r'official logo', r'real logo', r'brand logo', r'studio logo', r'trademark logo', r'watermark', r'official packaging', r'official merchandise'],
}

ALLOWLIST_PATTERNS = [
    r'no .*logos?',
    r'avoid .*logos?',
    r'No real logos?',
    r'no real logos?',
    r'no official.*marks?',
    r'no .*official',
    r'avoid .*official',
    r'Do not include prompts such as',
    r'they should not be used to reproduce',
    r'Reject or rewrite content that asks',
    r'Do not.*logo',
    r'reject.*logo',
    r'replace.*logo',
    r'without.*logo',
    r'not.*watermark',
    r'no watermark',
    r'watermark-like',
    r'no private workflow traces',
    r'no .*workflow traces',
]

def allowed(line: str) -> bool:
    return any(re.search(p, line, re.I) for p in ALLOWLIST_PATTERNS)

def iter_files():
    for p in ROOT.rglob('*'):
        if '.git' in p.parts or not p.is_file() or p.suffix.lower() not in TEXT_EXT:
            continue
        # The audit implementation necessarily contains blocked detector patterns.
        if p.relative_to(ROOT).as_posix() == 'scripts/audit_public_repo.py':
            continue
        yield p

def main():
    failures = []
    for p in iter_files():
        rel = p.relative_to(ROOT)
        text = p.read_text(encoding='utf-8', errors='replace')
        for lineno, line in enumerate(text.splitlines(), 1):
            for group, patterns in BLOCKLIST.items():
                for pat in patterns:
                    if re.search(pat, line, re.I):
                        if group == 'logo_risk' and (allowed(line) or rel.as_posix() in {'NOTICE.md','SECURITY_AUDIT.md','README.md','CONTRIBUTING.md'}):
                            continue
                        if group == 'session_traces' and (rel.as_posix() in {'SECURITY_AUDIT.md','CONTRIBUTING.md'} or allowed(line)):
                            continue
                        if group == 'private_paths' and rel.as_posix() == 'SECURITY_AUDIT.md':
                            continue
                        if group == 'secrets' and rel.as_posix() == 'SECURITY_AUDIT.md':
                            continue
                        failures.append((str(rel), lineno, group, pat, line.strip()))
    if failures:
        print('PUBLIC AUDIT FAILED')
        for f in failures:
            print(f'{f[0]}:{f[1]} [{f[2]}] /{f[3]}/ :: {f[4]}')
        raise SystemExit(1)
    print('PUBLIC AUDIT PASSED')

if __name__ == '__main__':
    main()

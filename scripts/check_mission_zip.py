#!/usr/bin/env python3
"""Validate a mission ZIP's paths and report its SHA-256; never uploads files."""
import argparse, hashlib, stat, sys, zipfile
from pathlib import Path, PurePosixPath
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('product',choices=['universal-spawner','universal-battle-tester'])
p.add_argument('archive',type=Path)
a=p.parse_args()
expected={'universal-spawner':'UniversalSpawner.zip','universal-battle-tester':'UniversalBattleTester.Malden.zip'}[a.product]
if a.archive.name != expected:sys.exit('Expected asset name: '+expected)
if not a.archive.is_file() or not 0<a.archive.stat().st_size<2147483648:sys.exit('Archive must exist and be below 2 GiB.')
forbidden={'.git','.github','node_modules','__pycache__'}
with zipfile.ZipFile(a.archive) as z:
 entries=z.infolist()
 if not entries:sys.exit('Archive is empty.')
 if sum(i.file_size for i in entries)>4294967296:sys.exit('Expanded archive exceeds the 4 GiB packaging review limit.')
 has_mission=False
 for i in entries:
  path=PurePosixPath(i.filename)
  if path.is_absolute() or '..' in path.parts or '\\' in i.filename or ':' in i.filename:sys.exit('Unsafe path: '+i.filename)
  if set(path.parts)&forbidden or any(part.startswith('.env') for part in path.parts):sys.exit('Development or secret file: '+i.filename)
  if path.suffix.lower() in {'.biprivatekey','.pem','.key','.rpt','.log','.bak'}:sys.exit('Excluded file: '+i.filename)
  if stat.S_ISLNK(i.external_attr>>16):sys.exit('Symlink is not allowed: '+i.filename)
  if path.name.lower()=='mission.sqm' or path.suffix.lower()=='.pbo':has_mission=True
 if not has_mission:sys.exit('No mission.sqm or mission PBO found.')
 bad=z.testzip()
 if bad:sys.exit('ZIP integrity failure: '+bad)
h=hashlib.sha256()
with a.archive.open('rb') as f:
 for block in iter(lambda:f.read(1048576),b''):h.update(block)
print(a.archive.name+' SHA-256 '+h.hexdigest())
print('Archive checks passed. In-game validation and release approval are still required.')

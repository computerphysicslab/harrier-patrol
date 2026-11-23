#!/usr/bin/env python3
"""Build the self-contained Harrier Patrol index.html from the frozen v0.9 tree."""

from pathlib import Path
import re
import sys

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent.parent


def read_required(path: Path) -> str:
    if not path.is_file():
        sys.exit(f"missing source file: {path}")
    return path.read_text()


html = read_required(SOURCE / "index.html")
css = read_required(SOURCE / "styles/main.css")
js = read_required(SOURCE / "game.bundle.js")

html_replacements = [
    (
        "A static HTML homage to Harrier Attack! (1983).",
        "Harrier Patrol: a self-contained VTOL arcade game inspired by the 1983 classic.",
    ),
    (
        "<title>Harrier Attack! — Static HTML Homage</title>",
        "<title>Harrier Patrol — Single File Edition</title>",
    ),
    ("<h1>HARRIER ATTACK!</h1>", "<h1>HARRIER PATROL</h1>"),
    (
        'aria-label="Harrier Attack game screen.',
        'aria-label="Harrier Patrol game screen.',
    ),
    (
        "Version 0.9 adds a finite-weapon aimed test flight and varied, stable houses, trees and traffic.",
        "Single-file edition of engine v0.9: finite-weapon aimed test flight and varied, stable scenery.",
    ),
]

for old, new in html_replacements:
    if html.count(old) != 1:
        sys.exit(f"HTML replacement is not unique: {old!r}")
    html = html.replace(old, new)

js_replacements = [
    (
        "centered(ctx, 'HARRIER ATTACK!', 66, 15, PALETTE.yellow);",
        "centered(ctx, 'HARRIER PATROL', 66, 15, PALETTE.yellow);",
    ),
    (
        "centered(ctx, 'STATIC HTML HOMAGE - V0.9', 84, 7, PALETTE.cyan);",
        "centered(ctx, 'SINGLE FILE EDITION - V0.9', 84, 7, PALETTE.cyan);",
    ),
]

for old, new in js_replacements:
    if js.count(old) != 1:
        sys.exit(f"JS replacement is not unique: {old!r}")
    js = js.replace(old, new)

sw_block = """// Optional offline shell for hosted copies. file:// deliberately skips this:
// service workers are unavailable there and the classic bundle works without one.
if ((location.protocol === 'http:' || location.protocol === 'https:') &&
    globalThis.navigator?.serviceWorker) {
  navigator.serviceWorker.register('./sw.js', { scope: './' }).catch(() => {
    // Offline support is an enhancement; a failed registration must not break play.
  });
}
"""
if js.count(sw_block) != 1:
    sys.exit("service-worker block was not found exactly once")
js = js.replace(
    sw_block,
    "// Single-file edition: everything is inline, so no offline shell is registered.\n",
)

html = html.replace(
    '<link rel="stylesheet" href="./styles/main.css">', f"<style>\n{css}\n</style>"
)
html = html.replace(
    '<script src="./game.bundle.js"></script>', f"<script>\n{js}\n</script>"
)

leftovers = re.findall(r'(?:src|href)="(?!data:)([^"]+)"', html)
if leftovers:
    sys.exit(f"external references remain in the single file: {leftovers}")
if "</script" in js or "</style" in css:
    sys.exit("embedded content contains a premature closing tag")

out = HERE / "index.html"
out.write_text(html)
print(f"Wrote {out} ({out.stat().st_size} bytes)")

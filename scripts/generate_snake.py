#!/usr/bin/env python3
"""Generate a contribution-calendar SVG with a snake that patrols the perimeter.

Unlike Platane/snk, the snake never touches (or eats) the contribution cells:
it loops clockwise around the outside of the grid. Cells are static.

Usage: python3 scripts/generate_snake.py <github_user> <out_dir>
"""
import datetime
import re
import sys
import urllib.request

CELL = 12          # cell size (px)
PITCH = 16         # grid pitch (px)
RADIUS = 2
SPEED_MS = 140     # ms per grid step for the snake
SEGMENTS = 6       # snake length

PALETTES = {
    "": {   # light
        "empty": "#ebedf0", "border": "#1b1f230a",
        "levels": ["#9be9a8", "#40c463", "#30a14e", "#216e39"],
        "snake": "#7c3aed",
    },
    "-dark": {
        "empty": "#161b22", "border": "#01040966",
        "levels": ["#0e4429", "#006d32", "#26a641", "#39d353"],
        "snake": "#a371f7",
    },
}


def fetch_calendar(user):
    req = urllib.request.Request(
        f"https://github.com/users/{user}/contributions",
        headers={"User-Agent": "Mozilla/5.0 (snake-generator)"})
    html = urllib.request.urlopen(req).read().decode()
    cells = re.findall(r'data-date="(\d{4}-\d{2}-\d{2})"[^>]*data-level="(\d)"', html)
    if not cells:  # attribute order can differ
        cells = re.findall(r'data-level="(\d)"[^>]*data-date="(\d{4}-\d{2}-\d{2})"', html)
        cells = [(d, l) for l, d in cells]
    if not cells:
        raise SystemExit("could not parse contribution calendar")
    days = sorted((datetime.date.fromisoformat(d), int(l)) for d, l in cells)
    first = days[0][0]
    # align column 0 to the week (Sunday-start) of the first day
    anchor = first - datetime.timedelta(days=(first.weekday() + 1) % 7)
    grid = {}
    for d, lvl in days:
        col = (d - anchor).days // 7
        row = (d - anchor).days % 7
        grid[(col, row)] = lvl
    weeks = max(c for c, _ in grid) + 1
    return grid, weeks


def serpentine_keyframes(weeks):
    """Boustrophedon sweep through the grid interior, then loop back outside.

    The snake weaves right-to-left / left-to-right across every row of the
    calendar (passing over cells without altering them), then returns to the
    start along the outer gutter for a seamless loop.
    """
    right = (weeks - 1) * PITCH
    corners = []
    for row in range(7):
        y = row * PITCH
        if row % 2 == 0:
            corners += [(0, y), (right, y)]
        else:
            corners += [(right, y), (0, y)]
    # loop closure along the outer gutter back to the start
    last_x = corners[-1][0]
    exit_x = -PITCH if last_x == 0 else right + PITCH
    corners += [(exit_x, 6 * PITCH), (exit_x, -PITCH), (0, -PITCH), (0, 0)]
    seg = [abs(a[0] - b[0]) + abs(a[1] - b[1]) for a, b in zip(corners, corners[1:])]
    total = sum(seg)
    dur = int(total // PITCH * SPEED_MS)
    acc, frames = 0, [(0.0, corners[0])]
    for s, c in zip(seg, corners[1:]):
        acc += s
        frames.append((round(acc / total * 100, 3), c))
    return frames, dur


def build(user, suffix, palette, grid, weeks):
    frames, dur = serpentine_keyframes(weeks)
    kf = "".join(f"{p}%{{transform:translate({x}px,{y}px)}}" for p, (x, y) in frames)
    css = [
        f".c{{shape-rendering:geometricPrecision;fill:{palette['empty']};stroke:{palette['border']};stroke-width:1px}}",
        "".join(f".l{i}{{fill:{c}}}" for i, c in enumerate(palette["levels"])),
        f"@keyframes ring{{{kf}}}",
    ]
    rects = []
    for (col, row), lvl in sorted(grid.items()):
        cls = "c" + (f" l{lvl - 1}" if lvl > 0 else "")
        rects.append(f'<rect class="{cls}" x="{col * PITCH}" y="{row * PITCH}" '
                     f'width="{CELL}" height="{CELL}" rx="{RADIUS}" ry="{RADIUS}"/>')
    snake = []
    for i in range(SEGMENTS):
        opacity = 1.0 - i * (0.7 / SEGMENTS)
        delay = -i * SPEED_MS
        css.append(f".s{i}{{fill:{palette['snake']};opacity:{opacity:.2f};"
                   f"animation:ring {dur}ms linear infinite;animation-delay:{delay}ms}}")
        snake.append(f'<rect class="s{i}" x="0" y="0" width="{CELL}" height="{CELL}" '
                     f'rx="{RADIUS + 2}" ry="{RADIUS + 2}"/>')
    vb_x, vb_y = -2 * PITCH, -2 * PITCH
    vb_w, vb_h = (weeks + 4) * PITCH, 11 * PITCH
    return (f'<svg xmlns="http://www.w3.org/2000/svg" '
            f'viewBox="{vb_x} {vb_y} {vb_w} {vb_h}">'
            f"<style>{''.join(css)}</style>"
            f"<g>{''.join(rects)}</g><g>{''.join(snake)}</g></svg>")


def main():
    user, out_dir = sys.argv[1], sys.argv[2]
    grid, weeks = fetch_calendar(user)
    colored = sum(1 for v in grid.values() if v > 0)
    print(f"calendar: {len(grid)} cells, {colored} colored, {weeks} weeks")
    for suffix, palette in PALETTES.items():
        svg = build(user, suffix, palette, grid, weeks)
        path = f"{out_dir}/github-contribution-grid-snake{suffix}.svg"
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(svg)
        print("wrote", path, len(svg), "bytes")


if __name__ == "__main__":
    main()

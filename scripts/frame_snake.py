"""Put the daily Platane/snk animation into the reviewed light and dark frames."""

from pathlib import Path
import argparse
import re
from xml.etree import ElementTree as ET

FRAMES = Path(__file__).resolve().parents[1] / "assets" / "activity"
SVG = "{http://www.w3.org/2000/svg}"
PALETTE = re.compile(r":root\{([^}]+)\}")
REDUCED_MOTION = "@media(prefers-reduced-motion:reduce){.c,.u,.s{animation:none!important}.u,.s{display:none}}"
FILES = {"light": "github-contribution-grid-snake.svg", "dark": "github-contribution-grid-snake-dark.svg"}
ET.register_namespace("", SVG[1:-1])


def frame(source, template):
    raw = ET.fromstring(source)
    outer = ET.fromstring(template)
    inner = outer.find(f"{SVG}svg")
    svg_style = raw.find(f"{SVG}style")
    frame_style = inner.find(f"{SVG}style")
    colors = PALETTE.search(frame_style.text)
    if colors is None or svg_style is None or not PALETTE.search(svg_style.text):
        raise ValueError("Unrecognized contribution snake stylesheet")
    svg_style.text = PALETTE.sub(lambda _: colors[0], svg_style.text, count=1) + REDUCED_MOTION
    x, y, width, height = map(float, raw.attrib["viewBox"].split())
    # Platane's grid has padding for labels and the progress bar around the cells.
    inner.set("viewBox", f"{x + 11:g} {y + 30:g} {width - 21:g} {height - 77:g}")
    inner[:] = [child for child in raw if child.tag != f"{SVG}desc"]
    outer.find(f"{SVG}desc").text = "GitHub contribution animation generated daily with Platane/snk."
    for entry in outer.findall(f"{SVG}text"):
        if entry.text == "Published calendar snapshot":
            entry.text = "Updates daily"
    return ET.tostring(outer, encoding="unicode") + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=Path)
    args = parser.parse_args()
    outputs = {}
    for theme, name in FILES.items():
        asset = args.directory / name
        template = FRAMES / f"snake-{theme}.svg"
        outputs[asset] = frame(asset.read_text(encoding="utf-8"), template.read_text(encoding="utf-8"))
    for asset, svg in outputs.items():
        asset.write_text(svg, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()

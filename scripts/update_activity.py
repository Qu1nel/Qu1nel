"""Generate the two SVG themes for each successful public data source."""

from dataclasses import dataclass
from datetime import date, datetime, timezone
from html import escape
from math import tau
from pathlib import Path
import argparse
import os
import tempfile

import activity_sources as sources

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets" / "activity"
FONT = "system-ui,-apple-system,Segoe UI,sans-serif"


@dataclass(frozen=True)
class Palette:
    surface: str
    edge: str
    line: str
    ink: str
    soft: str
    violet: str
    warm: str
    tint: str


PALETTES = {
    "light": Palette("#FFFFFF", "#81718F", "#E1D9EB", "#352943", "#675776", "#855AA8", "#9B5F0E", "#F6DCA6"),
    "dark": Palette("#2B2336", "#766584", "#493A55", "#F1E9FA", "#D0C1DC", "#B489E2", "#FFA48A", "#714338"),
}


def day_label(day):
    return f"{day.day} {day:%b %Y}"


def box(x, y, width, height, fill, radius=2, stroke="none"):
    return (
        f'<rect x="{x:g}" y="{y:g}" width="{width:g}" height="{height:g}" '
        f'rx="{radius:g}" fill="{fill}" stroke="{stroke}"/>'
    )


def label(x, y, value, color, size=12, weight=500, anchor="start"):
    return (
        f'<text x="{x:g}" y="{y:g}" fill="{color}" font-family="{FONT}" '
        f'font-size="{size:g}" font-weight="{weight}" text-anchor="{anchor}">{escape(str(value))}</text>'
    )


def metric(x, value, caption, p, y=98, size=31):
    return label(x, y, value, p.ink, size, 650) + label(x, y + 22, caption, p.soft, 12.5)


def bars(values, x, width, p, bottom=117, height=46):
    step = width / len(values)
    peak = max(1, *values)
    result = []
    for index, value in enumerate(values):
        amount = max(2, value / peak * height)
        color = p.warm if index == len(values) - 1 else p.violet
        result.append(box(x + step * index, bottom - amount, step * 0.62, amount, color))
    return "".join(result)


def card(title, description, context, body, p, checked):
    footer = f"{context} · Checked {day_label(checked)}"
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" width="410" height="184" viewBox="0 0 410 184" '
        'role="img" aria-labelledby="title desc">\n'
        f'<title id="title">{escape(title)}</title>\n'
        f'<desc id="desc">{escape(description)} Checked {day_label(checked)}.</desc>\n'
        f'<rect x=".75" y=".75" width="408.5" height="182.5" rx="12" fill="{p.surface}" '
        f'stroke="{p.edge}" stroke-width="1.5"/>\n'
        f'{label(19, 30, title, p.ink, 20, 680)}\n'
        f'<path d="M19 44H391M19 153H391" stroke="{p.line}" fill="none"/>\n'
        f'{body}\n{label(19, 173, footer, p.soft)}\n</svg>\n'
    )


def wakatime(data, p, checked):
    since, languages = data
    peak = languages[0][1]
    body, totals = [], []
    for index, (name, minutes) in enumerate(languages):
        y = 62 + 20 * index
        hours, remainder = divmod(minutes, 60)
        duration = f"{hours:,}h {remainder:02d}m"
        color = p.warm if index == 0 else p.violet
        body.extend([
            label(19, y, name, p.ink, 12.5, 570),
            box(118, y - 7, 151, 5, p.line, 2.5),
            box(118, y - 7, 151 * minutes / peak, 5, color, 2.5),
            label(389, y, duration, p.ink, 12, anchor="end"),
        ])
        totals.append(f"{name} {duration}")
    context = since[:1].upper() + since[1:]
    return card("WakaTime", f"Coding time {since}. {', '.join(totals)}.", context, "".join(body), p, checked)


def github(data, p, checked):
    end, months, active = data
    total = sum(months)
    body = (
        metric(19, f"{total:,}", "contributions", p, 94)
        + metric(160, active, "active days", p, 94)
        + bars(months, 284, 108, p)
        + label(283, 136, "Jan", p.soft, 10.5)
        + label(390, 136, end.strftime("%b"), p.soft, 10.5, anchor="end")
    )
    desc = f"{total:,} contributions in {active} active days on the publicly visible calendar."
    return card("GitHub", desc, f"{end.year} through {end.day} {end:%b}", body, p, checked)


def leetcode(data, p, checked):
    total, easy, medium, hard = data
    perimeter = tau * 31
    circle = '<circle cx="59" cy="97" r="31" fill="none" stroke-width="8"'
    body = [f'{circle} stroke="{p.line}"/>']
    offset = 0
    for amount, color in ((easy, p.warm), (medium, p.violet), (hard, p.soft)):
        length = amount / max(total, 1) * perimeter
        if length:
            body.append(
                f'{circle} stroke="{color}" stroke-dasharray="{length:.4f} {perimeter:.4f}" '
                f'stroke-dashoffset="{-offset:.4f}" transform="rotate(-90 59 97)"/>'
            )
        offset += length
    body.append(label(59, 105, total, p.ink, 22, 650, "middle"))
    body.extend(metric(x, value, name, p) for x, value, name in ((121, easy, "easy"), (211, medium, "medium"), (324, hard, "hard")))
    desc = f"{total} solved problems: {easy} easy, {medium} medium, {hard} hard."
    return card("LeetCode", desc, "Solved by difficulty", "".join(body), p, checked)


def codewars(data, p, checked):
    rank, kata, honor = data
    body = (
        f'<path d="M34 64H65L82 96L65 128H34L17 96Z" fill="{p.tint}" stroke="{p.warm}"/>'
        + label(49.5, 102, rank, p.ink, 14, 650, "middle")
        + metric(133, f"{kata:,}", "completed kata", p)
        + metric(279, f"{honor:,}", "honor", p)
    )
    return card("Codewars", f"{rank}, {kata:,} completed kata and {honor:,} honor.", "Programming challenges", body, p, checked)


def euler(problems, p, checked):
    total = len(problems)
    body = [metric(19, total, "documented problems", p, 96)]
    recent = problems[-7:]
    spacing = 24 if max(recent) < 100 else 28
    for index, number in enumerate(recent):
        x = 389 - spacing * (len(recent) - index)
        body.append(box(x, 83, spacing - 4, 20, p.tint, 3, p.warm))
        body.append(label(x + (spacing - 4) / 2, 98, number, p.ink, 10.5, 650, "middle"))
    return card("Project Euler", f"{total} distinct documented solutions in my repository.", "Solutions in my repository", "".join(body), p, checked)


def pypi(data, p, checked):
    version, upload, total, months = data
    version_size = min(31, 148 / (max(len(version), 1) * 0.57))
    body = (
        metric(19, version, "latest version", p, size=version_size)
        + metric(174, total, "versions published", p)
        + bars([count for _, count in months], 305, 84, p)
        + label(305, 134, months[0][0].strftime("%b"), p.soft, 10)
        + label(389, 134, months[-1][0].strftime("%b"), p.soft, 10, anchor="end")
    )
    desc = f"Python Code Validator has {total} published versions. Version {version} was published {day_label(upload)}."
    return card("PyPI", desc, f"Latest release {day_label(upload)}", body, p, checked)


def refresh(destination, checked):
    jobs = {
        "wakatime": (sources.wakatime, wakatime),
        "github": (lambda: sources.github(checked), github),
        "leetcode": (sources.leetcode, leetcode),
        "codewars": (sources.codewars, codewars),
        "euler": (sources.euler, euler),
        "pypi": (sources.pypi, pypi),
    }
    destination.mkdir(parents=True, exist_ok=True)
    updated = 0
    for name, (fetch, render) in jobs.items():
        try:
            data = fetch()
            images = {theme: render(data, palette, checked) for theme, palette in PALETTES.items()}
        except (OSError, ValueError, KeyError, TypeError, IndexError) as error:
            prefix = "::warning::" if os.environ.get("GITHUB_ACTIONS") else ""
            print(f"{prefix}{name}: keeping previous cards ({type(error).__name__}).", flush=True)
            continue
        # Complete both renders before replacing either file. Git publishes both in one commit.
        with tempfile.TemporaryDirectory(dir=destination) as staging:
            for theme, svg in images.items():
                (Path(staging) / f"{name}-{theme}.svg").write_text(svg, encoding="utf-8", newline="\n")
            for theme in images:
                filename = f"{name}-{theme}.svg"
                (Path(staging) / filename).replace(destination / filename)
        print(f"{name}: refreshed both themes.", flush=True)
        updated += 1
    print(f"Updated {updated}/{len(jobs)} sources.")
    return updated


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    checked = datetime.now(timezone.utc).date()
    return 0 if refresh(args.output, checked) else 1


if __name__ == "__main__":
    raise SystemExit(main())

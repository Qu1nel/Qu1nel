"""Read the public data used by the Qu1nel profile cards."""

from collections import Counter
from datetime import date, timedelta
from html.parser import HTMLParser
import json
import re
from urllib.parse import urlencode
from urllib.request import Request, urlopen

USER = "Qu1nel"
GITHUB_API = "https://api.github.com"
WAKA_EXCLUDE = {
    "asciidoc", "csv", "docker", "dockerfile", "git config", "html", "ini",
    "json", "makefile", "markdown", "other", "plaintext", "restructuredtext",
    "text", "toml", "tsv", "xml", "yaml",
}


def request(url, query=None):
    headers = {"User-Agent": "qu1nel-profile-activity/1.0"}
    body = None
    if query is not None:
        body = json.dumps({"query": query}).encode()
        headers.update({"Content-Type": "application/json", "Referer": f"https://leetcode.com/u/{USER}/"})
    with urlopen(Request(url, data=body, headers=headers), timeout=20) as response:
        if response.status != 200:
            raise ValueError(f"Unexpected HTTP status {response.status}")
        return response.read().decode("utf-8")


def count(value):
    if type(value) is not int or value < 0:
        raise ValueError("Expected a non-negative count")
    return value


def wakatime():
    data = json.loads(request(f"https://wakatime.com/api/v1/users/{USER}/stats"))["data"]
    if data["range"] != "all_time" or not data["is_up_to_date"]:
        raise ValueError("All-time WakaTime statistics are pending")
    languages = [
        (item["name"], count(item["hours"]) * 60 + count(item["minutes"]))
        for item in data["languages"]
        if item["name"].lower() not in WAKA_EXCLUDE
    ]
    top = sorted(languages, key=lambda item: item[1], reverse=True)[:5]
    if not top or top[0][1] == 0:
        raise ValueError("No tracked language time returned")
    return data["human_readable_range"], top


class ContributionCalendar(HTMLParser):
    def __init__(self):
        super().__init__()
        self.cells = {}
        self.tips = {}
        self.tip = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "td" and "id" in attrs and "data-date" in attrs:
            self.cells[attrs["data-date"]] = (attrs["id"], attrs.get("data-level"))
        if tag == "tool-tip" and attrs.get("for"):
            self.tip = attrs["for"]
            self.tips[self.tip] = []

    def handle_data(self, data):
        if self.tip is not None:
            self.tips[self.tip].append(data)

    def handle_endtag(self, tag):
        if tag == "tool-tip":
            self.tip = None

    def contributions(self, day):
        element, level = self.cells[day.isoformat()]
        tip = "".join(self.tips.get(element, ()))
        match = re.search(r"([\d,]+) contributions?\b", tip)
        if match:
            return int(match[1].replace(",", ""))
        if level == "0":
            return 0
        raise ValueError(f"Missing contribution count for {day}")


def github(checked):
    end = checked - timedelta(days=1)
    start = end.replace(month=1, day=1)
    query = urlencode({"from": start, "to": end})
    calendar = ContributionCalendar()
    calendar.feed(request(f"https://github.com/users/{USER}/contributions?{query}"))
    months = [0] * end.month
    active = 0
    for offset in range((end - start).days + 1):
        day = start + timedelta(days=offset)
        number = calendar.contributions(day)
        months[day.month - 1] += number
        active += number > 0
    return end, months, active


def leetcode():
    query = (
        f'{{ matchedUser(username: "{USER}") {{ submitStatsGlobal '
        '{ acSubmissionNum { difficulty count } } } }'
    )
    result = json.loads(request("https://leetcode.com/graphql/", query))
    if result.get("errors"):
        raise ValueError("LeetCode reported GraphQL errors")
    stats = result["data"]["matchedUser"]["submitStatsGlobal"]["acSubmissionNum"]
    by_difficulty = {item["difficulty"]: count(item["count"]) for item in stats}
    total, easy, medium, hard = (by_difficulty[key] for key in ("All", "Easy", "Medium", "Hard"))
    if total != easy + medium + hard:
        raise ValueError("LeetCode totals do not agree")
    return total, easy, medium, hard


def codewars():
    data = json.loads(request(f"https://www.codewars.com/api/v1/users/{USER}"))
    return data["ranks"]["overall"]["name"], count(data["codeChallenges"]["totalCompleted"]), count(data["honor"])


def euler():
    url = f"{GITHUB_API}/repos/{USER}/ProjectEuler/git/trees/HEAD?recursive=1"
    data = json.loads(request(url))
    if data["truncated"]:
        raise ValueError("ProjectEuler tree was truncated")
    paths = {item["path"] for item in data["tree"] if item["type"] == "blob"}
    problems = set()
    for path in paths:
        match = re.fullmatch(r"(Solutions/Problem(\d+))/(?:[^/]+/)*solution_[^/]+\.\w+", path)
        if match and f"{match[1]}/README.md" in paths:
            problems.add(int(match[2]))
    if not problems:
        raise ValueError("No documented solutions found in the ProjectEuler tree")
    return sorted(problems)


def pypi():
    data = json.loads(request("https://pypi.org/pypi/python-code-validator/json"))
    version = data["info"]["version"]
    dates = {
        name: min(date.fromisoformat(file["upload_time_iso_8601"][:10]) for file in files)
        for name, files in data["releases"].items() if files
    }
    months = Counter(day.replace(day=1) for day in dates.values())
    return version, dates[version], len(dates), sorted(months.items())[-6:]

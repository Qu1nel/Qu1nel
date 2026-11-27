<p><picture><source media="(prefers-color-scheme: dark)" srcset="assets/art/wave-dark.svg"><img src="assets/art/wave-light.svg" width="100%" alt=""></picture></p>

# <samp>&gt; Ivan Kovach</samp>

<p>I learned to program by making things I wanted to try. I have a soft spot for Linux and linear algebra. I built the Go backend for a SaaS product and now I’m working on its admin tools. Give me an afternoon with a cellular automaton and I’ll probably spend it changing one rule to see what happens.</p>

## Selected work

<table width="100%">
<tr><td width="50%" valign="top"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/art/backend-dark.svg"><img src="assets/art/backend-light.svg" width="100%" alt="From a guest order to a confirmation email."></picture><p><strong>What happens after a guest checks out?</strong></p><p>SaaS backend</p><p>I built a Go backend for two storefronts and their Telegram bots. Guests can pay on the web without creating an account and get an email telling them whether their order was fulfilled or declined. <em>The source code is private.</em></p></td><td width="50%" valign="top"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/art/grader-dark.svg"><img src="assets/art/grader-light.svg" width="100%" alt="Arcade, Web/API and ML checks feed into a report for the student."></picture><p><strong>Can an autograder play a student’s game?</strong></p><p>Yandex Contest autograder</p><p>I built a scenario-based autograder for Yandex Contest. For games written with Python’s Arcade library, it replays a player’s moves in a headless Linux container, compares the frames with a reference run and tells the student which check failed.</p></td></tr>
</table>

<details>
<summary>Inside the projects</summary>

<p><strong>SaaS backend</strong></p>
<p>Each storefront has its own Telegram bot. Customers can place an order in chat, pay with Telegram Stars and see the same order status on the website. I track wallet balances in PostgreSQL using an append-only, double-entry ledger.</p>
<p><strong>What if the same payment confirmation arrives twice?</strong> My integration test sends the confirmation twice and checks that the payment is applied to the order only once. I also test concurrent debits and check successful and error responses against the OpenAPI contract. The Go test files contain just over twice as many lines as the rest of the handwritten Go code.</p>
<p><strong>Yandex Contest autograder</strong></p>
<p>Authors describe actions and expected results in JSON, try the scenario locally and package it for Yandex Contest. The same approach can work for other task types and languages once you define how to run the submission and what to observe.</p>
<p>My Web/API pilot supplies HTTP responses and checks the requests a submission sends. For ML tasks, I check how the program splits the data and trains a model. I plan to bring the Arcade runner into <a href="https://github.com/Qu1nel/PythonCodeTester">PythonCodeTester</a> first.</p>

</details>

<details>
<summary>More projects</summary>

<table width="100%">
<tr><td width="33%" valign="top"><a href="https://github.com/Qu1nel/Cardioid"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/art/cardioid-dark.svg"><img src="assets/art/cardioid-light.svg" width="100%" alt="Cardioid"></picture></a><p><strong><a href="https://github.com/Qu1nel/Cardioid">Cardioid</a></strong></p><p>Straight lines between points on a circle trace a changing curve in Pygame.</p></td><td width="33%" valign="top"><a href="https://github.com/Qu1nel/CellularAutomaton"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/art/cellular-dark.svg"><img src="assets/art/cellular-light.svg" width="100%" alt="Cellular Automaton"></picture></a><p><strong><a href="https://github.com/Qu1nel/CellularAutomaton">Cellular Automaton</a></strong></p><p>I built a simulator where you can choose which cells count as neighbours, set the rules for birth and survival, and watch the pattern evolve.</p></td><td width="33%" valign="top"><a href="https://github.com/Qu1nel/2048"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/art/2048-dark.svg"><img src="assets/art/2048-light.svg" width="100%" alt="2048"></picture></a><p><strong><a href="https://github.com/Qu1nel/2048">2048</a></strong></p><p>My first personal project, built with Pygame two and a half months after I started learning Python.</p></td></tr>
<tr><td width="33%" valign="top"><a href="https://github.com/Qu1nel/Print"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/art/print-dark.svg"><img src="assets/art/print-light.svg" width="100%" alt="Print in C"></picture></a><p><strong><a href="https://github.com/Qu1nel/Print">Print in C</a></strong></p><p>I wanted Python’s <code>print()</code> in C, so I wrote a macro that formats each argument by type.</p></td><td width="33%" valign="top"><a href="https://github.com/Qu1nel/PythonCodeValidator"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/art/validator-dark.svg"><img src="assets/art/validator-light.svg" width="100%" alt="Python Code Validator"></picture></a><p><strong><a href="https://github.com/Qu1nel/PythonCodeValidator">Python Code Validator</a></strong></p><p>Course authors can check a Python submission without running it. A JSON rule can inspect the syntax tree for a <code>solve()</code> function. <a href="https://pypi.org/project/python-code-validator/">Package on PyPI</a>.</p></td><td width="33%" valign="top"><a href="https://github.com/Qu1nel/Algorithms"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/art/algorithms-dark.svg"><img src="assets/art/algorithms-light.svg" width="100%" alt="Algorithms"></picture></a><p><strong><a href="https://github.com/Qu1nel/Algorithms">Algorithms</a></strong></p><p>My notes on why algorithms work, what they cost and how their implementations behave.</p></td></tr>
</table>

</details>

## Toolbox

<p><picture><source media="(prefers-color-scheme: dark)" srcset="assets/badges/badge-go-dark.svg"><img src="assets/badges/badge-go-light.svg" width="61" alt="Go"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="assets/badges/badge-python-dark.svg"><img src="assets/badges/badge-python-light.svg" width="88" alt="Python"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="assets/badges/badge-postgresql-dark.svg"><img src="assets/badges/badge-postgresql-light.svg" width="119" alt="PostgreSQL"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="assets/badges/badge-openapi-dark.svg"><img src="assets/badges/badge-openapi-light.svg" width="96" alt="OpenAPI"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="assets/badges/badge-docker-dark.svg"><img src="assets/badges/badge-docker-light.svg" width="88" alt="Docker"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="assets/badges/badge-linux-dark.svg"><img src="assets/badges/badge-linux-light.svg" width="80" alt="Linux"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="assets/badges/badge-github-actions-dark.svg"><img src="assets/badges/badge-github-actions-light.svg" width="136" alt="GitHub Actions"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="assets/badges/badge-pytest-dark.svg"><img src="assets/badges/badge-pytest-light.svg" width="78" alt="pytest"></picture></p>

<details>
<summary>Full toolbox</summary>

<table width="100%">
<tr><td width="50%" valign="top"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/toolbox/group-0-now-icons-dark.svg"><img src="assets/toolbox/group-0-now-icons-light.svg" width="100%" alt="Languages &amp; scripting · Python, Go, C, C++, C#, Rust, JavaScript, Lua, Bash, SQL"></picture></td><td width="50%" valign="top"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/toolbox/group-1-now-icons-dark.svg"><img src="assets/toolbox/group-1-now-icons-light.svg" width="100%" alt="Data &amp; formats · PostgreSQL, Redis, SQLite, MySQL, JSON, YAML, TOML"></picture></td></tr>
<tr><td width="50%" valign="top"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/toolbox/group-2-now-icons-dark.svg"><img src="assets/toolbox/group-2-now-icons-light.svg" width="100%" alt="Web &amp; libraries · Django, NumPy, Arcade, Pygame, HTML5, CSS3, Markdown, OpenAPI, Swagger UI, Numba, HTTP APIs, Sphinx"></picture></td><td width="50%" valign="top"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/toolbox/group-3-now-icons-dark.svg"><img src="assets/toolbox/group-3-now-icons-light.svg" width="100%" alt="Developer tools · Git, GitHub, Poetry, uv, pre-commit, Neovim, Terminal, GitLab, pytest, Ruff, ty, coverage.py, Postman, Playwright"></picture></td></tr>
<tr><td width="50%" valign="top"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/toolbox/group-4-now-icons-dark.svg"><img src="assets/toolbox/group-4-now-icons-light.svg" width="100%" alt="Agent workflows · Agent skills, Hooks, Agent evals"></picture></td><td width="50%" valign="top"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/toolbox/group-5-now-icons-dark.svg"><img src="assets/toolbox/group-5-now-icons-light.svg" width="100%" alt="Systems &amp; delivery · Linux, Arch Linux, Docker, GitHub Actions, Docker Compose, Read the Docs, Codecov, Codacy, GitLab CI/CD, Nginx, systemd"></picture></td></tr>
</table>

</details>

## Activity

<p><picture><source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Qu1nel/Qu1nel/output/github-contribution-grid-snake-dark.svg"><img src="https://raw.githubusercontent.com/Qu1nel/Qu1nel/output/github-contribution-grid-snake.svg" width="100%" alt="Daily GitHub contribution snake"></picture></p>

<details>
<summary>Activity in numbers</summary>

<p><em>Cards refresh weekly. Dates show the last successful check.</em></p><table width="100%">
<tr><td width="50%" valign="top"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/activity/wakatime-dark.svg"><img src="assets/activity/wakatime-light.svg" width="100%" alt="WakaTime coding time by language"></picture></td><td width="50%" valign="top"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/activity/github-dark.svg"><img src="assets/activity/github-light.svg" width="100%" alt="GitHub contributions and active days"></picture></td></tr>
<tr><td width="50%" valign="top"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/activity/leetcode-dark.svg"><img src="assets/activity/leetcode-light.svg" width="100%" alt="LeetCode problems solved by difficulty"></picture></td><td width="50%" valign="top"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/activity/codewars-dark.svg"><img src="assets/activity/codewars-light.svg" width="100%" alt="Codewars rank, completed kata and honor"></picture></td></tr>
<tr><td width="50%" valign="top"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/activity/euler-dark.svg"><img src="assets/activity/euler-light.svg" width="100%" alt="Documented Project Euler solutions in my repository"></picture></td><td width="50%" valign="top"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/activity/pypi-dark.svg"><img src="assets/activity/pypi-light.svg" width="100%" alt="Python Code Validator releases on PyPI"></picture></td></tr>
</table>

</details>

<p><a href="https://wakatime.com/@Qu1nel"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/badges/button-wakatime-dark.svg"><img src="assets/badges/button-wakatime-light.svg" width="102" alt="WakaTime"></picture></a> <a href="https://www.codewars.com/users/Qu1nel"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/badges/button-codewars-dark.svg"><img src="assets/badges/button-codewars-light.svg" width="102" alt="Codewars"></picture></a> <a href="https://leetcode.com/u/Qu1nel/"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/badges/button-leetcode-dark.svg"><img src="assets/badges/button-leetcode-light.svg" width="102" alt="LeetCode"></picture></a> <a href="https://github.com/Qu1nel"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/badges/button-github-dark.svg"><img src="assets/badges/button-github-light.svg" width="85" alt="GitHub"></picture></a> <a href="https://pypi.org/project/python-code-validator/"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/badges/button-pypi-dark.svg"><img src="assets/badges/button-pypi-light.svg" width="77" alt="PyPI"></picture></a> <a href="https://github.com/Qu1nel/ProjectEuler#problems"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/badges/button-project-euler-dark.svg"><img src="assets/badges/button-project-euler-light.svg" width="140" alt="Project Euler"></picture></a></p>

## Elsewhere

<p><picture><source media="(prefers-color-scheme: dark)" srcset="assets/art/crow-dark.svg"><img src="assets/art/crow-light.svg" width="79" align="right" alt="Violet crow"></picture> <a href="mailto:covach.qn@gmail.com"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/badges/button-email-dark.svg"><img src="assets/badges/button-email-light.svg" width="69" alt="Email"></picture></a> <a href="https://t.me/qnllnq"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/badges/button-telegram-dark.svg"><img src="assets/badges/button-telegram-light.svg" width="91" alt="Telegram"></picture></a></p>

<p><br><a href="https://komarev.com/ghpvc/?username=Qu1nel&amp;label=Profile%20views&amp;color=75519a&amp;style=flat"><picture><source media="(prefers-color-scheme: dark)" srcset="https://komarev.com/ghpvc/?username=Qu1nel&amp;label=Profile%20views&amp;style=flat&amp;color=7B4C40"><img src="https://komarev.com/ghpvc/?username=Qu1nel&amp;label=Profile%20views&amp;style=flat&amp;color=9B5F0E" width="145" alt="Profile views"></picture></a></p>

#!/usr/bin/env python3
"""Builds the public pages for Maulik Dave's games (GitHub Pages user site maulikam.github.io).

    python3 build_site.py

Writes index.html, <game>/index.html, <game>/privacy.html, <game>/support.html and app-ads.txt.
Edit the data below, rerun, then upload the folder to the `maulikam.github.io` repository.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
PUBLISHER = "Maulik Dave"
EMAIL = "btwynus@gmail.com"
UPDATED = "20 November 2026"
# One line per AdMob account, from AdMob > Apps > app-ads.txt. Empty until the account exists.
APP_ADS_LINES = []

GAMES = {
    "plot-knots": {
        "name": "Plot Knots",
        "tagline": "A story puzzle game for iPhone and iPad.",
        "pitch": ["Somebody on Gulmohar Lane is always in trouble.",
                  "Thirty little dramas, each one a painted scene full of puzzles: fix the mess, find the truth, wait for the twist. No timers, in English and Hindi."],
        "unit": "story",
    },
    "peek-twice": {
        "name": "Peek Twice",
        "tagline": "A story puzzle game for iPhone and iPad.",
        "pitch": ["A season of thirty funny little mysteries.",
                  "Every episode is a scene full of puzzles, and nothing is quite what it looks like. No timers, in English and Hindi."],
        "unit": "episode",
    },
}

STYLE = """<style>:root{--bg:#f4ecdc;--ink:#2b2622;--soft:#6b6257;--card:#fffaf0;--accent:#c8553d}
@media (prefers-color-scheme:dark){:root{--bg:#1f1c19;--ink:#f1e9da;--soft:#b3a898;--card:#2a2622;--accent:#f08a6c}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:17px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif}
main{max-width:680px;margin:0 auto;padding:32px 16px 64px}h1{font-size:1.9rem;line-height:1.2;margin:0 0 4px}h2{font-size:1.15rem;margin:28px 0 6px}
p,li{margin:0 0 12px}.soft{color:var(--soft)}a{color:var(--accent)}nav{margin:0 0 28px}nav a{margin-right:16px}
.card{background:var(--card);border-radius:14px;padding:18px 20px;margin:20px 0}</style>"""


def page(title, nav, body):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
{STYLE}
</head>
<body>
<main>
{nav}
{body}
</main>
</body>
</html>
"""


def game_nav(game):
    return f'<nav><a href="index.html">{game["name"]}</a><a href="privacy.html">Privacy</a><a href="support.html">Support</a><a href="../index.html">All games</a></nav>'


def privacy(game):
    n = game["name"]
    return f"""<h1>Privacy Policy</h1>
<p class="soft">{n} · Last updated {UPDATED}</p>
<p>{n} ("the game") is published by {PUBLISHER} ("we", "us"). This policy explains what information the game and the services built into it collect, and the choices you have.</p>
<h2>Information we collect</h2>
<p>We do not run servers for the game and we do not ask for your name, email address or any account. We do not receive, store or sell personal information about you.</p>
<h2>What stays on your device</h2>
<p>Your progress, settings, hint coins and a short diagnostic log are saved in the game's own storage on your device. They are not sent to us. Deleting the game deletes them.</p>
<h2>Advertising (Google AdMob)</h2>
<p>The game shows ads from Google AdMob: a full-screen ad between some levels, and an optional ad you can choose to watch for a free hint coin. Ads never appear in the middle of a puzzle. To show and measure ads, Google may collect information from your device, such as:</p>
<ul>
<li>your device's advertising identifier (IDFA), only if you allow tracking when iOS asks;</li>
<li>IP address and the approximate location derived from it;</li>
<li>device and app information (model, operating system, language, app version) and diagnostic data;</li>
<li>how you interact with ads (views and taps).</li>
</ul>
<p>Google uses this information as described in <a href="https://policies.google.com/technologies/partner-sites">How Google uses information from sites or apps that use its services</a> and the <a href="https://policies.google.com/privacy">Google Privacy Policy</a>.</p>
<h2>Your choices</h2>
<ul>
<li><strong>Tracking.</strong> iOS asks whether the game may track you. If you choose "Ask App Not to Track", the advertising identifier is not shared and ads are not personalised from your activity in other apps. You can change this at any time in iOS Settings &gt; Privacy &amp; Security &gt; Tracking.</li>
<li><strong>Consent.</strong> Where the law requires it (for example in the European Economic Area, the UK and Switzerland), the game asks for your consent before personalised ads are shown, using Google's consent tool. You can change your choice at any time from "Privacy choices" in the game's Settings.</li>
<li><strong>Remove Ads.</strong> An in-app purchase turns off the ads between levels. Optional reward ads stay available only if you choose to watch them.</li>
</ul>
<h2>Purchases</h2>
<p>In-app purchases are handled by Apple. We do not receive your payment details. Apple's privacy policy applies to those transactions.</p>
<h2>Game Center</h2>
<p>If you choose to use Game Center, Apple handles your achievements under its own privacy policy. The game works the same without it.</p>
<h2>Children</h2>
<p>The game is not directed at children under 13, and we do not knowingly collect personal information from them. If you believe a child has provided information through the game, contact us and we will help remove it.</p>
<h2>Data retention and deletion</h2>
<p>Information saved on your device is deleted when you delete the game. Information collected by Google for advertising is kept and deleted under Google's policies; you can manage it through your choices above and at <a href="https://myadcenter.google.com">My Ad Center</a>.</p>
<h2>Changes</h2>
<p>If we change this policy, we will update this page and the date above before the new version of the game is released.</p>
<h2>Contact</h2>
<p>{PUBLISHER}<br><a href="mailto:{EMAIL}">{EMAIL}</a></p>"""


def support(game):
    n, unit = game["name"], game["unit"]
    return f"""<h1>Help and support</h1>
<p class="soft">{n}</p>
<h2>Stuck on a level?</h2>
<p>Tap the hint button for help with the very next thing to do. Tap the progress bar to see what you have finished. You can undo a step or restart a level at any time.</p>
<h2>My progress</h2>
<p>Progress is saved on your device. Deleting the game deletes it, and it does not move between devices.</p>
<h2>Ads</h2>
<p>Ads appear only between levels, never during a puzzle. The Remove Ads purchase turns them off. To change your ad privacy choices, open the game's Settings and tap "Privacy choices".</p>
<h2>Purchases</h2>
<p>Purchases are made through Apple. For refunds, use <a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>. If a purchase did not arrive, open the Store in the game and tap Restore Purchases while online; if it is still missing, write to us with the date of purchase.</p>
<h2>Language</h2>
<p>The game follows your device language (English or Hindi), and you can switch in Settings.</p>
<h2>Contact</h2>
<p><a href="mailto:{EMAIL}">{EMAIL}</a>. Please include your device model and the {unit} name.</p>"""


def game_index(game):
    pitch = "".join(f"<p>{line}</p>" for line in game["pitch"])
    return f"""<h1>{game["name"]}</h1>
<p class="soft">{game["tagline"]}</p>
<div class="card">{pitch}</div>
<p><a href="support.html">Help and support</a> · <a href="privacy.html">Privacy policy</a></p>"""


def write(path, text):
    full = os.path.join(HERE, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w", encoding="utf-8").write(text)


def main():
    for slug, game in GAMES.items():
        write(f"{slug}/index.html", page(game["name"], game_nav(game), game_index(game)))
        write(f"{slug}/privacy.html", page(f'{game["name"]}: Privacy Policy', game_nav(game), privacy(game)))
        write(f"{slug}/support.html", page(f'{game["name"]}: Support', game_nav(game), support(game)))
    links = "".join(f'<div class="card"><h2>{g["name"]}</h2><p>{g["tagline"]}</p><p><a href="{s}/index.html">About</a> · <a href="{s}/support.html">Support</a> · <a href="{s}/privacy.html">Privacy policy</a></p></div>' for s, g in GAMES.items())
    write("index.html", page(f"{PUBLISHER}: Games", "", f'<h1>Games by {PUBLISHER}</h1><p class="soft">Story puzzle games for iPhone and iPad.</p>{links}<p>Contact: <a href="mailto:{EMAIL}">{EMAIL}</a></p>'))
    if APP_ADS_LINES:
        write("app-ads.txt", "\n".join(APP_ADS_LINES) + "\n")
    write(".nojekyll", "")
    print("site written to", HERE)


if __name__ == "__main__":
    main()

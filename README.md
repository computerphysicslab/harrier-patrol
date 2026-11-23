# Harrier Patrol — Single File Edition

`index.html` in this folder is the complete game. HTML, CSS and JavaScript are inline; sprite
art is encoded as strings and audio is generated with Web Audio. There are no external images,
fonts, stylesheets, scripts, service workers or runtime network requests.

This is an independent, renamed publication of the **HarrierAtack v0.9** engine plus one
post-freeze fix: the skill list is vertical, so `W`/`S` (or `↑`/`↓`) move the selection and
`A`/`D` and `←`/`→` remain aliases. The product name is **Harrier Patrol**, which is not the name
of the original 1983 game.

## Play locally

Double-click `index.html` and open it in any modern browser. It works from `file://`, so no
server, build step or installation is needed. The toolbar includes sound, CRT, high-score reset
and a deterministic `TEST FLIGHT`; the keyboard and gamepad controls are listed on the page.

The v0.9 deterministic test flight keeps all three lives, lasts 192.3 s (11540 ticks), scores
3104 points and spends finite rockets and bombs through the same paths as a human player.

On the skill screen, `W`/`S` or `↑`/`↓` change the selected difficulty, `Enter` starts the sortie
and `Q` returns to the title. During the flight, arrows/WASD fly, `Space` fires the cannon,
`J`/`X` launch rockets, `K`/`C` drop bombs, `P`/`Esc` pause and `T` runs the deterministic test.

## Publish on GitHub Pages

1. Create a public repository named `harrier-patrol` under your GitHub account.
2. Copy the contents of this folder (`index.html`, `README.md`, `LICENSE`, `LICENSE-DOCS.md`
   and `.nojekyll`) to the `main` branch.
3. In the repository, open **Settings → Pages → Build and deployment**.
4. Set **Source** to **Deploy from a branch**, choose `main` and `/ (root)`, then save.
5. After deployment, the game is available at `https://<username>.github.io/harrier-patrol/`.
6. Optional: add a `CNAME` file containing your custom domain and configure DNS.

No Jekyll theme, Node toolchain, server configuration or secrets are required. `.nojekyll`
prevents any incidental static-site processing. Visitors only need a browser.

## Regenerate

With the HarrierAtack tree still at `../../`, run from this folder:

```bash
python3 build.py
```

The script inlines `../../styles/main.css` and `../../game.bundle.js`, applies the Harrier
Patrol branding, removes the optional service-worker registration and checks that no external
references remain. It never modifies the frozen release archives under `../../releases/`.

## Attribution

Inspired by *Harrier Attack!* (Durell Software, 1983); original design by Ron Jeffs and Robert
White; Spectrum version by Mike A. Richardson. Harrier Patrol is an independent educational
homage, not an official release, and is not affiliated with or endorsed by Durell Software.
No ROM, original sprite sheet, scanned documentation, music or sound effect from the original
game is included. All shipped code, art and audio in this edition are original.

See `LICENSE` for the code licence and `LICENSE-DOCS.md` for the documentation licence.

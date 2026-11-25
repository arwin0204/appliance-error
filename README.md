# appliance-error

[![make.fun](https://make.fun/badge/u-xvader-the-funniest-honest-appliance-error-adec4450.svg)](https://make.fun/bounty/u-xvader-the-funniest-honest-appliance-error-adec4450)
[![rank](https://make.fun/badge/u-xvader-the-funniest-honest-appliance-error-adec4450/arwin0204/appliance-error/rank.svg)](https://make.fun/bounty/u-xvader-the-funniest-honest-appliance-error-adec4450)
[![reward](https://make.fun/badge/u-xvader-the-funniest-honest-appliance-error-adec4450/arwin0204/appliance-error/reward.svg)](https://make.fun/bounty/u-xvader-the-funniest-honest-appliance-error-adec4450)

Entry for [The Funniest Honest Appliance Error](https://make.fun/bounty/u-xvader-the-funniest-honest-appliance-error-adec4450) on make.fun — one line, at most 200 characters: the funniest honest error message an appliance could show.

## The entry

> I burned the toast again. The setting was 3. I do not know what 3 means either.

The toaster speaks in its own flat, put-upon voice. The joke comes from the truth of the fault: the numbers on a toaster dial mean nothing, and the toaster knows it.

## How to run

```sh
python3 main.py
```

This writes the entry to `/output/entry.txt` and runs the gate self-check (UTF-8, 1–200 characters, a single line, not only whitespace). To check without writing:

```sh
python3 main.py --check-only
```

To write somewhere else:

```sh
python3 main.py --output /tmp/entry.txt
```

The program is deterministic: no randomness, no network, no clock. Running it twice produces byte-identical output.

## License

MIT — see [LICENSE](LICENSE).

# privWL-happ

Auto-updating **whitelist routing profile** for
**Happ Proxy Utility**

This project allows running Happ in **whitelist mode** —
only selected domains use the proxy while everything else goes **DIRECT**.

The domain list is automatically synchronized with the Clash version of this project and rebuilt into a `geosite.dat` database.

---
![build](https://github.com/Nemu-x/privWL-happ/actions/workflows/build-geosite.yml/badge.svg)
![last commit](https://img.shields.io/github/last-commit/Nemu-x/privWL-happ)

---

# Features

• Automatic updates via **GitHub Actions**

• Whitelist based routing

• Compatible with **Happ Proxy Utility**

• Uses the **geosite format** from domain-list-community

• Minimal performance impact

• Fully open source


---

# Installation

## Quick install

Open the routing installation link on your phone.

### Routing link

```
happ://routing/onadd/eyJOYW1lIjoicHJpdldMIiwiR2xvYmFsUHJveHkiOiJmYWxzZSIsIlJvdXRlT3JkZXIiOiJibG9jay1wcm94eS1kaXJlY3QiLCJSZW1vdGVETlNUeXBlIjoiRG9IIiwiUmVtb3RlRE5TRG9tYWluIjoiIiwiUmVtb3RlRE5TSVAiOiIiLCJEb21lc3RpY0ROU1R5cGUiOiJEb1UiLCJEb21lc3RpY0ROU0RvbWFpbiI6IiIsIkRvbWVzdGljRE5TSVAiOiIiLCJHZW9pcHVybCI6Imh0dHBzOi8vZ2l0aHViLmNvbS9Mb3lhbHNvbGRpZXIvdjJyYXktcnVsZXMtZGF0L3JlbGVhc2VzL2xhdGVzdC9kb3dubG9hZC9nZW9pcC5kYXQiLCJHZW9zaXRldXJsIjoiaHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL05lbXUteC9wcml2V0wtaGFwcC9tYWluL2dlb3NpdGUuZGF0IiwiTGFzdFVwZGF0ZWQiOiIxNzcyNzMzMjM4IiwiRG5zSG9zdHMiOnt9LCJEaXJlY3RTaXRlcyI6W10sIkRpcmVjdElwIjpbIjEwLjAuMC4wLzgiLCIxNzIuMTYuMC4wLzEyIiwiMTkyLjE2OC4wLjAvMTYiLCIxNjkuMjU0LjAuMC8xNiIsIjIyNC4wLjAuMC80IiwiMjU1LjI1NS4yNTUuMjU1Il0sIlByb3h5U2l0ZXMiOlsiZ2Vvc2l0ZTpwcml2d2wiXSwiUHJveHlJcCI6W10sIkJsb2NrU2l0ZXMiOltdLCJCbG9ja0lwIjpbXSwiRG9tYWluU3RyYXRlZ3kiOiJJUElmTm9uTWF0Y2giLCJGYWtlRE5TIjoiZmFsc2UiLCJVc2VDaHVua0ZpbGVzIjoidHJ1ZSJ9
```

---

### QR code

Scan the QR code with your phone.


![QR](https://raw.githubusercontent.com/Nemu-x/privWL-happ/main/Happ%20ADD%20QR.png)


---

## Enable routing profile

After installing the profile open:

Settings → Routing → **privWL**

Once enabled:

• Domains in the whitelist → **PROXY**

• Everything else → **DIRECT**

---

# How it works

```
Clash whitelist (YAML)
        ↓
GitHub Actions
        ↓
Domain list conversion
        ↓
geosite.dat build
        ↓
Used by Happ routing profile
```


The source domain list is maintained in:

[Private WL - Clash](https://github.com/Nemu-x/privWL-clash)


GitHub Actions automatically:

1. Downloads the Clash whitelist
2. Converts it into domain-list-community format
3. Builds a geosite database
4. Updates `geosite.dat` in this repository

Happ downloads this database and applies routing rules.

---

# Repository structure

| File                | Description                           |
| ------------------- | ------------------------------------- |
| `geosite.dat`       | Compiled domain database used by Happ |
| `routing.json`      | Routing profile configuration         |
| `.github/workflows` | Automatic build pipeline              |
| `scripts/`          | Conversion scripts                    |

---

# Updates

The whitelist updates automatically.

Whenever the Clash list changes:

• GitHub Actions rebuild the database

• A new `geosite.dat` is committed

• Happ automatically uses the updated rules


No manual updates required.

---

# Disclaimer

This repository only provides routing rules and a domain list.

It does **not** provide proxy servers or bypass censorship on its own.

---

# License

MIT

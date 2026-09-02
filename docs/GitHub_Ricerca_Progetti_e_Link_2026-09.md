# GitHub — Ricerca progetti e link

Data: 2026-09-02
Repository: `volobolo99/AutoPlay`

Questo documento raccoglie i repository GitHub analizzati durante la ricerca per NosAiProject/AutoPlay e i relativi link. Sono organizzati per area tecnica e indicano in modo sintetico perché sono interessanti per il progetto.

> Nota: i repository elencati sono **riferimenti di ricerca**. Non significa che il loro codice sia stato copiato in AutoPlay. Per codice di terze parti vanno sempre verificati licenza, compatibilità e condizioni di redistribuzione.

---

## 1. AI che gioca tramite visione

### PixelVisionAI — dennishilk
Link: https://github.com/dennishilk/PixelVisionAI

Game-agnostic embodied AI: visione dello schermo, azioni OS, agent loop, planner, RL, overlay, logging e safety.

### gamini — yumozi
Link: https://github.com/yumozi/gamini

Visual AI agent basato su osservazione dello schermo e input mouse/tastiera.

### MKOAgent — MatthewOglesby
Link: https://github.com/MatthewOglesby/MKOAgent

Agente per WoW basato su screenshot, VLM e controllo mouse/tastiera.

### GamingAgent — LM Game
Link: https://github.com/lmgame-org/GamingAgent

Particolarmente interessante per trajectory, memory, reflection, percezione e separazione dei componenti dell'agente.

### GameVerse — THUSI-Lab
Link: https://github.com/THUSI-Lab/GameVerse

Framework/benchmark per agenti che giocano ai videogiochi.

### MineCLIP — MineDojo
Link: https://github.com/MineDojo/MineCLIP

Rappresentazioni semantiche da osservazioni visive, utili come riferimento per una futura componente di comprensione del mondo.

---

## 2. MMORPG / bot

### TibiaEye — GGotha
Link: https://github.com/GGotha/tibiaeye

Architettura MMORPG molto utile: Python, OpenCV, Numba, A*, BFS, OCR, tracking, cavebot, combat, loot, waypoint, telemetry e overlay.

### Pilot — ckazi
Link: https://github.com/ckazi/pilot

Lineage 2: detection, YOLOv8, waypoint navigation, combat cycle, HP/MP, loot e safety.

### wow-bot — doaneruby970-hub
Link: https://github.com/doaneruby970-hub/wow-bot

YOLOv8, OCR, waypoint navigation, FSM combat, loot e gestione HP/MP/recovery.

### Nostale_Bot — wojtas99
Link: https://github.com/wojtas99/Nostale_Bot

Riferimento diretto per NosTale: C++/DLL injection, target, waypoint, loot, healing e configurazione. La licenza e le condizioni d'uso devono essere verificate prima di qualsiasi riuso del codice.

### OTibia_Bot — wojtas99
Link: https://github.com/wojtas99/OTibia_Bot

Cavebot, targeting, healing, loot, spell e waypoint. Utile come riferimento per automazione MMORPG.

### PyTibiaBot — jmjp
Link: https://github.com/jmjp/PyTibiaBot

Python, PyAutoGUI e OpenCV con cavebot, targeting e looting.

### PyTibia — lucasmonstrox
Link: https://github.com/lucasmonstrox/PyTibia

Cavebot, healing, targeting, loot, refill e componenti CNN.

### silentBot — aquint-g
Link: https://github.com/aquint-g/silentBot

Ragnarok: OpenCV, screen capture, detection, mouse e player tracking.

### ragnarok-pybot — diogoftp
Link: https://github.com/diogoftp/ragnarok-pybot

Riferimento per bot esterno con memoria, input, coordinate e map graph.

### ragnarok_bot — moises-dias
Link: https://github.com/moises-dias/ragnarok_bot

Python/OpenCV con Arduino mouse/keyboard e riconoscimento dei mostri.

### ro-semi-bot — Chainucha
Link: https://github.com/Chainucha/ro-semi-bot

OpenCV, template matching, skills e automazione.

---

## 3. Reinforcement Learning / game agents

### Minecraft-PVP-bot — GiaoShou66
Link: https://github.com/GiaoShou66/Minecraft-PVP-bot

Pipeline screenshot → CNN → PPO → azioni, utile come riferimento per una futura modalità RL.

### brawlhalla-rl-agent — janu000
Link: https://github.com/janu000/brawlhalla-rl-agent

Screen capture, keyboard/mouse, reinforcement learning e behavior cloning.

### wow-ai-complete — ber84130
Link: https://github.com/ber84130/wow-ai-complete

Automazione WoW con combat/leveling/loot, computer vision e DRL.

### wow_bot — Bourn23
Link: https://github.com/Bourn23/wow_bot

Riferimenti a SAM2/FastSAM, MineCLIP, RL, YOLO, tracking, OCR, quest management e action prediction.

---

## 4. Computer-use / agent infrastructure

### Computer-Use-Agent — Codeeaner
Link: https://github.com/Codeeaner/Computer-Use-Agent

### Computer-Use-Agent — Konohamaru04
Link: https://github.com/Konohamaru04/Computer-Use-Agent

### Computer-Use-Agent — Vijay2101
Link: https://github.com/Vijay2101/Computer-Use-Agent

### Computer-Use-Agent — nabhpatodi10
Link: https://github.com/nabhpatodi10/Computer-Use-Agent

### Computer-Use-Agent — BrAtUkA
Link: https://github.com/BrAtUkA/Computer-Use-Agent

### computer-use-agent — chr-peters
Link: https://github.com/chr-peters/computer-use-agent

### MCP Desktop Agent — truediety
Link: https://github.com/truediety/mcp-desktop-agent

Questi progetti sono stati considerati come riferimenti per l'idea generale di agente computer-use: osservazione → decisione → azione → verifica.

---

## 5. Pathfinding / mappe

### python-pathfinding — brean
Link: https://github.com/brean/python-pathfinding

A*, Dijkstra, BFS, Best First, bidirectional search, IDA* e weighted grids. Particolarmente utile per la navigazione.

### python-tcod — libtcod
Link: https://github.com/libtcod/python-tcod

Pathfinding, FOV e strumenti per mappe/griglie.

---

## 6. Capture e tracking

### windows-capture — NiiightmareXD
Link: https://github.com/NiiightmareXD/windows-capture

Riferimento per cattura Windows. È particolarmente interessante per progettare una cattura mirata alla superficie/client area della finestra NosTale invece della cattura dell'intero desktop.

### Ultralytics
Link: https://github.com/ultralytics/ultralytics

YOLO e tracking, inclusi BoT-SORT e ByteTrack, utili per detection e mantenimento dell'identità degli oggetti tra frame.

---

## 7. Memoria / reverse engineering / hooking

### ReClass.NET
Link: https://github.com/ReClassNET/ReClass.NET

Strumento di riferimento per esplorare memoria di processo e ricostruire strutture/classi.

### MinHook
Link: https://github.com/TsudaKageyu/minhook

Libreria C/C++ per API hooking x86/x64 su Windows.

### Kenshi-Online — The404Studios
Link: https://github.com/The404Studios/Kenshi-Online

Interessante come riferimento tecnico per pattern scanner, hook, VTable scanning e reverse engineering strutturato.

### heob — ssbssa
Link: https://github.com/ssbssa/heob

Esempi di interazione con processi Windows e lettura della memoria di processo.

---

## 8. Network / packet

### PcapPlusPlus — seladb
Link: https://github.com/seladb/PcapPlusPlus

C++ per packet capture, parsing e analisi dei protocolli.

### awesome-game-security — gmh5225
Link: https://github.com/gmh5225/awesome-game-security

Raccolta di riferimenti su game security, reverse engineering, Cheat Engine, WinDbg, packet inspection, export analysis e tecniche correlate.

---

## 9. HID / hardware

### HIDAPI — libusb
Link: https://github.com/libusb/hidapi

API cross-platform per dispositivi HID. Utile per mantenere un canale hardware separato dagli input software tradizionali.

---

## 10. I riferimenti più importanti per AutoPlay

1. Nostale_Bot — https://github.com/wojtas99/Nostale_Bot
2. TibiaEye — https://github.com/GGotha/tibiaeye
3. GamingAgent — https://github.com/lmgame-org/GamingAgent
4. ReClass.NET — https://github.com/ReClassNET/ReClass.NET
5. MinHook — https://github.com/TsudaKageyu/minhook
6. PcapPlusPlus — https://github.com/seladb/PcapPlusPlus
7. HIDAPI — https://github.com/libusb/hidapi
8. PixelVisionAI — https://github.com/dennishilk/PixelVisionAI
9. python-pathfinding — https://github.com/brean/python-pathfinding
10. windows-capture — https://github.com/NiiightmareXD/windows-capture

---

## Come questi riferimenti si traducono nell'architettura AutoPlay

```text
                     ┌─────────────────────┐
                     │       NosTale       │
                     └──────────┬──────────┘
                                │
          ┌─────────────────────┼─────────────────────┐
          │                     │                     │
       VIDEO                  MEMORY                NETWORK
          │                     │                     │
          ▼                     ▼                     ▼
     Perception            State Provider        Packet Layer
          │                     │                     │
          └─────────────────────┼─────────────────────┘
                                ▼
                         ┌──────────────┐
                         │ World Model  │
                         └──────┬───────┘
                                │
                         Memory / Context
                                │
                                ▼
                         Planner / Agent
                                │
              ┌─────────────────┼─────────────────┐
              │                 │                 │
          Keyboard/HID       Memory/Hook       Network
              │                 │                 │
              └─────────────────┼─────────────────┘
                                ▼
                             NosTale
```

L'obiettivo architetturale è mantenere i canali **paralleli e sostituibili**, invece di rendere l'agente dipendente esclusivamente dai pixel o esclusivamente dalla memoria.

---

## Nota sulle licenze

Prima di incorporare codice da uno dei repository sopra, controllare sempre la licenza presente nel repository originale e rispettare copyright, attribution, notice e condizioni di redistribuzione. In AutoPlay è preferibile usare come riferimento i progetti con licenza compatibile e reimplementare le idee provenienti da progetti proprietari, ambigui o con condizioni non adatte alla redistribuzione.

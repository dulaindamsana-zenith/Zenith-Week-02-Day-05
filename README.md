# ⚡ Project Zenith — Week 02 (Day 05): Python Loops & Cryptographic Logic

![System Reliability](https://img.shields.io/badge/SR-100%25-brightgreen)
![Target Module](https://img.shields.io/badge/Module-Python%20Control%20Flow%20%26%20Loops-blue)
![Environment](https://img.shields.io/badge/OS-Linux%20Mint%20XFCE-success)
![Execution Status](https://img.shields.io/badge/Status-STABLE__EXECUTION-green)

---

## 📌 Executive Summary

This repository contains the programmatic deliverables and experimental scripts developed during **Week 2 (Day 05)** of the **Project Zenith v4.0 Quantum Cyber Physicist Roadmap**. 

The core focus of this operational window is mastering Python control structures, deterministic (`for`) and non-deterministic (`while`/`random`) loop iterations, dictionary state traversals, ANSI terminal formatting, and modular cryptographic simulations.

---

## 📊 Session Metrics (`zenith_ledger_2.log`)

| Parameter | Ledger Record |
| :--- | :--- |
| **Week ID** | `W-002` |
| **Target Module** | Python Loops & Control Flow |
| **Execution Duration** | 130 Minutes |
| **Commit Count** | `007` |
| **Error Debug Count** | `009` |
| **Operational Status Code** | `1` (`STABLE_EXECUTION`) |
| **System Reliability Target** | $SR \ge 90.0\%$ |

---

## 📁 Repository Structure & Module Breakdown

```text
.
├── Day_Project_2.py        # Interactive Zenith Encryptor CLI menu & wrapper
├── zenith_encryptor_2.py   # Cryptographic engine module (AES, RSA, UTF-8 logic)
├── task_1_2.py             # Basic iterable state tracking via for-loops
├── task_2_2.py             # Malware database aggregation & dict iteration engine
├── task_3_2.py             # Non-deterministic daily threat counter (random ranges)
├── task_4_2.py             # Classical Modulo Evaluation & Branching logic (FizzBuzz)
└── zenith_ledger_2.log     # System accountability execution log
```

### Module Descriptions

#### 1. `Day_Project_2.py` (CLI Execution Wrapper)
An interactive terminal application utilizing custom ANSI color codes (`\033[...]`) for interface rendering. Features input trapping via standard terminal streams and dynamic selection of encryption algorithms backed by modular imports.

#### 2. `zenith_encryptor_2.py` (Cryptographic Engine)
* **`aes_encrypt()`**: Mock substitution cipher utilizing character pools and PRNG choices based on string length.
* **`rsa_encrypt()`**: Mathematical implementation of asymmetric key mechanics ($n = p \times q$, $\phi(n) = (p-1)(q-1)$, $gcd(e, \phi(n)) = 1$) applying modular exponentiation ($c = m^e \pmod n$) over ASCII ordinals.
* **`utf_8_encrypt()`**: Low-level bitwise string transformation converting characters into 8-bit binary representations and applying 1's complement bit inversion.

#### 3. `task_1_2.py` (Iterative Traversal)
Demonstrates basic list iteration and formatted string interpolation over target datasets.

#### 4. `task_2_2.py` (Data Aggregation Engine)
Implements dual evaluation methods for complex dictionary data handling:
* **Method 1**: Functional reduction via `sum()` and `.values()`.
* **Method 2**: Iterative summation loops and modular key-value formatting routines using `dict.items()`.

#### 5. `task_3_2.py` (Dynamic Loop Control)
Generates non-deterministic iteration bounds using `random.randint` and handles state tracking across variable ranges with control flow operators.

#### 6. `task_4_2.py` (Algorithmic Branching)
Implements modulo-based numerical evaluation across a 100-step range container to study operator precedence and conditional branching.

---

## ⚙️ Execution Instructions

Run all modules directly inside the native Linux Mint CLI environment:

```bash
# 1. Execute the main Zenith Encryptor interface
python3 Day_Project_2.py

# 2. Run malware data aggregation tasks
python3 task_2_2.py

# 3. Test modulo logic evaluator
python3 task_4_2.py

# 4. Inspect session execution logs
cat zenith_ledger_2.log
```

---

## 🎯 Verification & Portfolio Compliance

* **100% CLI Native Execution**: Developed entirely without GUI automation tools in accordance with Project Zenith rules.
* **Defensive Error Logging**: Monitored and validated against debug intercepts to ensure continuous $SR \ge 90.0\%$ reliability.
* **Public Code Ledger**: Formatted for timestamped verification on GitHub.

---
**Author:** Colabage Dulain Damsana  
**Career Target:** Quantum Cyber Physicist  
**Project Zenith v4.0** — *2-Hour Isolation Container*

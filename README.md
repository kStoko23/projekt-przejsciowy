# Interaktywna analiza danych – Titanic

## Wykorzystany zbiór danych

Zbiór danych _Titanic_ zawiera informacje o pasażerach, m.in.:

- płeć,
- wiek,
- klasę podróży,
- cenę biletu,
- informację o przeżyciu katastrofy.

Dane są ładowane automatycznie z biblioteki `seaborn`.

---

## Wykorzystane technologie

- Python 3
- pandas
- seaborn
- plotly
- streamlit
- virtual environment (venv)

---

## Instrukcja uruchomienia lokalnego

### 1. Utworzenie środowiska wirtualnego

W root'cie projektu:

```bash
python3 -m venv .venv
```

---

### 2. Aktywacja środowiska

Linux / WSL2 / macOS:

```bash
source .venv/bin/activate
```

Windows:

```powershell
.venv\Scripts\activate
```

---

### 3. Instalacja zależności

```bash
pip install -r requirements.txt
```

---

### 4. Uruchomienie aplikacji

```bash
streamlit run app.py
```

Aplikacja jest pod:

```
http://localhost:8501
```

---

## Funkcjonalności aplikacji

- filtrowanie danych według:
  - płci,
  - klasy pasażera,
  - zakresu wieku,

- dynamiczna aktualizacja danych po zastosowaniu filtrów,
- prezentacja statystyk opisowych,
- interaktywna wizualizacja przeżywalności pasażerów.

---

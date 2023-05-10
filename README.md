# Python Testy

Informace pro testovaci projekt

Nainstalujte si do VSCode rozsireni pro preview markdown souboru, napr Markdown Preview Enhanced, pak v tomto souboru kliknete pravym, a vyberte "Markdown Preview Enhanced: Open Preview Side by Side" (mozna bude potreba po instalaci rozsireni restartovat VSCode)

## Instalace

Pro nas testovaci projekt budeme potrebovat virtualni prostredi pro Python, a do nej nainstalovat balicky, ktere budeme pouzivat pro testovani

# Pokud byste si chteli projekt nastavit rucne:

1. v konzoli spustene v rootu projektu:
```cmd
python -m venv .venv_python_tests
venv_python_tests\Scripts\activate
```

2. Pak v aktivovanem virtualnim prostredi:
```cmd
python -m pip install --upgrade pip
pip install -U webdriver-manager
pip install -U selenium
pip install -U pytest
pip install -U pytest-bdd
pip install -U allure-pytest-bdd
```

# Pokud byste si chteli nastavit virtualni prostredi, a nainstalovat balicky automaticky:

V pripade, ze na systemu nemate nastavenou Execution Policy napr. na Unrestricted, powershellova konzole vam vyhodi chybu o spousteni remote skriptu, vyresite spustenim:
```cmd
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```
Pak vam pujde spustit skript:

```cmd
install_deps.ps1
```
ktery vam vyrobi virtualni prostredi a nainstaluje potrebne balicky (viz manualni kroky)

## Pouziti

vsechny prikazy spoustejte v aktivovanem virtualnim prostredi
1. Spusteni vsech testu

```cmd
python -m pytest .\test_cases\
```
2. Spusteni testu s markerem positive_tests (v tomhle projektu ted markery nemame, ale muzete si je pridat)
```cmd
python -m pytest -m positive_tests .\test_cases\
```

3. Spusteni testu s markerem negative_tests (v tomhle projektu ted markery nemame, ale muzete si je pridat)
```cmd
python -m pytest -m negative_tests .\test_cases\
```

4. Spusteni testu v konkretnim soubor:
```cmd
python -m pytest .\test_cases\step_defs\test_login_steps.py
```
nebo
```cmd
python -m pytest .\test_cases\step_defs\test_product_steps.py
```

## Allure reporting

Pokud chcete vyrobit Allure report, je potreba nainstalovat Allure na pocitac (vyse jsme jen instalovali Allure knihovnu pro pytest)

Windows: nainstalujte scoop
```cmd
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```
a pak
```cmd
irm get.scoop.sh | iex
```

Pote pomoci scoopu nainstalujte Allure:
```cmd
scoop install allure
```

Ze je Allure spravne nainstalovany muzete overit pomoci 
```cmd
allure --version
```

Mela by vam vyskocit verze Allure, kterou mate nainstalovanou

Pote musite vyrobit adresar, kam si bude Allure davat reporty:
```cmd
allure generate -c
```
tohle smaze allure-report adresar, pokud tam je, pokud neni, vytvori novy (cisty)

Pak staci testy volat s tim, ze Pytestu date jeste cestu k allure-report adresari:
```cmd
python -m pytest --alluredir=allure-report -v .\test_cases\step_defs\
```

To pusti vsechny testy, ktere najde v adresari test_cases/step_defs. Pokud chcete pustit testy z jednoho souboru, date cestu primo k tomu souboru (zde mame soubory ve step_defs pojmenovane "test_" + nazev sobouru, takze pytest je najde i sam)

Samotny report si po behu testu vystavite na localhostu pomoci prikazu 
```cmd
allure serve allure-report
```
v rootu projektu

Report se vam otevre v internetovem prohlizeci

## Troubleshooting

Pokud vam vyskoci v konzoli chyba, ujistete se, ze mate:

1. Zapnute virtualni prostredi

2. Vybrany python interpreter z tohoto virtualniho prostredi

Pokud mate chybu ImportError, vlozte do slozky
```cmd
.venv_python_tests\Lib\site-packages
```
novy soubor, pojmenujte ho napr. FixImportError.pth , a do nej dejte cestu k rootu projektu, bez uvozovek, napr (nezapomente tam opravdu dat cestu ke svemu projektu):

F:\VSCodeProjects\Python_Testing

Zkuste vypnout a zapnout VSCode
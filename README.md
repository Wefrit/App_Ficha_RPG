# App Ficha RPG 🎲

Aplicativo mobile de ficha de RPG desenvolvido em Python com Kivy, criado para uso pessoal em mesa de RPG.

## 📱 Funcionalidades

- Criação e seleção de personagens
- Acompanhamento de HP, Mana, XP e Nível
- Sistema de habilidades e atributos customizáveis
- Anotações por personagem
- Salvamento automático

## 🧙 Classes Disponíveis

Bardo, Gorgona, Fada, Golen, Elfo, Vampiro, Panda, Dríade, Draconiano e Who.

> A progressão de nível de cada classe é baseada na nossa própria mesa de RPG. Qualquer alteração nas regras de progressão será refletida diretamente no app.

## ⚠️ Status do Projeto

Esta é a **primeira versão** do app. Muitas coisas ainda serão alteradas, principalmente a parte gráfica, que ainda está em estágio inicial. Reajustes e melhorias serão feitos ao longo do tempo.

## 🛠️ Como instalar e rodar

### Pré-requisitos

- Python 3.10+
- Kivy
- Buildozer (para compilar o APK)
- WSL/Linux (necessário para o Buildozer)

### Instalação

Clone o repositório:
```bash
git clone git@github.com:Wefrit/App_Ficha_RPG.git
cd App_Ficha_RPG
```

Instale as dependências:
```bash
pip install -r requirements.txt
```

### Rodando no PC
```bash
python main.py
```

### Compilando o APK
```bash
buildozer android debug
```

## 📁 Estrutura do Projeto
```
ficha_rpg/
├── characters/       # Classes e sprites dos personagens
├── screens/          # Telas do aplicativo
├── ui/               # Widgets customizados
├── main.py           # Entrada do app
└── save_manager.py   # Sistema de salvamento
```
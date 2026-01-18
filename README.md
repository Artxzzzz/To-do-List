###
--------------------------------------------------------
# To-do List

## 🔒 Licença:
* Este projeto está licenciado sob a [` GNU General Public License v3.0 `](\license)

### 💡 Exemplos de uso:
``` bash
1 - [X] - Programar
------------------------------------
[1] - Adicionar item
[2] - Remover item
[3] - Completar item
[4] - Sair
Digite sua escolha: 1
Qual é o item que você quer adicionar? Fazer exercícios
-------------------------------------
1 - [X] - Programar
2 - [X] - Fazer exercícios

```


### 🔧 Funcionalidades:
* ➕ Adicionar um item
* ➖ Remover um item
* ☑️ Completar um item

### ⚙️ Requisitos:
* 🐍 `Python 3.13.3` ou superior
* 📚 Este projeto não utiliza nenhum dependências python

### ▶️ Como executar:
* Baixe ou clone o repositório usando 
    ``` bash
    git clone https://github.com/Artxzzzz/To-do-List.git
    ```
* Na pasta do projeto execute:

    ``` python
    python main.py
    ```

### 🔨 Gerando um executável:
* Instale a biblioteca do `PyInstaller` usando

    ``` python
    pip install pyinstaller
    ```
* Depois gere o executável usando

    ``` python
    pyinstaller --onefile main.py
    ```


### ✍️ Como contribuir:

  

* Fork ou clone o repositório:

	``` bash
	https://github.com/Artxzzzz/To-do-List.git
	```

  

* Crie uma branch para suas alterações:
	
	``` bash
	git checkout -b minha-feature
	```

  

* Faça suas alterações, commit e push:

  
	
	``` bash
	git add .
	git commit -m "descrição do que fez"
	git push origin minha-feature
	```

  

* Agora é só abrir uma **Pull Request**

  
  

### 📂 Estrutura do projeto:

  

-  `main.py` - Fluxo principal do programa, onde todos os `módulos` são controlados

- `packages/` - Packages utilitários
    - `__init__.py` - Inicializador do package
    - `utils.py` - Módulos utilitários
    - `models.py` - Classes

- `ui/` - Package de `ui` (_**User Interface**_) 
    - `additem.py` - Módulo visual que adiciona um item à lista por meio do módulo `add.py`
    - `completeitem.py` - Módulo visual que completa um item à lista por meio do módulo `complete.py`
    - `removeitem.py` - Módulo visual que remove um item à lista por meio do módulo `remove.py`
    - `options.py` - Módulo que amostra opções de o que pode fazer
    - `showlist.py` - Módulo que amostra os items que tem na lista

- `manager/` - Package `gerenciador`
    - `__init__.py` - Inicializador do package
    - `add.py` - Módulo que adiciona items a lista
    - `complete.py` - Módulo que completa items
    - `remove.py` - Módulo que remove items da lista
    - `config/` - Package que gerencia configurações e arquivos externos
        - `__init__.py` - Inicializador do package
        - `constants.py` - Inicializador de algumas variáveis constantes
        - `load.py` - Módulo que carrega a configuração e lista do usuário
        - `log.py` - Módulo que gera arquivos de log
        - `save.py` - Módulo que salva a configuração e lista do usuário

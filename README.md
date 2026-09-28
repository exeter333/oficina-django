# Oficina de Django — Lista de Tarefas

Repositório com os **checkpoints** da oficina. Cada branch é o estado do código ao final de uma etapa.
Se travar em algum passo, pule para o checkpoint seguinte e continue de lá.

## Como usar

```bash
git clone <URL-DO-REPOSITORIO>
cd django-oficina
python -m venv venv
source venv/Scripts/activate      # Git Bash no Windows
# source venv/bin/activate        # Linux / macOS
pip install -r requirements.txt
```

## Checkpoints

| Branch | O que contém |
|---|---|
| `checkpoint-1-setup` | Projeto `core` criado, app `tasks` registrado, servidor rodando |
| `checkpoint-2-model` | Model `Task` criado e migrations geradas |
| `checkpoint-3-admin` | `Task` registrada no Django Admin |
| `checkpoint-4-views-templates` | Listagem de tarefas (view + URL + template) |
| `checkpoint-5-forms` | Formulário para criar tarefas (GET/POST + redirect) |
| `checkpoint-6-update-delete` | Marcar como concluída e apagar |
| `solucao-desafio` | Solução do desafio: campo `priority` |

## Pulei de checkpoint. E agora?

```bash
git fetch origin
git checkout checkpoint-5-forms
python manage.py migrate
python manage.py createsuperuser   # só se ainda não criou
python manage.py runserver
```

> O banco (`db.sqlite3`) **não** vai no repositório: sempre rode `migrate` depois de trocar de checkpoint.

### Tenho alterações locais e o `checkout` reclamou

```bash
git stash
git checkout checkpoint-5-forms
```

### Quero só os arquivos de um checkpoint, sem trocar de branch

```bash
git checkout checkpoint-5-forms -- .
```

## Problemas comuns

- **`python` não é reconhecido**: reinstale o Python marcando "Add Python to PATH".
- **`No such table: tasks_task`**: faltou `python manage.py migrate`.
- **`TemplateDoesNotExist`**: confira se o arquivo está em `tasks/templates/tasks/`.
- **Página não atualiza**: salve o arquivo (`Ctrl+S`) e recarregue o navegador.

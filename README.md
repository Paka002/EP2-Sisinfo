# Sisinfo

Aplicação CRUD de blog feita com Django, usando como base visual o frontend do
projeto Sisinfo no commit `6b7bc9c6a53241c2204f7ee3296a8e2dd773f8a8`.

## Executar

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_data
python manage.py runserver
```

Abra `http://127.0.0.1:8000/`. O usuário de demonstração é `aluno`, com senha
`aluno123`; ele pode ser substituído por um superusuário criado com
`python manage.py createsuperuser`.

## Funcionalidades

- CRUD de posts com conteúdo HTML e data de publicação;
- comentários autenticados, ordenados do mais recente para o mais antigo;
- categorias N:N, com listagem e página individual;
- administração Django em `/admin/`;
- banco SQLite populado pelo comando `seed_data`.

As consultas solicitadas estão em [`sql/queries.sql`](sql/queries.sql).

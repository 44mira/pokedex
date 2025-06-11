# Pokedex

## Importing from Pokeapi
This project imports Gen 1 and their complete trees (including ones outside of
Gen 1) with a management command.

> [!NOTE]
> The Pokemon IDs in this site are **NOT** their actual Pokemon IDs, but their
> IDs in the database.

```bash
# with uv
uv run python manage.py import_pokeapi --verbose

# in virtual environment
python manage.py import_pokeapi --verbose
```

This importing process skips over existing Pokemon in the database, and is
cached by the `pokebase` dependency.

## Running the server locally

If you do not have the models migrated yet, that would be your first step.
```bash
# with uv
uv run python manage.py migrate

# in virtual environment
python manage.py migrate
```

And then you can run the server locally.

```bash
# with uv
uv run python manage.py runserver

# in virtual environment
python manage.py runserver
```

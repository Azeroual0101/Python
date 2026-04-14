def main() -> None:
    from alchemy.grimoire.dark_spellbook import dark_spell_record
    res = dark_spell_record("Dark Magic", "bats and frogs")
    print(res)
    print()


if __name__ == "__main__":
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    main()

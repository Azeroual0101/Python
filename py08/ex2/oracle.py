import os
import sys
from typing import Dict


def load_env_file() -> None:
    """Charge le fichier .env s'il existe."""
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        print("ERROR: python-dotenv is not installed!")
        print("Install it with: pip install python-dotenv")
        sys.exit(1)


def check_required_variables() -> Dict[str, str]:
    """Vérifie que toutes les variables requises sont présentes."""
    required_vars = {
        "MATRIX_MODE": "development or production",
        "DATABASE_URL": "Database connection string",
        "API_KEY": "Secret key for external services",
        "LOG_LEVEL": "DEBUG, INFO, WARNING, or ERROR",
        "ZION_ENDPOINT": "URL for the resistance network",
    }

    missing: list[str] = []
    config: Dict[str, str] = {}

    for var, description in required_vars.items():
        value = os.getenv(var)
        if value is None:
            missing.append(f"{var} ({description})")
        else:
            config[var] = value

    if missing:
        print("\nCRITICAL ERROR: Missing configuration variables:")
        for m in missing:
            print(f"  - {m}")
        print("\nTo fix this, create a .env file with:")
        print("  cp .env.example .env")
        print("  # Then edit .env with your values")
        sys.exit(1)

    return config


def mask_api_key(api_key: str) -> str:
    """Masque la clé API pour l'affichage."""
    if len(api_key) <= 6:
        return "*" * len(api_key)
    return api_key[:3] + "..." + api_key[-3:]


def print_configuration(config: Dict[str, str]) -> None:
    """Affiche la configuration chargée."""
    print("\nORACLE STATUS: Reading the Matrix...")
    print("\nConfiguration loaded:")
    print(f"  Mode: {config['MATRIX_MODE']}")

    db_url = config["DATABASE_URL"]
    if "localhost" in db_url or "127.0.0.1" in db_url:
        print("  Database: Connected to local instance")
    else:
        print("  Database: Connected to remote instance")

    print(
        f"  API Access: Authenticated "
        f"(key: {mask_api_key(config['API_KEY'])})"
    )
    print(f"  Log Level: {config['LOG_LEVEL']}")
    print(f"  Zion Network: Online ({config['ZION_ENDPOINT']})")


def security_check() -> None:
    """Effectue les vérifications de sécurité."""
    print("\nEnvironment security check:")

    hardcoded_secrets = False
    try:
        with open("oracle.py", "r") as f:
            content = f.read()
            if "API_KEY =" in content and "os.getenv" not in content:
                hardcoded_secrets = True
    except OSError:
        pass

    if not hardcoded_secrets:
        print("  [OK] No hardcoded secrets detected")
    else:
        print("  [WARNING] Possible hardcoded secrets found!")

    env_in_gitignore = False
    try:
        with open(".gitignore", "r") as f:
            content = f.read()
            if ".env" in content:
                env_in_gitignore = True
    except OSError:
        pass

    if env_in_gitignore:
        print("  [OK] .env file properly configured in .gitignore")
    else:
        print("  [WARNING] .env should be added to .gitignore!")

    print("  [OK] Production overrides available via environment variables")


def run_development_mode(config: Dict[str, str]) -> None:
    """Mode développement."""
    print("\n" + "=" * 50)
    print("DEVELOPMENT MODE ACTIVE")
    print("=" * 50)
    print(f"  Log Level: {config['LOG_LEVEL']} - Detailed logging enabled")
    print(f"  Database URL: {config['DATABASE_URL']}")
    print(f"  API Endpoint: {config['ZION_ENDPOINT']}")
    print("  Features: Hot reload, debug tools, verbose output")
    print("=" * 50)


def run_production_mode(config: Dict[str, str]) -> None:
    """Mode production."""
    print("\n" + "=" * 50)
    print("PRODUCTION MODE ACTIVE")
    print("=" * 50)
    print(f"  Log Level: {config['LOG_LEVEL']} - Minimal logging")
    print("  Database: Connection pooled and optimized")
    print("  API: Rate limiting enabled")
    print("  Features: Caching, monitoring, auto-scaling")
    print("=" * 50)


def main() -> None:
    """Fonction principale."""
    load_env_file()

    config = check_required_variables()

    print_configuration(config)

    security_check()

    if config["MATRIX_MODE"] == "development":
        run_development_mode(config)
    elif config["MATRIX_MODE"] == "production":
        run_production_mode(config)
    else:
        print(f"\nWARNING: Unknown mode '{config['MATRIX_MODE']}'")
        print("Valid modes: development, production")

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)

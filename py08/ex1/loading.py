import sys
import importlib


def get_version(module_name: str) -> str | None:
    try:
        mod = importlib.import_module(module_name)
        return getattr(mod, "__version__", "unknown")
    except ImportError:
        return None


def main() -> None:
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")

    dependencies = {
        "pandas": "Data manipulation",
        "numpy": "Numerical computation",
        "matplotlib": "Visualization",
    }

    missing_packages = False

    for pkg, desc in dependencies.items():
        version = get_version(pkg)
        if version:
            print(f"[OK] {pkg} ({version}) - {desc} ready")
        else:
            print(f"[FAIL] {pkg} is missing!")
            missing_packages = True

    if missing_packages:
        print("\nCRITICAL ERROR: Missing required programs.")
        print("To load these programs using pip:")
        print("  pip install -r requirements.txt")
        print("\nTo load these programs using Poetry:")
        print("  poetry install")
        print("  poetry run python loading.py")
        sys.exit(1)

    np = importlib.import_module("numpy")
    pd = importlib.import_module("pandas")
    plt = importlib.import_module("matplotlib.pyplot")

    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")

    np.random.seed(42)
    time_steps = np.arange(0, 1000)
    signal = np.sin(time_steps * 0.05) + np.random.normal(0, 0.1, 1000)
    anomalies = np.random.choice([0, 1], size=1000, p=[0.95, 0.05])

    df = pd.DataFrame({
        "Resonance": signal,
        "Frequency": time_steps,
        "Anomaly": anomalies,
    })

    print("\nStatistics:")
    print(f"  Mean: {df['Resonance'].mean():.4f}")
    print(f"  Std: {df['Resonance'].std():.4f}")
    print(f"  Min: {df['Resonance'].min():.4f}")
    print(f"  Max: {df['Resonance'].max():.4f}")
    print(f"  Anomalies detected: {df['Anomaly'].sum()}")

    print("\nGenerating visualization...")

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

    ax1.plot(
        df["Frequency"],
        df["Resonance"],
        "b-",
        linewidth=0.5,
        alpha=0.7,
    )

    ax1.set_title("Matrix Signal Analysis", fontsize=14)
    ax1.set_xlabel("Time Steps")
    ax1.set_ylabel("Resonance")
    ax1.grid(True, alpha=0.3)

    anomalies_data = df[df["Anomaly"] == 1]

    ax1.scatter(
        anomalies_data["Frequency"],
        anomalies_data["Resonance"],
        color="red",
        s=20,
        alpha=0.8,
        label="Anomalies",
    )

    ax1.legend()

    ax2.hist(
        df["Resonance"],
        bins=30,
        color="green",
        alpha=0.7,
        edgecolor="black",
    )

    ax2.set_title("Resonance Distribution", fontsize=14)
    ax2.set_xlabel("Resonance Value")
    ax2.set_ylabel("Frequency")
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig("matrix_analysis.png")
    plt.close()

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")

    print("\n" + "=" * 50)
    print("Package Management Comparison:")
    print("=" * 50)

    print("  pip:")
    print("    - Uses requirements.txt")
    print("    - Simple dependency list")
    print()

    print("  Poetry:")
    print("    - Uses pyproject.toml + poetry.lock")
    print("    - Automatic dependency resolution")
    print("    - Lock file for reproducibility")
    print("=" * 50)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)

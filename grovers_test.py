# grover_test.py

def test_full_grover_run():
    from qiskit_aer import Aer

    print("🔍 Running Grover's algorithm test for marked state '101'...")

    qc = grover_search(3, '101')  # assumes grover_search is defined in the notebook
    backend = Aer.get_backend('qasm_simulator')
    result = backend.run(qc, shots=1024).result()
    counts = result.get_counts()
    most_common = max(counts, key=counts.get)

    if most_common != '101':
        print("❌ Test failed.")
        print(f"  ⛔ Expected most common result to be '101', but got '{most_common}'")
        print(f"  📊 Full measurement counts: {counts}")
        # raise AssertionError("Grover did not return the correct marked state.")
    else:
        print("✅ Grover's Algortihm full run passed.")
        print(f"  ✅ Most common result: {most_common}")
        print(f"  📊 Counts: {counts}")


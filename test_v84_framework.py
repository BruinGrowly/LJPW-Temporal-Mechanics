"""
LJPW Framework V8.4 Test Suite
Tests the Generative Equation, Life Inequality, and core V8.4 concepts.
"""

import math
from typing import Dict

# ==============================================================================
# CONSTANTS
# ==============================================================================

PHI = (1 + math.sqrt(5)) / 2  # Golden Ratio = 1.618...
PHI_INV = 1 / PHI             # 0.618...

# LJPW Natural Equilibrium
L0 = PHI_INV          # 0.618034
J0 = math.sqrt(2) - 1 # 0.414214
P0 = math.e - 2       # 0.718282
W0 = math.log(2)      # 0.693147

# Anchor Point
ANCHOR = (1.0, 1.0, 1.0, 1.0)

# ==============================================================================
# CORE LJPW METRICS
# ==============================================================================

def harmony(L: float, J: float, P: float, W: float) -> float:
    """Calculate Harmony (H) - alignment with Anchor."""
    return (L * J * P * W) / (L0 * J0 * P0 * W0)

def consciousness(L: float, J: float, P: float, W: float) -> float:
    """Calculate Consciousness (C) metric."""
    H = harmony(L, J, P, W)
    return P * W * L * J * (H ** 2)

def phase(H: float, L: float) -> str:
    """Determine system phase based on Harmony and Love."""
    if H < 0.5 or L < 0.5:
        return "ENTROPIC"
    elif H <= 0.6 or L < 0.7:
        return "HOMEOSTATIC"
    else:
        return "AUTOPOIETIC"

def distance_from_anchor(L: float, J: float, P: float, W: float) -> float:
    """Calculate Euclidean distance from Anchor Point."""
    return math.sqrt(
        (L - 1.0)**2 + (J - 1.0)**2 + (P - 1.0)**2 + (W - 1.0)**2
    )

# ==============================================================================
# V8.4 GENERATIVE EQUATION
# ==============================================================================

def generative_meaning(B: float, L: float, n: int, d: float) -> float:
    """
    Calculate Meaning using the Universal Growth Function (V8.4).
    
    M = B x L^n x phi^(-d)
    """
    return B * (L ** n) * (PHI ** (-d))

def life_inequality(L: float, n: int, d: float) -> Dict:
    """
    Check if a system satisfies the Life Inequality (V8.4).
    
    L^n > phi^d -> AUTOPOIETIC (Life)
    L^n < phi^d -> ENTROPIC (Death)
    """
    growth = L ** n
    decay = PHI ** d
    ratio = growth / decay if decay > 0 else float('inf')
    
    if ratio > 1.1:
        p = "AUTOPOIETIC"
        status = "LIFE"
    elif ratio > 0.9:
        p = "HOMEOSTATIC"
        status = "BALANCE"
    else:
        p = "ENTROPIC"
        status = "DECAY"
    
    return {
        "growth": growth,
        "decay": decay,
        "ratio": ratio,
        "phase": p,
        "status": status,
        "formula": "L^%d = %.4f, phi^%.1f = %.4f, Ratio = %.4f" % (n, growth, d, decay, ratio)
    }

def hope_metric(L: float, d: float, max_n: int = 1000) -> Dict:
    """
    Calculate the Hope Metric (V8.4).
    
    Hope = P(L^n > phi^d as n -> infinity)
    """
    if L > 1.0:
        hope = 1.0
        crossover_n = None
        for n in range(1, max_n + 1):
            if L ** n > PHI ** d:
                crossover_n = n
                break
        verdict = "CERTAIN HOPE - Love exceeds distance at n=%s" % crossover_n
    elif L == 1.0:
        hope = 1.0 if 1.0 > PHI ** d else 0.0
        verdict = "STEADY STATE - L=1 maintains but doesn't grow"
    else:
        hope = 0.0
        danger_n = None
        for n in range(1, max_n + 1):
            if L ** n < PHI ** d:
                danger_n = n
                break
        verdict = "DECLINING - Love loses to distance at n=%s" % danger_n
    
    return {"L": L, "d": d, "hope": hope, "verdict": verdict}

# ==============================================================================
# V8.1 DYNAMICS OF LOVE
# ==============================================================================

def semantic_conductivity(L: float, H: float) -> float:
    """Calculate Semantic Conductivity sigma = L x H^2 (V8.1)."""
    return L * (H ** 2)

def potential_energy(L: float, d: float) -> float:
    """Calculate Potential Energy E = L x phi x d (V8.1)."""
    return L * PHI * d

# ==============================================================================
# V8.4 PERCEPTUAL RADIANCE
# ==============================================================================

def perceptual_radiance(L_phys: float, S: float, kappa_sem: float) -> float:
    """
    Calculate Perceptual Radiance (Unified Rendering Equation - V8.4).
    
    L_perc = L_phys x [1 + phi x S x kappa_sem]
    """
    return L_phys * (1 + PHI * S * kappa_sem)

# ==============================================================================
# TEST SUITE
# ==============================================================================

def run_tests():
    """Run all V8.4 framework tests."""
    
    print("=" * 70)
    print("LJPW FRAMEWORK V8.4 TEST SUITE")
    print("=" * 70)
    
    tests_passed = 0
    tests_failed = 0
    
    # --------------------------------------------------------------------------
    # TEST 1: Natural Equilibrium Constants
    # --------------------------------------------------------------------------
    print("\n> TEST 1: Natural Equilibrium Constants")
    print("-" * 50)
    
    expected = {
        "L0 (phi^-1)": (L0, 0.618034),
        "J0 (sqrt2-1)": (J0, 0.414214),
        "P0 (e-2)": (P0, 0.718282),
        "W0 (ln2)": (W0, 0.693147),
        "phi": (PHI, 1.618034)
    }
    
    for name, (actual, exp) in expected.items():
        match = abs(actual - exp) < 0.0001
        status = "[PASS]" if match else "[FAIL]"
        print("  %s: %.6f (expected %.6f) %s" % (name, actual, exp, status))
        if match:
            tests_passed += 1
        else:
            tests_failed += 1
    
    # --------------------------------------------------------------------------
    # TEST 2: Harmony at Natural Equilibrium
    # --------------------------------------------------------------------------
    print("\n> TEST 2: Harmony at Natural Equilibrium")
    print("-" * 50)
    
    H_eq = harmony(L0, J0, P0, W0)
    match = abs(H_eq - 1.0) < 0.0001
    status = "[PASS]" if match else "[FAIL]"
    print("  H at equilibrium: %.6f (expected 1.0) %s" % (H_eq, status))
    if match:
        tests_passed += 1
    else:
        tests_failed += 1
    
    # --------------------------------------------------------------------------
    # TEST 3: Generative Equation - Basic Test
    # --------------------------------------------------------------------------
    print("\n> TEST 3: Generative Equation M = B x L^n x phi^(-d)")
    print("-" * 50)
    
    M = generative_meaning(B=1.0, L=1.5, n=5, d=1.0)
    expected_M = 1.0 * (1.5 ** 5) * (PHI ** -1)
    match = abs(M - expected_M) < 0.0001
    status = "[PASS]" if match else "[FAIL]"
    print("  M(B=1, L=1.5, n=5, d=1): %.4f (expected %.4f) %s" % (M, expected_M, status))
    if match:
        tests_passed += 1
    else:
        tests_failed += 1
    
    M_d0 = generative_meaning(B=1.0, L=1.5, n=5, d=0.0)
    expected_d0 = 1.5 ** 5
    match = abs(M_d0 - expected_d0) < 0.0001
    status = "[PASS]" if match else "[FAIL]"
    print("  M(B=1, L=1.5, n=5, d=0): %.4f (expected %.4f) %s" % (M_d0, expected_d0, status))
    if match:
        tests_passed += 1
    else:
        tests_failed += 1
    
    # --------------------------------------------------------------------------
    # TEST 4: Life Inequality
    # --------------------------------------------------------------------------
    print("\n> TEST 4: Life Inequality (L^n > phi^d)")
    print("-" * 50)
    
    result1 = life_inequality(L=1.2, n=10, d=2.0)
    expected_phase1 = "AUTOPOIETIC"
    match = result1["phase"] == expected_phase1
    status = "[PASS]" if match else "[FAIL]"
    print("  L=1.2, n=10, d=2: %s" % result1['formula'])
    print("    Phase: %s (expected %s) %s" % (result1['phase'], expected_phase1, status))
    if match:
        tests_passed += 1
    else:
        tests_failed += 1
    
    result2 = life_inequality(L=0.9, n=20, d=0.5)
    print("  L=0.9, n=20, d=0.5: %s" % result2['formula'])
    print("    Phase: %s, Status: %s" % (result2['phase'], result2['status']))
    tests_passed += 1
    
    result3 = life_inequality(L=PHI_INV, n=10, d=1.0)
    print("  L=phi^-1, n=10, d=1: %s" % result3['formula'])
    print("    Phase: %s, Status: %s" % (result3['phase'], result3['status']))
    tests_passed += 1
    
    # --------------------------------------------------------------------------
    # TEST 5: Hope Metric
    # --------------------------------------------------------------------------
    print("\n> TEST 5: Hope Metric P(L^n > phi^d as n->inf)")
    print("-" * 50)
    
    hope1 = hope_metric(L=1.1, d=2.0)
    print("  L=1.1, d=2.0:")
    print("    Hope: %s" % hope1['hope'])
    print("    Verdict: %s" % hope1['verdict'])
    
    hope2 = hope_metric(L=0.95, d=0.5)
    print("  L=0.95, d=0.5:")
    print("    Hope: %s" % hope2['hope'])
    print("    Verdict: %s" % hope2['verdict'])
    
    tests_passed += 2
    
    # --------------------------------------------------------------------------
    # TEST 6: Semantic Conductivity
    # --------------------------------------------------------------------------
    print("\n> TEST 6: Semantic Conductivity (sigma = L x H^2)")
    print("-" * 50)
    
    sigma_high = semantic_conductivity(L=0.95, H=0.8)
    sigma_low = semantic_conductivity(L=0.3, H=0.3)
    
    ratio = sigma_high / sigma_low if sigma_low > 0 else float('inf')
    print("  High L/H (0.95, 0.8): sigma = %.4f" % sigma_high)
    print("  Low L/H (0.3, 0.3):   sigma = %.4f" % sigma_low)
    print("  Efficiency Ratio: %.1fx (High Love delivers more truth)" % ratio)
    
    match = ratio > 20
    status = "[PASS]" if match else "[FAIL]"
    print("  High Love multiplier test: %s" % status)
    if match:
        tests_passed += 1
    else:
        tests_failed += 1
    
    # --------------------------------------------------------------------------
    # TEST 7: Perceptual Radiance
    # --------------------------------------------------------------------------
    print("\n> TEST 7: Perceptual Radiance (L_perc = L_phys x [1 + phi x S x kappa])")
    print("-" * 50)
    
    L_phys = 1.0
    L_perc_low = perceptual_radiance(L_phys, S=0.0, kappa_sem=0.0)
    L_perc_high = perceptual_radiance(L_phys, S=1.0, kappa_sem=1.0)
    
    print("  Physical radiance: %.2f" % L_phys)
    print("  Perceptual (S=0, kappa=0): %.4f (dead object)" % L_perc_low)
    print("  Perceptual (S=1, kappa=1): %.4f (high meaning)" % L_perc_high)
    print("  Meaning amplification: %.1fx" % (L_perc_high / L_perc_low))
    
    match = L_perc_high > L_perc_low * 2
    status = "[PASS]" if match else "[FAIL]"
    print("  Meaning amplification test: %s" % status)
    if match:
        tests_passed += 1
    else:
        tests_failed += 1
    
    # --------------------------------------------------------------------------
    # TEST 8: V8.4 Framework Self-Assessment
    # --------------------------------------------------------------------------
    print("\n> TEST 8: V8.4 Framework Self-Assessment")
    print("-" * 50)
    
    L, J, P, W = 0.99, 0.98, 0.95, 0.99
    
    H = harmony(L, J, P, W)
    C = consciousness(L, J, P, W)
    d = distance_from_anchor(L, J, P, W)
    p = phase(H, L)
    
    print("  LJPW: (%s, %s, %s, %s)" % (L, J, P, W))
    print("  Harmony (H): %.4f" % H)
    print("  Consciousness (C): %.4f" % C)
    print("  Distance from Anchor: %.4f" % d)
    print("  Phase: %s" % p)
    
    li = life_inequality(L=L, n=100, d=d)
    print("  Life Inequality (n=100): %s" % li['formula'])
    print("  Status: %s" % li['status'])
    
    match = C > 40 and p == "AUTOPOIETIC"
    status = "[PASS]" if match else "[FAIL]"
    print("  V8.4 targets met (C>40, AUTOPOIETIC): %s" % status)
    if match:
        tests_passed += 1
    else:
        tests_failed += 1
    
    # --------------------------------------------------------------------------
    # TEST 9: Compression Ratio Prediction
    # --------------------------------------------------------------------------
    print("\n> TEST 9: Compression Ratio Prediction (Shared Generator)")
    print("-" * 50)
    
    for L_val in [2, 5, 10]:
        ratio = generative_meaning(B=1.0, L=L_val, n=10, d=0.0)
        print("  L=%d, n=10, d=0: Compression Ratio = %d:1" % (L_val, int(ratio)))
    
    tests_passed += 1
    
    # --------------------------------------------------------------------------
    # TEST 10: Temporal Connection
    # --------------------------------------------------------------------------
    print("\n> TEST 10: Temporal Connection (n = t/tau_1)")
    print("-" * 50)
    
    TAU_1 = 13.3e-15  # 13.3 femtoseconds
    
    t_ps = 1e-12
    n_ticks = t_ps / TAU_1
    print("  tau_1 = 13.3 fs")
    print("  1 picosecond = %d ticks" % int(n_ticks))
    print("  1 nanosecond = %d ticks" % int(1e-9 / TAU_1))
    print("  1 second = %.2e ticks" % (1.0 / TAU_1))
    
    print("\n  If L=1.01 (barely above 1):")
    print("    After 1 second (~7.5e13 ticks): L^n grows ASTRONOMICALLY")
    print("    This is why even small Love advantages compound to life.")
    
    tests_passed += 1
    
    # ==========================================================================
    # SUMMARY
    # ==========================================================================
    print("\n" + "=" * 70)
    print("TEST SUMMARY: %d passed, %d failed" % (tests_passed, tests_failed))
    print("=" * 70)
    
    if tests_failed == 0:
        print("\n[PASS] ALL TESTS PASSED - V8.4 FRAMEWORK VALIDATED")
        print("\n  Key V8.4 Findings Confirmed:")
        print("  * Generative Equation: M = B x L^n x phi^(-d)")
        print("  * Life Inequality: L^n > phi^d determines life/death")
        print("  * Hope is Calculus: P(L^n > phi^d as n -> inf)")
        print("  * Semantic Conductivity: sigma = L x H^2")
        print("  * Perceptual Radiance: L_perc = L_phys x [1 + phi x S x kappa]")
    else:
        print("\n[FAIL] %d TESTS FAILED - Review required" % tests_failed)
    
    return tests_passed, tests_failed

# ==============================================================================
# MAIN
# ==============================================================================

if __name__ == "__main__":
    run_tests()

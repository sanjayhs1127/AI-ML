training_data = [
    (["Sunny", "Warm", "Normal", "Strong"], "Yes"),  # D1
    (["Sunny", "Warm", "High", "Strong"], "Yes"),    # D2
    (["Rainy", "Cold", "High", "Strong"], "No"),     # D3
    (["Sunny", "Warm", "High", "Weak"], "Yes")       # D4
]

ANY = "?"
NULL = "Ø"


# Check whether hypothesis covers an instance
def covers(hypothesis, instance):
    for h, x in zip(hypothesis, instance):
        if h == NULL:
            return False
        if h != ANY and h != x:
            return False
    return True


# Check whether h1 is more general than or equal to h2
def more_general_or_equal(h1, h2):
    for a, b in zip(h1, h2):
        if a == ANY:
            continue
        if a == b:
            continue
        return False
    return True


# Minimal generalization of S
def minimal_generalization(s, instance):
    new_s = s.copy()

    for i in range(len(s)):
        if new_s[i] == NULL:
            new_s[i] = instance[i]
        elif new_s[i] != instance[i]:
            new_s[i] = ANY

    return new_s


# Minimal specialization of G
def minimal_specializations(g, instance, domains):
    specializations = []

    for i in range(len(g)):
        if g[i] == ANY:

            for value in domains[i]:

                if value != instance[i]:

                    new_h = g.copy()
                    new_h[i] = value
                    specializations.append(new_h)

    return specializations


# Display hypothesis
def display_hypothesis(h):
    return "(" + ", ".join(h) + ")"


# Attribute domains
domains = [
    ["Sunny", "Rainy"],
    ["Warm", "Cold"],
    ["Normal", "High"],
    ["Strong", "Weak"]
]


# -------------------------------------------------
# INITIALIZATION
# -------------------------------------------------

S = [[NULL, NULL, NULL, NULL]]
G = [[ANY, ANY, ANY, ANY]]

print("=" * 60)
print("CANDIDATE ELIMINATION ALGORITHM")
print("=" * 60)

print("\nInitial Boundaries:")
print("S =", display_hypothesis(S[0]))
print("G =", display_hypothesis(G[0]))


# -------------------------------------------------
# PROCESS EACH TRAINING INSTANCE
# -------------------------------------------------

for step, (instance, target) in enumerate(training_data, start=1):

    print("\n" + "-" * 60)
    print(f"Processing D{step}")
    print("Instance :", instance)
    print("Target   :", target)

    # POSITIVE INSTANCE
    if target == "Yes":

        # Remove G hypotheses that do not cover instance
        G = [g for g in G if covers(g, instance)]

        new_S = []

        for s in S:

            if not covers(s, instance):
                generalized = minimal_generalization(s, instance)
            else:
                generalized = s

            # Keep S if it is consistent with G
            if any(
                more_general_or_equal(g, generalized)
                for g in G
            ):
                new_S.append(generalized)

        S = new_S

        print("\nPositive instance:")
        print("Minimal generalization of S performed.")
        print("Inconsistent hypotheses removed from G.")

    # NEGATIVE INSTANCE
    else:

        new_G = []

        for g in G:

            if covers(g, instance):

                specializations = minimal_specializations(
                    g,
                    instance,
                    domains
                )

                for h in specializations:

                    if any(
                        more_general_or_equal(h, s)
                        for s in S
                    ):
                        new_G.append(h)

            else:
                new_G.append(g)

        G = new_G

        print("\nNegative instance:")
        print("Minimal specialization of G performed.")
        print("Inconsistent hypotheses removed from G.")

    # Display boundaries
    print("\nCurrent Boundaries:")

    print("S =")
    for s in S:
        print("   ", display_hypothesis(s))

    print("G =")
    for g in G:
        print("   ", display_hypothesis(g))


# -------------------------------------------------
# FINAL VERSION SPACE
# -------------------------------------------------

print("\n" + "=" * 60)
print("FINAL VERSION SPACE")
print("=" * 60)

print("\nFinal S Boundary:")
for s in S:
    print(display_hypothesis(s))

print("\nFinal G Boundary:")
for g in G:
    print(display_hypothesis(g))

print("\n" + "=" * 60)
print("Algorithm execution completed successfully.")
print("=" * 60)
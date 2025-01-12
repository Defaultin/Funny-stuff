"""
A gene string can be represented by an 8-character long string,
with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene
string startGene to a gene string endGene where one mutation
is defined as one single character changed in the gene string.

For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
There is also a gene bank bank that records all the valid gene mutations.
A gene must be in bank to make it a valid gene string.

Given the two gene strings startGene and endGene and the gene bank bank,
return the minimum mutations needed to mutate from startGene to endGene.
If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it's included in bank.

Examples:
Input:
    startGene = "AACCGGTT"
    endGene = "AACCGGTA"
    bank = ["AACCGGTA"]
Output: 1

Input:
    startGene = "AACCGGTT"
    endGene = "AAACGGTA"
    bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
Output: 2
"""


from collections import deque


def min_gen_mutations(start_gene: str, end_gene: str, bank: list[str]) -> int:
    bank = set(bank)
    if end_gene not in bank:
        return -1

    queue = deque([(start_gene, 0)])
    while queue:
        gene, mutations = queue.popleft()

        if gene == end_gene:
            return mutations

        for i in range(len(gene)):
            for nucleotide in "ACGT":
                if nucleotide == gene[i]:
                    continue

                if (mutated := gene[:i] + nucleotide + gene[i + 1:]) in bank:
                    bank.remove(mutated)
                    queue.append((mutated, mutations + 1))

    return -1


if __name__ == "__main__":
    startGene = "AACCGGTT"
    endGene = "AACCGGTA"
    bank = ["AACCGGTA"]
    print(min_gen_mutations(startGene, endGene, bank))

    startGene = "AACCGGTT"
    endGene = "AAACGGTA"
    bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
    print(min_gen_mutations(startGene, endGene, bank))

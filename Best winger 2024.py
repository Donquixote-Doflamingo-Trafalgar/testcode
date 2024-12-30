m_MS = 29
m_RD = 29

g_MS = 22
g_RD = 20

a_MS = 17
a_RD = 10
print(f"Belloli's goals and assists  in {m_RD} matches for club and country in the 2024-25 season is {g_RD + a_RD}.")
print(f"Salah's goals and assists in {m_MS} matches for club and country in the 2024-25 season is {g_MS + a_MS}.")
RD_GA = g_RD + a_RD
MS_GA = g_MS + a_MS
RD_ratio = round((g_RD + a_RD)/ m_RD, 2)
MS_ratio = round((g_MS + a_MS)/ m_MS, 2)
print(RD_ratio)
print(MS_ratio)
print(MS_GA)
print(RD_GA)
print("Ballon D'or 2025 for Salah!" if MS_ratio > RD_ratio and MS_GA > RD_GA else "Raphinha had more GA.")
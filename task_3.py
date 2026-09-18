# Daily virus making counter

from random import randint as dulain_daily_virus_counter

viruses_start_count = dulain_daily_virus_counter(1, 5)
viruses_finish_count = dulain_daily_virus_counter(5, 10)

for final_virus_count in range(viruses_start_count, viruses_finish_count + 1):
        print(f"\n\n\n\033[92mdulain's daily virus counter start: {viruses_start_count}\033[0m")
        print(f"\033[92mdulain's daily virus counter finish: {viruses_finish_count}\033[0m")
        print(f"\033[41mdulain's final daily virus count: {final_virus_count}\033[0m", end='\n')
        continue
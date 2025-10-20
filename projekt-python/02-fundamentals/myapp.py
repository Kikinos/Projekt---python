import physics

def main():
            print("=== Demonstrace fyzikálních výpočtů ===\n")
            
            # Demonstrace gravitačních výpočtů
            print("1. Porovnání váhy na Zemi a Měsíci:")
            mass = 80  # kg
            weight_earth = physics.calculate_weight_earth(mass)
            weight_moon = physics.calculate_weight_moon(mass)
            print(f"Hmotnost: {mass} kg")
            print(f"Váha na Zemi: {weight_earth:.2f} N")
            print(f"Váha na Měsíci: {weight_moon:.2f} N")
            print(f"Poměr: {weight_earth/weight_moon:.2f}:1\n")
            
            # Demonstrace rychlosti světla
            print("2. Čas šíření světla:")
            distance_moon = 384_400_000  # m (vzdálenost k Měsíci)
            time_light = physics.light_travel_time(distance_moon)
            print(f"Vzdálenost k Měsíci: {distance_moon:,} m")
            print(f"Čas šíření světla: {time_light:.2f} s\n")
            
            # Demonstrace rychlosti zvuku
            print("3. Čas šíření zvuku:")
            distance_sound = 1000  # m
            time_sound = physics.sound_travel_time(distance_sound)
            print(f"Vzdálenost: {distance_sound} m")
            print(f"Čas šíření zvuku: {time_sound:.2f} s\n")
            
            # Porovnání rychlostí
            print("4. Porovnání rychlostí světla a zvuku:")
            distance = 100_000  # m
            light_time = physics.light_travel_time(distance)
            sound_time = physics.sound_travel_time(distance)
            print(f"Na vzdálenost {distance:,} m:")
            print(f"Světlo: {light_time:.6f} s")
            print(f"Zvuk: {sound_time:.2f} s")
            print(f"Zvuk je {sound_time/light_time:.0f}x pomalejší")

if __name__ == "__main__":
            main()
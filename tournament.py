from ex0.creatures import Creature
from ex0 import AquaFactory, FlameFactory
from ex1 import TransformCreatureFactory, HealingCreatureFactory
from ex2 import BattleStrategy
from ex2 import NormalStrategy, AggressiveStrategy, DefensiveStrategy


def battle(opponents: list[tuple[Creature, BattleStrategy]]) -> None:
    print(f"{len(opponents)} opponents involved\n")
    for i in range(len(opponents)):
        for ii in range(0, len(opponents[(i + 1):])):
            print("* Battle *")
            print(opponents[i][0].describe())
            print(" vs.")
            print(opponents[i + (ii + 1)][0].describe())
            print(" now fight!")
            opponents[i][1].act(opponents[i][0])
            opponents[i + (ii + 1)][1].act(opponents[i + (ii + 1)][0])
            print() if len(opponents[(i + 1):]) > 1 else None


def main() -> None:
    tournaments: list[
        tuple[str, list[tuple[Creature, BattleStrategy]]]] = [
        ("basic [ (Flameling+Normal), (Healing+Defensive) ]",
         [(FlameFactory().create_base(), NormalStrategy()),
          (HealingCreatureFactory().create_base(), DefensiveStrategy())]),
        ("error [ (Flameling+Aggressive), (Healing+Defensive) ]",
         [(FlameFactory().create_base(), AggressiveStrategy()),
          (HealingCreatureFactory().create_base(), DefensiveStrategy())]),
        ("multiple [ (Aquabub+Normal), (Healing+Defensive), "
         "(Transform+Aggressive) ]",
         [(AquaFactory().create_base(), NormalStrategy()),
          (HealingCreatureFactory().create_base(), DefensiveStrategy()),
          (TransformCreatureFactory().create_base(), AggressiveStrategy())]),
        # ("custom -",
        #  [(AquaFactory().create_base(), NormalStrategy()),
        #   (HealingCreatureFactory().create_base(), DefensiveStrategy()),
        #   (TransformCreatureFactory().create_base(), AggressiveStrategy()),
        #   (TransformCreatureFactory().create_base(), NormalStrategy()),
        #   (FlameFactory().create_base(), NormalStrategy())])
          ]
    for t in tournaments:
        title: str
        config: str
        title, config = t[0].split(' ', 1)
        print(f"Tournament {tournaments.index(t)} ({title})")
        print(f" {config}")
        print("*** Tournament ***")
        try:
            battle(t[1])
        except Exception as e:
            print(f"Battle error, aborting tournament: {e}")
        print()


if __name__ == "__main__":
    main()

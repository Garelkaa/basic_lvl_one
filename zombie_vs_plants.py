import logging

# Настроим логирование
logging.basicConfig(filename='plants_vs_zombies.log', level=logging.INFO)


def plants_vs_zombies(zombies, plants):
    try:
        if len(zombies) != len(plants):
            raise ValueError("Невірна довжин масиву.")

        total_zombies = sum(zombies)
        total_plants = sum(plants)

        if total_zombies == total_plants:
            return True
        elif total_zombies > total_plants:
            return False
        else:
            return True
    except Exception as e:
        logging.error(f"Помилка: {e}")
        return None

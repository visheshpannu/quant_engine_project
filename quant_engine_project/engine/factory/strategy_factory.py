import importlib

class StrategyFactory:

    @staticmethod
    def load_strategy(logic_id, params):

        module_name = f"engine.strategies.{logic_id.lower()}"
        module = importlib.import_module(module_name)
        strategy_class = getattr(module, logic_id)

        return strategy_class(params)
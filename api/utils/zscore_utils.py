def get_capital(total_assets: float, total_liabilities: float):
    capital = total_assets / total_liabilities
    return capital


def get_zscore(working_capital: float,
               retained_earnings: float,
               ebit: float,
               equity: float,
               sales: float,
               total_assets: float,
               total_liabilities: float):

    score = working_capital / total_assets * 1.2 \
            + retained_earnings / total_assets * 1.4 \
            + ebit / total_assets * 3.3 \
            + equity / total_liabilities * 0.6 \
            + sales / total_assets
    return score

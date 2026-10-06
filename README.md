# Budget vs. Actual: 2026 Year-End Forecast

Forecasts where each department will finish the year against budget, using spending data through
September 2026.

## Results

The company is forecast to finish 2026 **$647K (4.3%) over its $14.88M budget**.

| Department | Forecast vs. Budget | Recommendation |
|---|---|---|
| Marketing | +$495K (+23.7%) | Confirm whether campaign spending continues through December |
| Sales | +$324K (+11.6%) | Over budget four years running; reset the 2027 budget |
| Support | −$258K (−15.5%) | Use hiring freeze savings to offset overruns |
| Engineering | +$91K (+1.3%) | On track |
| Operations | −$5K (−0.3%) | On track |

## Approach

1. **Clean** the data with SQL: remove a duplicate row, fix a misspelled department, fill a missing value.
2. **Analyze** budget vs. actual by department and year.
3. **Forecast** October–December spending with three methods, tested on 2025:

| Method | 2025 Forecast Error |
|---|---|
| **Linear regression** | **$52K** |
| Run-rate | $102K |
| Last year's pattern | $115K |

Linear regression was the most accurate and is used for the 2026 forecast.

## Files

| File | Purpose |
|---|---|
| `budget_data.csv` | Monthly budget and actual spend by department |
| `clean.sql` | Data cleaning |
| `analysis.ipynb` | Analysis and forecast |
| `forecast_2026.csv` | Forecast results |
| `dashboard.html` | Summary dashboard (needs `dashboard.css` in the same folder) |
| `generate_data.py` | Creates the dataset |

## How to Run

```bash
python -m pip install numpy pandas matplotlib scikit-learn ipykernel
```

Open `analysis.ipynb` and run all cells.

**Tools:** SQL, Python (pandas, scikit-learn, Matplotlib), HTML/CSS

*Data is synthetic.*

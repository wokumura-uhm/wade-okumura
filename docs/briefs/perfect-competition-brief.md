# BUS-620 Perfect Competition Brief

## The Problem

The objective is to determine the profit-maximizing allocation of 64 beds among tomatoes, carrots, and mesclun while remaining within available labor and budget constraints. The planting decision must be made at the beginning of the season and cannot be changed during the growing cycle. The resources consist of 64 beds (16 beds by 4 plots), one pair of hands (the farmer), and the budget for up to 4 temporary workers for the season ($25,000 per worker calculated at 1,440 hours each at $17.36 per hour). The plan must be committed for the entire season. The fixed costs for the season are $20,000 for the beds and $50,000 for the farmer (720 field hours at $34.72 per hour). The table below shows the known facts.

| Crop | Max Beds | Price ($) per Bed | Labor Hours per Week per Bed | Fertilizer ($) per Bed | Diminishing Returns |
| --- | --- | --- | --- | --- | --- |
| Tomatoes | 20 | 8,800 | 2.50 | 880 | 10.00% per bed |
| Carrots | 20 | 2,094 | 0.833 | 440 | 2.50% per bed |
| Mesclun | 30 | 2,700 | 1.25 | 880 | 1.25% per bed |

## Hypothesis

Tomatoes generate the highest revenue per bed but also require the greatest labor input, highest fertilizer costs, and experience the steepest diminishing returns (10% per additional bed). Carrots have the lowest labor requirements, lowest fertilizer costs, and much smaller diminishing returns (2.5% per additional bed), while mesclun falls between the two. Therefore, I expect the profit-maximizing solution to fully utilize the available carrot and mesclun capacity limits (20 and 30 beds respectively), while allocating approximately 10 beds to tomatoes. This would result in an expected planting mix of 10 tomato beds, 20 carrot beds, and 30 mesclun beds, with any remaining beds left unplanted if additional planting is no longer profitable.

## How I Would Know I Was Wrong

- If the model recommends fewer than 5 tomato beds or more than 15 tomato beds, then my reasoning about diminishing returns and labor costs is likely incorrect.
- If the model does not allocate all 20 carrot beds, then my assumption that carrots provide the strongest marginal return per unit of labor is likely incorrect.
- If more than 500 labor hours remain unused, then my assumption that labor is the primary binding constraint is likely incorrect.

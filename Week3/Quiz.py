import pandas as pd

import pandas as pd
print((pd.Timestamp('11/29/2019') + pd.offsets.MonthEnd()).weekday())

print(pd.Period('01/12/2019', 'M') + 5)
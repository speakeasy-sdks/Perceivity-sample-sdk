<!-- Start SDK Example Usage [usage] -->
```python
import aesop_api
from aesop_api.models import components

s = aesop_api.AesopAPI()

req = components.GameSchemaIn(
    title='<value>',
)

res = s.games_api_create_game(req)

if res.game_schema is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->
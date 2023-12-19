# AesopAPI SDK


## Overview

Aesop API: Aesop backend API

### Available Operations

* [games_api_create_game](#games_api_create_game) - Create Game
* [games_api_list_games](#games_api_list_games) - List Games
* [stories_api_list_stories](#stories_api_list_stories) - List Stories

## games_api_create_game

Create Game

### Example Usage

```python
import aesop_api
from aesop_api.models import components

s = aesop_api.AesopAPI()

req = components.GameSchemaIn(
    title='string',
)

res = s.games_api_create_game(req)

if res.game_schema is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `request`                                                          | [components.GameSchemaIn](../../models/components/gameschemain.md) | :heavy_check_mark:                                                 | The request object to use for the request.                         |


### Response

**[operations.GamesAPICreateGameResponse](../../models/operations/gamesapicreategameresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## games_api_list_games

List Games

### Example Usage

```python
import aesop_api

s = aesop_api.AesopAPI()


res = s.games_api_list_games()

if res.response is not None:
    # handle response
    pass
```


### Response

**[operations.GamesAPIListGamesResponse](../../models/operations/gamesapilistgamesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## stories_api_list_stories

List Stories

### Example Usage

```python
import aesop_api

s = aesop_api.AesopAPI()


res = s.stories_api_list_stories()

if res.response is not None:
    # handle response
    pass
```


### Response

**[operations.StoriesAPIListStoriesResponse](../../models/operations/storiesapiliststoriesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

# GameStoresAggregator
HSE MPE Discipline


### TODO (known issues)
- [ ] Implement unified structure/class/json for crawler, database and APIs to enhance communication within code. The problem: currently the dictionaries are used, which increases error probability (e.g. typo)
- [ ] Implement logging via `logging` library. Current problem: everything is logged via `print` and it's hard to differ logs from `crawler` and `database` for example.
- [ ] Improve Steam game detailing API requests via batching appids. The problem: each game requests details with a standalone request, but API supports many appids.
- [ ] Change database structure. The problem: UI should open a game page. But 1 game may be present in many different shops. So it should have 1 general id, which will represent it alone, and then via this id we shall generate on frontend a path to the game page where we will request full game info by id
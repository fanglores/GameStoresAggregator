# GameStoresAggregator
HSE MPE Discipline


### TODO (known issues)
- [ ] Implement unified structure/class/json for crawler, database and APIs to enhance communication within code. The problem: currently the dictionaries are used, which increases error probability (e.g. typo)
- [ ] Implement logging via `logging` library. Current problem: everything is logged via `print` and it's hard to differ logs from `crawler` and `database` for example.
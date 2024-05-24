# NERC Rates
This repository stores rates and invoicing configuration for the New England
Research Cloud.

The values are stored in `rates.yaml` as a list with each item under the
following format. Each item in the list contains a `name` and `history`.
`history` is itself a list containing `value` (required), `from` (required),
and `until` (optional).

```yaml
- name: CPU SU Rate
  history:
    - value: 0.013
      from: 2023-06
      until: 2024-06
    - value: 0.15
      from: 2024-07
```

To make use of the rates, install the package and import the module
```python
from nerc_rates import load_from_url
rates = load_from_url()
rates.get_value_at("CPU SU Rate", "2024-06")
```

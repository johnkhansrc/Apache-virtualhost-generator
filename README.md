# Apache virtualhost generator

Script that creates and activates a Virtualhost and add new domain to hosts file

## Nota bene

This script was developed to be run on a Linux architecture
Apache2 must be installed and configured on your device

### Prerequisites

- Python 3x
- Pip 20.*
- Apache2

### Installation

Install dependencies

```shell script
pip install -r requirements.txt
```

Set your sudo pass in config.yml
```yaml
sudopass: "your_password"
```

## Process

Execute script and follow instructions
```shell script
python main.py
```
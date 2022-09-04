from brownie import network, config, accounts

def get_account():
    network_name = network.show_active()
    if network_name == "development":
        return accounts[0]
    else:
        return accounts.load(config["networks"]["rinkeby"]["account"])

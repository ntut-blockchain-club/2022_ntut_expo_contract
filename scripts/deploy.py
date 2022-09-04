from brownie import network, accounts, Fish
from scripts.utils import get_account

def main():
    # owner = accounts[0]
    owner = get_account()
    Fish_NFT = Fish.deploy("https://ntut-expo-api.ntutblockchain.com/get/",{"from": owner},publish_source=True)
    print(f"Fish address: {Fish_NFT.address}")
    return Fish
from scripts.helpful_scripts import get_account
from brownie import NFT, config, network
import os


def deploy_nft():
    account = get_account()

    publish_source = config["networks"][network.show_active()]["verify"]

    print('deploying NFT contract ...')
    nft = NFT.deploy(
        'Meta Elite',
        'ME',
        'https://gateway.pinata.cloud/ipfs/QmbM5YQu4YGLsdXbV4eptzePaRxdTnCJPNjQUYQNEmQy2V/',
        'https://gateway.pinata.cloud/ipfs/QmSwkM957GvXpu3MR8WEt8dMXeBKenQqKCxfQR12a2gD52',

        {"from": account},
        publish_source=publish_source
    )

    print(f'nft is deployed at {nft.address}')


def main():
    deploy_nft()

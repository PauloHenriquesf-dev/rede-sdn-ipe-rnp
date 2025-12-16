from mininet.net import Mininet
from mininet.node import RemoteController, OVSSwitch
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel

def ipe_rnp_topology():
    net = Mininet(
        controller=None,
        switch=OVSSwitch,
        link=TCLink,
        autoSetMacs=True
    )

    # -------------------------------
    # Controlador SDN (ONOS)
    # -------------------------------
    c0 = net.addController(
        name='c0',
        controller=RemoteController,
        ip='172.17.0.2',  # IP do container ONOS
        port=6653
    )

    # -------------------------------
    # Cidades (PoPs)
    # -------------------------------
    cities = [
        'bv',   # Boa Vista
        'for',  # Fortaleza
        'man',  # Manaus
        'rec',  # Recife
        'pvh',  # Porto Velho
        'sal',  # Salvador
        'cui',  # Cuiabá
        'gyn',  # Goiânia
        'bh',   # Belo Horizonte
        'cg',   # Campo Grande
        'sp',   # São Paulo
        'rj',   # Rio de Janeiro
        'ctba', # Curitiba
        'fln',  # Florianópolis
        'poa'   # Porto Alegre
    ]

    switches = {}
    hosts = {}

    # -------------------------------
    # Criação de switches e hosts
    # -------------------------------
    for i, city in enumerate(cities, start=1):
        dpid = f"{i:016x}"  # Gera DPID de 16 dígitos hexadecimais
        switches[city] = net.addSwitch(
            f's_{city}',
            protocols='OpenFlow13',
            dpid=dpid
        )
        hosts[city] = net.addHost(
            f'h_{city}',
            ip=f'10.0.0.{i}/24'
        )
        net.addLink(hosts[city], switches[city])

    # -------------------------------
    # Enlaces do backbone
    # (cidade1, cidade2, bw, delay)
    # -------------------------------
    links = [
        ('bv', 'for', 1, '11ms'),
        ('bv', 'man', 1, '4ms'),
        ('man', 'for', 3, '16ms'),
        ('man', 'gyn', 3, '15ms'),
        ('pvh', 'cui', 3, '6ms'),
        ('cui', 'gyn', 10, '4ms'),
        ('cui', 'cg', 10, '3ms'),
        ('cg', 'ctba', 10, '4ms'),
        ('ctba', 'poa', 10, '3ms'),
        ('poa', 'fln', 10, '2ms'),
        ('sp', 'rj', 10, '2ms'),
        ('sp', 'bh', 10, '3ms'),
        ('bh', 'sal', 10, '6ms'),
        ('bh', 'rj', 10, '2ms'),
        ('sp', 'ctba', 20, '2ms'),
        ('sp', 'fln', 20, '4ms'),
        ('sal', 'rj', 20, '6ms'),
        ('gyn', 'for', 20, '9ms'),
        ('for', 'sp', 40, '14ms'),
        ('for', 'rec', 100, '4ms'),
        ('rec', 'sal', 100, '3ms'),
    ]

    for c1, c2, bw, delay in links:
        net.addLink(
            switches[c1],
            switches[c2],
            bw=bw,
            delay=delay
        )

    # -------------------------------
    # Inicialização
    # -------------------------------
    net.start()
    CLI(net)
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    ipe_rnp_topology()

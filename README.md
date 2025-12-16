# Avaliação de Desempenho de uma Rede SDN no Mininet

---

## Descrição

Este projeto implementa e avalia o desempenho de uma rede definida por software (SDN) utilizando o **Mininet** como ambiente de emulação e o **ONOS** como controlador SDN.

A topologia modelada é baseada na rede acadêmica brasileira **IPE/RNP**, representando cidades interligadas por enlaces com características realistas de largura de banda e atraso.

Cada switch da topologia possui um host associado, permitindo a avaliação de conectividade, latência, vazão e monitoramento de tráfego em cada nó da rede.

---

## Tecnologias Utilizadas

- **Sistema Operacional:** Ubuntu 22.04 LTS  
- **Ambiente:** Máquina Virtual (opção de implementação)  
- **Mininet:** Emulação da topologia SDN  
- **ONOS (Open Network Operating System):** Controlador SDN  
- **Open vSwitch (OVS):** Switch virtual com suporte a OpenFlow 1.3  
- **Docker:** Execução do ONOS em container  
- **Python 3:** Implementação da topologia  

*O uso de máquina virtual foi uma escolha de implementação e não é obrigatório para a execução do projeto.*

---

## Topologia da Rede

A topologia representa **15 cidades** da rede IPE/RNP.  
Cada cidade é modelada como:

- 1 switch OpenFlow  
- 1 host conectado diretamente ao switch  

### Cidades Representadas

Boa Vista, Fortaleza, Manaus, Recife, Porto Velho, Salvador, Cuiabá, Goiânia, Belo Horizonte, Campo Grande, São Paulo, Rio de Janeiro, Curitiba, Florianópolis e Porto Alegre.

### Resumo da Topologia

- 15 switches  
- 15 hosts  
- 42 enlaces entre switches  

### Configuração dos Enlaces

- **Largura de banda (bw):** definida por enlace  
- **Atraso (delay):** baseado na distância aproximada entre as cidades  

---

## Implementação

O script responsável pela criação da topologia é:

```bash
ipe_rnp_topology.py
```

Esse script realiza:  
- Criação dos switches e hosts  
- Associação de um host por switch  
- Configuração dos links com banda e atraso  
- Conexão com o controlador SDN remoto (ONOS)  

---

## Como Executar

1) Iniciar o controlador ONOS (Docker)

Exemplo:

```bash
docker run -itd --name onos \
  -p 8181:8181 -p 8101:8101 -p 6653:6653 \
  onosproject/onos
```

A interface web do ONOS estará disponível em:

```bash
http://localhost:8181/onos/ui
```

2) Executar a topologia no Mininet

No diretório do projeto:

```bash
sudo python3 ipe_rnp_topology.py
```

Após a execução, o Mininet cria a topologia e conecta os switches ao ONOS.

---

## Testes Realizados
🔹 Teste de Latência (Ping)

Entre dois hosts:
```bash
h_bv ping -c 1 h_for
```

🔹 Teste de Conectividade Global
```bash
pingall
```

Resultado esperado:
```bash
0% dropped
```

🔹 Teste de Vazão (Iperf)

Servidor:
```bash
h_bv iperf -s &
```

Cliente:
```bash
h_for iperf -c 10.0.0.1
```

O resultado apresenta a taxa de transmissão efetiva entre os hosts, validando a limitação de banda configurada nos enlaces.  

---

## Monitoramento no ONOS

O monitoramento da rede é realizado pela interface gráfica do ONOS:  

- Topology View: visualização de switches, links e hosts

- Devices → Port View: contadores de pacotes e bytes por porta

- Devices → Flow View: estatísticas dos flows OpenFlow instalados  

Esses dados permitem analisar o tráfego em cada switch e verificar o comportamento dinâmico do controlador SDN.  

---

## Demonstração em Vídeo

A demonstração prática da topologia, testes de comunicação e monitoramento no ONOS está disponível no link abaixo:

[Link para video com Monitoramento no ONOS](https://drive.google.com/file/d/1XWQn17K8ranDAX6cTRJ8urOyl-1G-ANn/view)


---

## Autor

**Paulo Henrique**  
Graduação em Ciência da Computação – UECE
Disciplina: Redes de Computadores
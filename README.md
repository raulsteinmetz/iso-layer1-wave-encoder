# Wave Encoder

### Esse código roda uma interface em python, que faz codificações de sequencias de bits em ondas, com métodos de comunicação de dados

## Como rodar

### Dependências
!sudo apt install python3 

!sudo apt-get install python-pip

%pip3 install numpy

%pip3 install matplotlib

%pip3 install pygame

### Código principal
!python3 main.py

## Tipos de Codificação de Ondas implementadas

### NRZ-L
O nível da voltagem representa o valor do bit, um nível é selecionado para representar bits zero, enquanto outro é selecionado para representar bits 1

![image](https://user-images.githubusercontent.com/85199336/234344464-5ee74aa7-fc6d-4d9f-a8c2-4bcf2da693eb.png)

### NRZ-I
O nível da voltagem muda para representar um bit 1 e permanece o mesmo para representar um bit 0

![image](https://user-images.githubusercontent.com/85199336/234344818-84350f7b-11e0-4502-bdfa-d3532ca97f03.png)

### AMI
Bit 0 é representado por 0, enquanto um bit 1 é representado por um nível de tensão positivo ou negativo alternado

![image](https://user-images.githubusercontent.com/85199336/234345007-9d206552-6bdf-4bc7-b09f-5686ae6ea6b8.png)

### PSEUDOTERNARIO
Bit 1 é representado por 0, enquanto um bit 0 é representado por um nível de tensão positivo ou negativo alternado
![image](https://user-images.githubusercontent.com/85199336/234347078-691b00a8-e4ba-46b6-a43f-b969cadad13b.png)


### MANCHESTER
Duracao de um bit é dividida pela metade, na primeira metade o bit permanece em um nivel, depois desloca-se, bit 0 é representado por uma transição de descida na voltagem, enquanto um bit 1
é representado por uma subida na voltagem

![image](https://user-images.githubusercontent.com/85199336/234347672-eef4b586-1ce1-4c8c-844b-0ea19907737b.png)

### MANCHESTER DIFERENCIAL
Existe sempre uma transição no meio do elemento, mas o valor é determinado no início. Se for 0, começa diferente da última voltagem e termina numa voltagem igual,
enquanto o bit 1 começa na última voltagem e termina numa voltagem diferente

![image](https://user-images.githubusercontent.com/85199336/234345807-667c6a47-4317-4056-b91e-3309ff563d46.png)

### MLT3
MLT-3 (Modified Lullabye Transmission Level 3) é uma técnica de codificação de linha usada em sistemas de telecomunicações para transmitir sinais digitais por meio 
de um meio físico, como um fio de cobre. Na codificação MLT-3, cada bit é representado por um sinal de três níveis. Os três níveis de sinal são tipicamente -1, 0 e +1. 
A lógica de codificação de MLT-3 é baseada no princípio de reduzir o número de zeros consecutivos no sinal transmitido. Isso ocorre porque sequências longas de zeros 
podem causar erros de sincronização e de temporização no receptor. Em MLT-3, um bit "0" é representado pela ausência de mudança no nível do sinal (ou seja, o sinal 
permanece no seu nível atual). Um bit "1" é representado por uma transição para o próximo nível de sinal. No entanto, em vez de transitar para o nível mais alto ou mais 
baixo do sinal, como em outras técnicas de codificação de linha, MLT-3 transita para o nível médio do sinal. Por exemplo, se o nível atual do sinal for 0 e o próximo bit 
a ser transmitido for um "1", o nível do sinal fará uma transição para +1. Se o próximo bit a ser transmitido for um "0", o nível do sinal permanecerá em +1. Se o próximo 
bit também for um "0", o nível do sinal fará uma transição para 0 (ou seja, o nível médio do sinal). O uso do nível médio do sinal para bits "1" reduz o número de zeros 
consecutivos no sinal transmitido, o que melhora a sincronização e a temporização no receptor. Além disso, a codificação MLT-3 tem um componente DC (corrente contínua) 
menor do que outras técnicas de codificação de linha, o que reduz o consumo de energia e a interferência eletromagnética. No entanto, a codificação MLT-3 tem uma taxa de 
dados menor do que outras técnicas que usam mais níveis de sinal, como a codificação 4B/5B.

![image](https://user-images.githubusercontent.com/85199336/234346512-e9b673e5-4565-443c-a63f-61ea6dfbabf9.png)


### DIFFERENTIAL BINARY
Nessa técnica, cada bit é codificado como a diferença entre o nível de sinal atual e o nível de sinal anterior. Um bit "1" é representado por uma diferença positiva, enquanto um bit "0" é representado por uma diferença negativa.

![image](https://user-images.githubusercontent.com/85199336/234346185-4033c1d2-09fe-44df-a691-9bcd5bfff1d3.png)


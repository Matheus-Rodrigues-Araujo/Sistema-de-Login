#The creation of the database 'usuarios'
create database usuarios

# A criação da tabela 'informacoes'
# The creation of the table 'informacoes'
CREATE TABLE `informacoes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(30) DEFAULT NULL,
  `nascimento` date NOT NULL,
  `cpf` varchar(11) NOT NULL,
  `email` varchar(40) NOT NULL,
  `senha` varchar(20) NOT NULL,
  `viagem` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `cpf` (`cpf`),
  KEY `viagem` (`viagem`),
  CONSTRAINT `informacoes_ibfk_1` FOREIGN KEY (`viagem`) REFERENCES `viagens` (`id_viagem`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

# Ignore a coluna viagem, não estou o utilizando nesse código
# Ignore the 'viagem' column, I'm not using it in this code
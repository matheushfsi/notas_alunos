CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(50) NOT NULL,
    senha VARCHAR(50) NOT NULL,
    nome VARCHAR(100) NOT NULL
);

CREATE TABLE notas_alunos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    materia VARCHAR(100) NOT NULL,
    nota DECIMAL(4,2) NOT NULL,
    faltas INT NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

INSERT INTO usuarios (usuario, senha, nome)
VALUES (
    'matheus',
    '123',
    'Matheus Henrique Ferreira da Silva'
);

INSERT INTO notas_alunos (usuario_id, materia, nota, faltas)
VALUES
(1, 'Matematica', 8.5, 2),
(1, 'Portugues', 7.8, 1),
(1, 'Historia', 9.2, 0),
(1, 'Geografia', 8.0, 1),
(1, 'Biologia', 8.7, 2),
(1, 'Quimica', 7.5, 3),
(1, 'Fisica', 8.1, 2),
(1, 'Ingles', 9.0, 0),
(1, 'Educacao Fisica', 10.0, 0),
(1, 'Filosofia', 8.4, 1),
(1, 'Sociologia', 8.8, 0),
(1, 'Informatica', 9.7, 0);
--
-- Скрипт сгенерирован Devart dbForge Studio 2020 for MySQL, Версия 9.0.567.0
-- Домашняя страница продукта: http://www.devart.com/ru/dbforge/mysql/studio
-- Дата скрипта: 19.06.2024 3:47:16
-- Версия сервера: 5.7.11
-- Версия клиента: 4.1
--

-- 
-- Отключение внешних ключей
-- 
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;

-- 
-- Установить режим SQL (SQL mode)
-- 
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- 
-- Установка кодировки, с использованием которой клиент будет посылать запросы на сервер
--
SET NAMES 'utf8';

--
-- Установка базы данных по умолчанию
--
USE `09.03.04.database`;

--
-- Удалить представление `descipline_competence_view`
--
DROP VIEW IF EXISTS descipline_competence_view CASCADE;

--
-- Удалить представление `discipline_competence_view`
--
DROP VIEW IF EXISTS discipline_competence_view CASCADE;

--
-- Удалить таблицу `desciplinecompetence`
--
DROP TABLE IF EXISTS desciplinecompetence;

--
-- Удалить таблицу `competence`
--
DROP TABLE IF EXISTS competence;

--
-- Удалить представление `result_view`
--
DROP VIEW IF EXISTS result_view CASCADE;

--
-- Удалить таблицу `result`
--
DROP TABLE IF EXISTS result;

--
-- Удалить представление `syllibusdiscipline_view`
--
DROP VIEW IF EXISTS syllibusdiscipline_view CASCADE;

--
-- Удалить таблицу `syllibusdiscipline`
--
DROP TABLE IF EXISTS syllibusdiscipline;

--
-- Удалить таблицу `discipline`
--
DROP TABLE IF EXISTS discipline;

--
-- Удалить представление `edicational_program_view`
--
DROP VIEW IF EXISTS edicational_program_view CASCADE;

--
-- Удалить таблицу `edicational_program`
--
DROP TABLE IF EXISTS edicational_program;

--
-- Удалить таблицу `edicational_standart`
--
DROP TABLE IF EXISTS edicational_standart;

--
-- Установка базы данных по умолчанию
--
USE `09.03.04.database`;

--
-- Создать таблицу `edicational_standart`
--
CREATE TABLE edicational_standart (
  IDEdSt int(11) NOT NULL AUTO_INCREMENT,
  Specialization_code varchar(100) DEFAULT NULL,
  Name varchar(255) DEFAULT NULL,
  Time varchar(255) DEFAULT NULL,
  PRIMARY KEY (IDEdSt),
  UNIQUE INDEX UK_edicational_standart_IDEdSt (IDEdSt)
)
ENGINE = INNODB,
AUTO_INCREMENT = 40,
CHARACTER SET utf8mb4,
COLLATE utf8mb4_general_ci;

--
-- Создать индекс `UK_edicational_standart` для объекта типа таблица `edicational_standart`
--
ALTER TABLE edicational_standart
ADD UNIQUE INDEX UK_edicational_standart (Specialization_code, Name, Time);

--
-- Создать таблицу `edicational_program`
--
CREATE TABLE edicational_program (
  IDEdPr int(11) NOT NULL AUTO_INCREMENT,
  IDEdSt int(11) DEFAULT NULL,
  Profile varchar(255) DEFAULT NULL,
  Year int(11) NOT NULL,
  PRIMARY KEY (IDEdPr),
  UNIQUE INDEX UK_edicational_program_IDEdPr (IDEdPr)
)
ENGINE = INNODB,
AUTO_INCREMENT = 60,
AVG_ROW_LENGTH = 8192,
CHARACTER SET utf8mb4,
COLLATE utf8mb4_general_ci;

--
-- Создать индекс `UK_edicational_program` для объекта типа таблица `edicational_program`
--
ALTER TABLE edicational_program
ADD UNIQUE INDEX UK_edicational_program (Profile, Year);

--
-- Создать внешний ключ
--
ALTER TABLE edicational_program
ADD CONSTRAINT FK_edicational_program_IDEdSt FOREIGN KEY (IDEdSt)
REFERENCES edicational_standart (IDEdSt) ON DELETE NO ACTION;

--
-- Создать представление `edicational_program_view`
--
CREATE
DEFINER = 'root'@'localhost'
VIEW edicational_program_view
AS
SELECT
  `edicational_standart`.`IDEdSt` AS `IDEdSt`,
  `edicational_program`.`IDEdPr` AS `IDEdPr`,
  `edicational_standart`.`Name` AS `NameS`,
  `edicational_program`.`Profile` AS `Profile`,
  `edicational_program`.`Year` AS `Year`
FROM (`edicational_program`
  JOIN `edicational_standart`
    ON ((`edicational_program`.`IDEdSt` = `edicational_standart`.`IDEdSt`)));

--
-- Создать таблицу `discipline`
--
CREATE TABLE discipline (
  IDD int(11) NOT NULL AUTO_INCREMENT,
  Name varchar(255) DEFAULT NULL,
  QuantityAcademicHour int(11) DEFAULT NULL,
  Description text DEFAULT NULL,
  Object varchar(255) DEFAULT NULL,
  PRIMARY KEY (IDD),
  UNIQUE INDEX UK_discipline_IDD (IDD)
)
ENGINE = INNODB,
AUTO_INCREMENT = 208,
AVG_ROW_LENGTH = 3276,
CHARACTER SET utf8mb4,
COLLATE utf8mb4_general_ci;

--
-- Создать индекс `UK_discipline` для объекта типа таблица `discipline`
--
ALTER TABLE discipline
ADD UNIQUE INDEX UK_discipline (Name, QuantityAcademicHour);

--
-- Создать таблицу `syllibusdiscipline`
--
CREATE TABLE syllibusdiscipline (
  ID int(11) NOT NULL AUTO_INCREMENT,
  IDEdPr int(11) DEFAULT NULL,
  IDD int(11) DEFAULT NULL,
  Semesters varchar(255) DEFAULT NULL,
  PRIMARY KEY (ID),
  UNIQUE INDEX UK_syllibusdiscipline_ID (ID)
)
ENGINE = INNODB,
AUTO_INCREMENT = 161,
AVG_ROW_LENGTH = 3276,
CHARACTER SET utf8mb4,
COLLATE utf8mb4_general_ci;

--
-- Создать индекс `UK_syllibusdiscipline` для объекта типа таблица `syllibusdiscipline`
--
ALTER TABLE syllibusdiscipline
ADD UNIQUE INDEX UK_syllibusdiscipline (IDEdPr, IDD);

--
-- Создать внешний ключ
--
ALTER TABLE syllibusdiscipline
ADD CONSTRAINT FK_syllibusdiscipline_IDD FOREIGN KEY (IDD)
REFERENCES discipline (IDD) ON DELETE NO ACTION;

--
-- Создать внешний ключ
--
ALTER TABLE syllibusdiscipline
ADD CONSTRAINT FK_syllibusdiscipline_IDEdPr FOREIGN KEY (IDEdPr)
REFERENCES edicational_program (IDEdPr) ON DELETE NO ACTION;

--
-- Создать представление `syllibusdiscipline_view`
--
CREATE
DEFINER = 'root'@'localhost'
VIEW syllibusdiscipline_view
AS
SELECT
  `syllibusdiscipline`.`ID` AS `ID`,
  `syllibusdiscipline`.`IDEdPr` AS `IDEdPr`,
  `syllibusdiscipline`.`IDD` AS `IDD`,
  `edicational_program`.`Profile` AS `Profile`,
  `edicational_program`.`Year` AS `Year`,
  `discipline`.`Name` AS `Name_d`,
  `syllibusdiscipline`.`Semesters` AS `Semesters`
FROM ((`syllibusdiscipline`
  JOIN `discipline`
    ON ((`syllibusdiscipline`.`IDD` = `discipline`.`IDD`)))
  JOIN `edicational_program`
    ON ((`syllibusdiscipline`.`IDEdPr` = `edicational_program`.`IDEdPr`)))
ORDER BY `syllibusdiscipline`.`IDEdPr`;

--
-- Создать таблицу `result`
--
CREATE TABLE result (
  IDResult int(11) NOT NULL AUTO_INCREMENT,
  IDD1 int(11) DEFAULT NULL,
  IDD2 int(11) DEFAULT NULL,
  Relations tinyint(1) DEFAULT 0,
  DescriptionR text DEFAULT NULL,
  PRIMARY KEY (IDResult),
  UNIQUE INDEX UK_result_IDResult (IDResult)
)
ENGINE = INNODB,
AUTO_INCREMENT = 320,
AVG_ROW_LENGTH = 1638,
CHARACTER SET utf8mb4,
COLLATE utf8mb4_general_ci;

--
-- Создать индекс `UK_result` для объекта типа таблица `result`
--
ALTER TABLE result
ADD UNIQUE INDEX UK_result (IDD1, IDD2);

--
-- Создать внешний ключ
--
ALTER TABLE result
ADD CONSTRAINT FK_result_IDD1 FOREIGN KEY (IDD1)
REFERENCES syllibusdiscipline (ID) ON DELETE NO ACTION;

--
-- Создать внешний ключ
--
ALTER TABLE result
ADD CONSTRAINT FK_result_IDD2 FOREIGN KEY (IDD2)
REFERENCES syllibusdiscipline (ID) ON DELETE NO ACTION;

--
-- Создать представление `result_view`
--
CREATE
DEFINER = 'root'@'localhost'
VIEW result_view
AS
SELECT
  `result`.`IDResult` AS `IDResult`,
  `result`.`IDD1` AS `IDD1`,
  `result`.`IDD2` AS `IDD2`,
  `discipline`.`Name` AS `Name1`,
  `discipline`.`Object` AS `Object1`,
  `discipline_1`.`Name` AS `Name2`,
  `discipline_1`.`Object` AS `Object2`,
  `result`.`Relations` AS `Relations`,
  `result`.`DescriptionR` AS `DescriptionR`,
  `edicational_program`.`Profile` AS `Profile`,
  `edicational_program`.`Year` AS `Year`,
  `discipline_1`.`Description` AS `Desc1`,
  `discipline`.`Description` AS `Desc2`
FROM (((((`result`
  JOIN `syllibusdiscipline`
    ON ((`result`.`IDD1` = `syllibusdiscipline`.`ID`)))
  JOIN `discipline`
    ON ((`syllibusdiscipline`.`IDD` = `discipline`.`IDD`)))
  JOIN `syllibusdiscipline` `syllibusdiscipline_1`
    ON ((`result`.`IDD2` = `syllibusdiscipline_1`.`ID`)))
  JOIN `discipline` `discipline_1`
    ON ((`syllibusdiscipline_1`.`IDD` = `discipline_1`.`IDD`)))
  JOIN `edicational_program`
    ON (((`syllibusdiscipline`.`IDEdPr` = `edicational_program`.`IDEdPr`)
    AND (`syllibusdiscipline_1`.`IDEdPr` = `edicational_program`.`IDEdPr`))));

--
-- Создать таблицу `competence`
--
CREATE TABLE competence (
  IDC int(11) NOT NULL AUTO_INCREMENT,
  Name varchar(255) DEFAULT NULL,
  Description text DEFAULT NULL,
  Type varchar(255) DEFAULT NULL,
  PRIMARY KEY (IDC),
  UNIQUE INDEX UK_competence_IDC (IDC)
)
ENGINE = INNODB,
AUTO_INCREMENT = 219,
AVG_ROW_LENGTH = 1820,
CHARACTER SET utf8mb4,
COLLATE utf8mb4_general_ci;

--
-- Создать индекс `UK_competence_Name` для объекта типа таблица `competence`
--
ALTER TABLE competence
ADD UNIQUE INDEX UK_competence_Name (Name);

--
-- Создать таблицу `desciplinecompetence`
--
CREATE TABLE desciplinecompetence (
  ID int(11) NOT NULL AUTO_INCREMENT,
  IDC int(11) DEFAULT NULL,
  IDD int(11) DEFAULT NULL,
  PRIMARY KEY (ID),
  UNIQUE INDEX UK_desciplinecompetence_ID (ID)
)
ENGINE = INNODB,
AUTO_INCREMENT = 128,
AVG_ROW_LENGTH = 2340,
CHARACTER SET utf8mb4,
COLLATE utf8mb4_general_ci;

--
-- Создать индекс `UK_desciplinecompetence` для объекта типа таблица `desciplinecompetence`
--
ALTER TABLE desciplinecompetence
ADD UNIQUE INDEX UK_desciplinecompetence (IDC, IDD);

--
-- Создать внешний ключ
--
ALTER TABLE desciplinecompetence
ADD CONSTRAINT FK_desciplinecompetence_IDC FOREIGN KEY (IDC)
REFERENCES competence (IDC) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Создать внешний ключ
--
ALTER TABLE desciplinecompetence
ADD CONSTRAINT FK_desciplinecompetence_IDD FOREIGN KEY (IDD)
REFERENCES discipline (IDD) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Создать представление `discipline_competence_view`
--
CREATE
DEFINER = 'root'@'localhost'
VIEW discipline_competence_view
AS
SELECT
  `desciplinecompetence`.`IDD` AS `IDD`,
  GROUP_CONCAT(`competence`.`IDC` SEPARATOR ',') AS `IDC`,
  MAX(`discipline`.`Name`) AS `Name_discipline`,
  GROUP_CONCAT(`competence`.`Name` SEPARATOR ',') AS `Name_competence`,
  `edicational_program`.`Profile` AS `Profile`,
  `edicational_program`.`Year` AS `Year`
FROM ((((`desciplinecompetence`
  JOIN `discipline`
    ON ((`desciplinecompetence`.`IDD` = `discipline`.`IDD`)))
  JOIN `competence`
    ON ((`desciplinecompetence`.`IDC` = `competence`.`IDC`)))
  JOIN `syllibusdiscipline`
    ON ((`syllibusdiscipline`.`IDD` = `discipline`.`IDD`)))
  JOIN `edicational_program`
    ON ((`syllibusdiscipline`.`IDEdPr` = `edicational_program`.`IDEdPr`)))
GROUP BY `desciplinecompetence`.`IDD`,
         `desciplinecompetence`.`IDC`,
         `competence`.`Name`,
         `edicational_program`.`Profile`,
         `edicational_program`.`Year`
ORDER BY `desciplinecompetence`.`IDD`;

--
-- Создать представление `descipline_competence_view`
--
CREATE
DEFINER = 'root'@'localhost'
VIEW descipline_competence_view
AS
SELECT
  `desciplinecompetence`.`ID` AS `ID`,
  `discipline`.`IDD` AS `IDD`,
  `competence`.`IDC` AS `IDC`,
  `discipline`.`Name` AS `Named`,
  `competence`.`Name` AS `Namec`
FROM ((`desciplinecompetence`
  JOIN `competence`
    ON ((`desciplinecompetence`.`IDC` = `competence`.`IDC`)))
  JOIN `discipline`
    ON ((`desciplinecompetence`.`IDD` = `discipline`.`IDD`)))
GROUP BY `desciplinecompetence`.`ID`,
         `competence`.`IDC`,
         `competence`.`Name`,
         `discipline`.`Name`,
         `discipline`.`IDD`
ORDER BY `discipline`.`IDD`;

-- 
-- Вывод данных для таблицы edicational_standart
--
INSERT INTO edicational_standart VALUES
(39, '09.03.04', 'Программная инженерия', 'бакалавриат');

-- 
-- Вывод данных для таблицы edicational_program
--
INSERT INTO edicational_program VALUES
(59, 39, 'Разработка и сопровождение информационных систем и web-приложений', 2019);

-- 
-- Вывод данных для таблицы discipline
--
INSERT INTO discipline VALUES
(203, 'иностранный язык', 252, 'Раздел 1. NICE TO MEET YOU. Hello, people of the world! We are family Everyday life Раздел 2. EDUCATION FOR LIFE The world of work My studying routine Higher education in the world Раздел 3. LEISURE TIME Hobbies Sports and games Sightseeing Раздел 4. AROUND THE WORLD My home time Russia my homeland Countries and their traditions Раздел 5. AUTOMATION AND ROBOTICS Automation Tipes of automation Robots in industry Раздел 6. COMPUTERS History of computers What is a computer? Functional organization of the computer Раздел 7. MODERN COMPUTER TECHNOLOGIES Information technology’s role today Operating systems Operational  system Windows Раздел 8. COMPUTER PROGRAMMING Programming languages Computer program The world wide web Раздел 9 TECHNOLOGICAL AND SCIENTIFIC ACHIEVEMENTS Great people who have changed the world Ecological problems Environmentally-friendly society Промежуточная аттестация', 'Гуманитарная'),
(204, 'алгебра и аналитическая геометрия', 144, 'Раздел 1. АЛГЕБРА МАТРИЦ. СИСТЕМЫ ЛИНЕЙНЫХ УРАВНЕНИЙ Матрицы, определители. Общая теория систем линейных уравнений. Раздел 2. ВЕКТОРНАЯ АЛГЕБРА И АНАЛИТИЧЕСКАЯ ГЕОМЕТРИЯ Пространство геометрических векторов. Операции над векторами. Приложения Предмет и метод аналитической геометрии. Прямая на плоскости, прямая и плоскость в пространстве. Кривые второго порядка. Общее и канонические уравнения. Преобразование координат, упрощение общего уравнения кривой. Поверхности в пространстве. Поверхности второго порядка. Раздел 3.АЛГЕБРА КОМПЛЕКСНЫХ ЧИСЕЛ И МНОГОЧЛЕНОВ Множество комплексных чисел. Многочлены и их корни. Рациональные дроби. Промежуточная аттестация', 'Техническая'),
(205, 'математический анализ', 360, 'Раздел 1. ВВЕДЕНИЕ В МАТЕАТИЧЕСКИЙ АНАЛИЗ Введение. Множество действительных чисел. Функция одной переменной, свойства, графики. Элементарные функции. Предел и непрерывность функции одной переменной. Раздел 2. ДИФФЕРЕНЦИАЛЬНОЕ ИСЧИСЛЕНИЕ ФУНКЦИИ ОЛНОЙ И НЕСКОЛЬКИХ ПЕРЕМЕННЫХ Производная и дифференциал функции одной переменной, их приложения. Функции нескольких переменных, частные производные и дифференциалы, полный дифференциал, их приложения. Экстремумы функции нескольких переменных. Раздел 3. ИНТЕГРАЛЬНОЕ ИСЧИСЛЕНИЕ ФУНКЦИИ ОДОЙ ПЕРЕМЕННОЙ Первообразная. Неопределенный интеграл, его свойства. Основные методы интегрирования. Определенный интеграл, его вычисление и приложения. Раздел 4. ИНТЕГРАЛЬНОЕ ИСЧИСЛЕНИЕ ФУНКЦИИ НЕСКОЛЬКИХ ПЕРЕМЕННЫХ. ЭЛЕМЕНТЫ ТЕОРИИ ПОЛЯ Кратные и криволинейные интегралы Элементы векторного анализа Раздел 5. ДИФФЕРЕНЦИАЛЬНЫЕ УРАВНЕНИЯ, СИСТЕМЫ ДИФФЕРЕНЦИАЛЬНЫХ УРАВНЕНИЙ. ЭЛЕМЕНТЫ ТЕОРИИ УСТОЙЧИВОСТИ. Дифференциальные уравнения. Обыкновенные дифференциальные уравнения первого порядка Дифференциальные уравнения высших порядков.\nОбщая теория линейных дифференциальных уравнений. Системы дифференциальных уравнений.\nТеория интегрирования линейны систем   дифференциальных уравнений Операционное исчисление. \nЭлементы теории устойчивости Раздел 6. РЯДЫ. ЧИСЛОВЫЕ РЯДЫ, СТЕПЕННЫЕ РЯДЫ И РЯДЫ ТЕЙЛОРА. РАЗЛОЖЕНИЕ ФУНКЦИИ В СТЕПЕННОЙ РЯД. Числовой ряд, сходимость и сумма ряда. Признаки сходимости Степенные ряды. Ряд Тейлора, разложение функции в степенной ряд. Промежуточная аттестация', 'Техническая'),
(206, 'инженерная и компьютерная графика', 144, 'Раздел 1.  ИЗОБРАЖЕНИЕ ПРЕДМЕТОВ Единая система конструкторской документации Виды, разрезы, сечения Аксонометрические проекции Раздел 2. СОЕДИНЕНИЯ ДЕТАЛЕЙ Трехмерное моделирование Классификация соединений Изображение и обозначение резьбы Раздел 3. ИЗОБРАЖЕНИЕ ИЗДЕЛИЙ Эскизы деталей Сборочные чертежи Чтение и деталирование сборочных чертежей Промежуточная аттестация', 'Гуманитарная'),
(207, 'история (история россии, всеобщая история)', 108, 'Раздел 1. ДРЕВНЯЯ И СРЕДНЕВЕКОВАЯ РУСЬ В ОБЩЕМИРОВОМ ПРОЦЕССЕ История как наука. Раннефеодальная монархия Киевская Русь. Удельный период. Агрессия «Востока» и «Запада» Московская Русь: основные тенденции развития и проблема самоидентификации Раздел 2. РОССИЙСКАЯ ИМПЕРИЯ: РЕФОРМЫ И РЕВОЛЮЦИИ Становление Российской империи Превращение России в монархию буржуазного типа Мир в начале ХХ в.: от империи – к советскому государству Раздел 3. СОВЕТСКИЙ И ПОСТСОВЕТСКИЙ ПЕРИОДЫ ОТЕЧЕСТВЕННОЙ ИСТОРИИ Формирование основ Советского государства. Первые пятилетки. Вторая мировая война и Великая Отечественная война Мир и СССР после войны. От СССР – к современной России Промежуточная аттестация', 'Гуманитарная');

-- 
-- Вывод данных для таблицы syllibusdiscipline
--
INSERT INTO syllibusdiscipline VALUES
(156, 59, 203, '1'),
(157, 59, 204, '1'),
(158, 59, 205, '1'),
(159, 59, 206, '1'),
(160, 59, 207, '2');

-- 
-- Вывод данных для таблицы competence
--
INSERT INTO competence VALUES
(168, 'УК-4', 'Способен осуществлять деловую коммуникацию в устной и письменной формах на государственном языке Российской Федерации и иностранном(ых) \nязыке(ах)', 'УК'),
(169, 'ОПК-1', 'ОПК-1. Способен применять естественнонаучные и общеинженерные знания, методы математического анализа и моделирования, теоретического и экспериментального исследования в профессиональной деятельности.', 'ОПК'),
(170, 'УК-1', 'УК-1Способен осуществлять поиск, критический анализ и синтез информации, применять системный подход для решения поставленных задач.', 'УК'),
(173, 'ОПК-2', 'Способен Использовать современные информационные технологии и программные средства, в том числе\nотечественного производства, при решении задач профессиональной деятельности.', 'ОПК'),
(174, 'УК-5', 'Способенвоспринимать межкультурное разнообразие общества в социально-историческом, этическом ифилософском контекстах', 'УК'),
(186, 'ПК-9', '', 'ПК'),
(187, 'ПК-7', 'Способен применять навыки моделирования, анализа и использования формальных методов конструирования программного обеспечения', 'ПК'),
(188, 'ПК-8', 'Способен создавать программные интерфейсы', 'ПК'),
(191, 'ОПК-5', 'Способен инсталлировать программное и аппаратное обеспечение для информационных и автоматизированных систем', 'ОПК'),
(197, 'ОПК-6', 'Способен разрабатывать алгоритмы и программы, пригодные для практического использования, применять основы информатики и программирования к проектированию, конструированию и тестированию программных продуктов', 'ОПК'),
(218, 'УК-2', 'Способен определять круг задач в рамках поставленной цели и выбирать оптимальные способы их решения, исходя из действующих правовых норм, имеющихся ресурсов и ограничений', 'УК');

-- 
-- Вывод данных для таблицы result
--
INSERT INTO result VALUES
(310, 156, 157, 0, '0.11620904'),
(311, 156, 158, 0, '-0.10912946'),
(312, 156, 159, 1, '0.6667398'),
(313, 156, 160, 1, '0.45574212'),
(314, 157, 158, 0, '-0.22060098'),
(315, 157, 159, 0, '0.35490307'),
(316, 157, 160, 0, '0.41999123'),
(317, 158, 159, 0, '0.06395119'),
(318, 158, 160, 0, '-0.2917198'),
(319, 159, 160, 0, '0.33594245');

-- 
-- Вывод данных для таблицы desciplinecompetence
--
INSERT INTO desciplinecompetence VALUES
(121, 168, 203),
(122, 169, 204),
(125, 169, 205),
(123, 170, 204),
(124, 170, 205),
(126, 173, 206),
(127, 174, 207);

--
-- Установка базы данных по умолчанию
--
USE `09.03.04.database`;

--
-- Удалить триггер `trigger1`
--
DROP TRIGGER IF EXISTS trigger1;

--
-- Установка базы данных по умолчанию
--
USE `09.03.04.database`;

DELIMITER $$

--
-- Создать триггер `trigger1`
--
CREATE
DEFINER = 'root'@'localhost'
TRIGGER trigger1
BEFORE INSERT
ON result
FOR EACH ROW
BEGIN
  IF EXISTS (SELECT
        1
      FROM result
      WHERE (IDD1 = NEW.IDD1
      AND IDD2 = NEW.IDD2)
      OR (IDD1 = NEW.IDD2
      AND IDD2 = NEW.IDD1)
      OR (NEW.IDD1 = NEW.IDD2)) THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Duplicate pair of IDD1 and IDD2';
  END IF;
END
$$

DELIMITER ;

-- 
-- Восстановить предыдущий режим SQL (SQL mode)
--
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;

-- 
-- Включение внешних ключей
-- 
/*!40014 SET FOREIGN_KEY_CHECKS = @OLD_FOREIGN_KEY_CHECKS */;
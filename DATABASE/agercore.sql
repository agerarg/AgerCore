-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 03-08-2023 a las 15:11:06
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `agercore`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `area`
--

CREATE TABLE `area` (
  `id` int(11) NOT NULL,
  `name` varchar(40) NOT NULL,
  `level` int(11) NOT NULL,
  `areaType` varchar(20) NOT NULL DEFAULT 'field'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `area`
--

INSERT INTO `area` (`id`, `name`, `level`, `areaType`) VALUES
(1, 'startcity', 1, 'town'),
(2, 'startarea', 1, 'field');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `characters`
--

CREATE TABLE IF NOT EXISTS `characters` (
	`char_id` INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
	`account_id` INT(11) UNSIGNED NOT NULL DEFAULT '0',
	`char_num` TINYINT(1) NOT NULL DEFAULT '0',
	`name` VARCHAR(50) NOT NULL COLLATE 'utf8_general_ci',
	`class_id` INT(11) NOT NULL,
	`level` SMALLINT(6) UNSIGNED NOT NULL DEFAULT '1',
	`exp` BIGINT(20) UNSIGNED NOT NULL DEFAULT '0',
	`expLimit` BIGINT(20) NOT NULL,
	`last_map` INT(12) NOT NULL DEFAULT '5',
	`last_x` FLOAT NOT NULL,
	`last_y` FLOAT NOT NULL,
	`online` TINYINT(2) NOT NULL DEFAULT '0',
	`sex` ENUM('M','F') NOT NULL COLLATE 'utf8_general_ci',
	PRIMARY KEY (`char_id`) USING BTREE,
	UNIQUE INDEX `name` (`name`) USING BTREE,
	INDEX `account_id` (`account_id`) USING BTREE
)
ENGINE=InnoDB AUTO_INCREMENT=150000;
--
-- Volcado de datos para la tabla `characters`
--

INSERT INTO `characters` (`account_id`, `char_id`, `char_num`, `name`, `class_id`, `level`, `exp`, `expLimit`, `last_map`, `last_x`, `last_y`, `online`, `sex`) VALUES
(2000000, 150000, 0, 'Warrior', 3, 5, 0, 5, 1, 0, 0, 0, 'M'),
(2000000, 150001, 0, 'Baba', 1, 7, 1, 5, 1, 0, 0, 0, 'M'),
(2000001, 150002, 0, 'test character', 2, 3, 0, 5, 1, 0, 0, 0, 'M'),
(2000002, 150003, 0, 'Pepito', 3, 1, 0, 5, 1, 0, 0, 0, 'M');


-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `class_db`
--

CREATE TABLE IF NOT EXISTS `class_db` (
  `class_id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `intelligence` int(11) NOT NULL,
  `dexterity` int(11) NOT NULL,
  `strength` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT  AUTO_INCREMENT=0;

--
-- Volcado de datos para la tabla `class_db`
--

INSERT INTO `class_db` (`id`, `name`, `intelligence`, `dexterity`, `strength`) VALUES
(0, 'warrior', 5, 10, 15),
(1, 'rogue', 10, 15, 5),
(2, 'mage', 15, 5, 10);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `login`
--

CREATE TABLE IF NOT EXISTS `login` (
  `account_id` int(11) unsigned NOT NULL auto_increment,
  `username` varchar(23) NOT NULL default '',
  `userpass` varchar(32) NOT NULL default '',
  `email` varchar(39) NOT NULL default '',
  `character_slots` tinyint(3) unsigned NOT NULL default '0',
) ENGINE=InnoDB AUTO_INCREMENT=2000000; 

--
-- Volcado de datos para la tabla `login`
--

INSERT INTO `login` (`account_id`, `username`, `userpass`, `email`, `character_slots`) VALUES
(2000000, 'test', '123456', '', 0),
(2000001, 'test2', '123456', 'test@mail.com', 0),
(2000002, 'test3', '123456', '', 0);

--
-- Ýndices para tablas volcadas
--

--
-- Indices de la tabla `area`
--
ALTER TABLE `area`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `characters`
--
ALTER TABLE `characters`
  ADD PRIMARY KEY (`id`),
  ADD KEY `account_id` (`account_id`);

--
-- Indices de la tabla `class_db`
--
ALTER TABLE `class_db`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `area`
--
ALTER TABLE `area`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `characters`
--
ALTER TABLE `characters`
  MODIFY `char_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `class_db`
--
ALTER TABLE `class_db`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `login`
--
ALTER TABLE `login`
  MODIFY `account_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

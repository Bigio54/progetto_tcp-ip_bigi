-- phpMyAdmin SQL Dump
-- version 4.6.6deb5ubuntu0.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Creato il: Nov 15, 2023 alle 09:42
-- Versione del server: 5.7.40-0ubuntu0.18.04.1
-- Versione PHP: 7.2.24-0ubuntu0.18.04.15

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `5BTepsit`
--

-- --------------------------------------------------------

--
-- Struttura della tabella `dipendenti_nicola_bigi`
--

CREATE TABLE `dipendenti_nicola_bigi` (
  `id` int(11) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `indirizzo` varchar(100) NOT NULL,
  `telefono` varchar(100) NOT NULL,
  `agente` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dump dei dati per la tabella `dipendenti_nicola_bigi`
--

INSERT INTO `dipendenti_nicola_bigi` (`id`, `nome`, `indirizzo`, `telefono`, `agente`) VALUES
(1, 'Nome1', 'Indirizzo1', 'Telefono1', 23),
(2, 'Nome2', 'Indirizzo2', 'Telefono2', 65),
(3, 'Nome3', 'Indirizzo3', 'Telefono3', 87),
(4, 'Nome4', 'Indirizzo4', 'Telefono4', 98),
(5, 'Nome5', 'Indirizzo5', 'Telefono5', 32),
(6, 'Nome6', 'Indirizzo6', 'Telefono6', 15),
(7, 'Nome7', 'Indirizzo7', 'Telefono7', 67),
(8, 'Nome8', 'Indirizzo8', 'Telefono8', 88),
(9, 'Nome9', 'Indirizzo9', 'Telefono9', 91),
(10, 'Nome10', 'Indirizzo10', 'Telefono10', 77);

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `dipendenti_nicola_bigi`
--
ALTER TABLE `dipendenti_nicola_bigi`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT per le tabelle scaricate
--

--
-- AUTO_INCREMENT per la tabella `dipendenti_nicola_bigi`
--
ALTER TABLE `dipendenti_nicola_bigi`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

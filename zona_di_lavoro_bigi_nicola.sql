-- phpMyAdmin SQL Dump
-- version 4.6.6deb5ubuntu0.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Creato il: Nov 15, 2023 alle 09:44
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
-- Struttura della tabella `zona_di_lavoro_bigi_nicola`
--

CREATE TABLE `zona_di_lavoro_bigi_nicola` (
  `id_zona` int(11) NOT NULL,
  `nome_zona` varchar(255) DEFAULT NULL,
  `numero_clienti` int(11) DEFAULT NULL,
  `cod_dipendenti` int(11) DEFAULT NULL,
  `settore` varchar(255) DEFAULT NULL,
  `citta` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dump dei dati per la tabella `zona_di_lavoro_bigi_nicola`
--

INSERT INTO `zona_di_lavoro_bigi_nicola` (`id_zona`, `nome_zona`, `numero_clienti`, `cod_dipendenti`, `settore`, `citta`) VALUES
(1, 'Zona A', 100, NULL, 'Tecnologia', 'Roma'),
(2, 'Zona B', 80, NULL, 'Vendite', 'Milano'),
(3, 'Zona C', 120, NULL, 'Finanza', 'Napoli'),
(4, 'Zona D', 90, NULL, 'Risorse Umane', 'Torino'),
(5, 'Zona E', 150, NULL, 'Tecnologia', 'Firenze'),
(6, 'Zona F', 70, NULL, 'Vendite', 'Bologna'),
(7, 'Zona G', 110, NULL, 'Logistica', 'Palermo'),
(8, 'Zona H', 60, NULL, 'Risorse Umane', 'Genova'),
(9, 'Zona I', 130, NULL, 'Vendite', 'Bari'),
(10, 'Zona J', 95, NULL, 'Finanza', 'Cagliari');

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `zona_di_lavoro_bigi_nicola`
--
ALTER TABLE `zona_di_lavoro_bigi_nicola`
  ADD PRIMARY KEY (`id_zona`);

--
-- AUTO_INCREMENT per le tabelle scaricate
--

--
-- AUTO_INCREMENT per la tabella `zona_di_lavoro_bigi_nicola`
--
ALTER TABLE `zona_di_lavoro_bigi_nicola`
  MODIFY `id_zona` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

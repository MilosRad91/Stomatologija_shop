-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 05, 2025 at 12:06 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `stomatologija_shop`
--

-- --------------------------------------------------------

--
-- Table structure for table `detalji_porudzbine`
--

CREATE TABLE `detalji_porudzbine` (
  `id` int(11) NOT NULL,
  `porudzbina_id` int(11) NOT NULL,
  `proizvod_id` int(11) NOT NULL,
  `kolicina` int(11) NOT NULL,
  `cena_proizvoda` decimal(10,0) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `korisnici`
--

CREATE TABLE `korisnici` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `godina_rodjenja` int(11) NOT NULL,
  `trenutno_stanje_novca` decimal(10,0) NOT NULL,
  `vrsta_korisnika_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `korisnici`
--

INSERT INTO `korisnici` (`id`, `username`, `password`, `email`, `godina_rodjenja`, `trenutno_stanje_novca`, `vrsta_korisnika_id`) VALUES
(1, 'lemi91', 'lemi123', 'mrmilebob@gmail.com', 1991, 0, 1),
(2, 'johny89', 'johny123', 'nikola.radovanovic@gmail.com', 1989, 16700, 2),
(3, 'mikica91', 'mikica123', 'mikica.dzanic@gmail.com', 1991, 13900, 3);

-- --------------------------------------------------------

--
-- Table structure for table `porudzbine`
--

CREATE TABLE `porudzbine` (
  `id` int(11) NOT NULL,
  `kupac_id` int(11) NOT NULL,
  `datum_porudzbine` datetime NOT NULL,
  `ukupna_cena` decimal(10,0) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `proizvodi`
--

CREATE TABLE `proizvodi` (
  `id` int(11) NOT NULL,
  `naziv` varchar(100) NOT NULL,
  `opis` varchar(240) NOT NULL,
  `cena` decimal(10,0) NOT NULL,
  `kolicina` int(11) NOT NULL,
  `prodavac_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `vrsta_korisnika`
--

CREATE TABLE `vrsta_korisnika` (
  `id` int(11) NOT NULL,
  `naziv` varchar(50) NOT NULL,
  `opis` varchar(240) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `vrsta_korisnika`
--

INSERT INTO `vrsta_korisnika` (`id`, `naziv`, `opis`) VALUES
(1, 'admin', 'Admin'),
(2, 'kupac', 'Kupac'),
(3, 'prodavac', 'Prodavac');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `detalji_porudzbine`
--
ALTER TABLE `detalji_porudzbine`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_porudzbina_id` (`porudzbina_id`),
  ADD KEY `fk_proizvod_id` (`proizvod_id`);

--
-- Indexes for table `korisnici`
--
ALTER TABLE `korisnici`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_vrsta_korisnika` (`vrsta_korisnika_id`);

--
-- Indexes for table `porudzbine`
--
ALTER TABLE `porudzbine`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_kupac_id` (`kupac_id`);

--
-- Indexes for table `proizvodi`
--
ALTER TABLE `proizvodi`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_prodavac_id` (`prodavac_id`);

--
-- Indexes for table `vrsta_korisnika`
--
ALTER TABLE `vrsta_korisnika`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `detalji_porudzbine`
--
ALTER TABLE `detalji_porudzbine`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `korisnici`
--
ALTER TABLE `korisnici`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `porudzbine`
--
ALTER TABLE `porudzbine`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `proizvodi`
--
ALTER TABLE `proizvodi`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `vrsta_korisnika`
--
ALTER TABLE `vrsta_korisnika`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `detalji_porudzbine`
--
ALTER TABLE `detalji_porudzbine`
  ADD CONSTRAINT `fk_porudzbina_id` FOREIGN KEY (`porudzbina_id`) REFERENCES `porudzbine` (`id`),
  ADD CONSTRAINT `fk_proizvod_id` FOREIGN KEY (`proizvod_id`) REFERENCES `proizvodi` (`id`);

--
-- Constraints for table `korisnici`
--
ALTER TABLE `korisnici`
  ADD CONSTRAINT `fk_vrsta_korisnika` FOREIGN KEY (`vrsta_korisnika_id`) REFERENCES `vrsta_korisnika` (`id`);

--
-- Constraints for table `porudzbine`
--
ALTER TABLE `porudzbine`
  ADD CONSTRAINT `fk_kupac_id` FOREIGN KEY (`kupac_id`) REFERENCES `korisnici` (`id`);

--
-- Constraints for table `proizvodi`
--
ALTER TABLE `proizvodi`
  ADD CONSTRAINT `fk_prodavac_id` FOREIGN KEY (`prodavac_id`) REFERENCES `korisnici` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

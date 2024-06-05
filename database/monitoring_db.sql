-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 21, 2024 at 09:25 AM
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
-- Database: `monitoring_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `class`
--

CREATE TABLE `class` (
  `id` int(11) NOT NULL,
  `subject` varchar(255) NOT NULL,
  `teacher` varchar(255) NOT NULL,
  `class_time` varchar(50) NOT NULL,
  `class_code` varchar(20) NOT NULL,
  `lesson` varchar(255) NOT NULL,
  `class_availability` enum('available','unavailable') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `class`
--

INSERT INTO `class` (`id`, `subject`, `teacher`, `class_time`, `class_code`, `lesson`, `class_availability`) VALUES
(1, 'Math', 'Adimar Paul Canghagas', '7:30-10:00 am', 'a1t46X', '2+2?', 'unavailable'),
(4, 'P.E', 'Nyko Lopez, PHP', '10:00-12:00', 'A1k5t', 'Activity 1. What is P.E?', 'available'),
(5, 'PYTHON ', 'Denz Manceras', '8:30-10:00 AM', 'IT 123', 'Create a crud system using python', 'available'),
(6, 'IT ELEC 1', ' Paul Sebando', '1:00-2:30', 'k18isT', 'programming', 'available'),
(7, 'English', 'Krizelle Subade', '8:30-9:30', 'ENG98o1', 'noun and pronoun', 'available'),
(8, 'IT ELEC 325', 'Ma\'am Estacio', '7:00-8:30', 'ELEC235', 'Security', 'available'),
(9, 'ACCOUNTING 111', 'Nikki Panto', '4:00-5:00', 'ACTGG111', 'Assets,Owner\'s Equity,Liabilities', 'available'),
(10, 'A.P', 'Hannah Gatinao', '10:00-11:00', 'AP457', 'Analyze the impact of the revolution on Philippine history.', 'unavailable');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `password`) VALUES
(1, 'hannah', 'hannah123');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `class`
--
ALTER TABLE `class`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `class`
--
ALTER TABLE `class`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 19, 2024 at 11:17 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 7.4.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bsc_martial`
--

-- --------------------------------------------------------

--
-- Table structure for table `arts`
--

CREATE TABLE `arts` (
  `artsid` int(50) NOT NULL,
  `artsname` varchar(50) NOT NULL,
  `description` text NOT NULL,
  `image` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `arts`
--

INSERT INTO `arts` (`artsid`, `artsname`, `description`, `image`) VALUES
(34, 'Karatte', 'sfsdg', 'img5.png'),
(35, 'kungfu', 'c', 'img3.png');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add arts', 7, 'add_arts'),
(26, 'Can change arts', 7, 'change_arts'),
(27, 'Can delete arts', 7, 'delete_arts'),
(28, 'Can view arts', 7, 'view_arts'),
(29, 'Can add auth group', 8, 'add_authgroup'),
(30, 'Can change auth group', 8, 'change_authgroup'),
(31, 'Can delete auth group', 8, 'delete_authgroup'),
(32, 'Can view auth group', 8, 'view_authgroup'),
(33, 'Can add auth group permissions', 9, 'add_authgrouppermissions'),
(34, 'Can change auth group permissions', 9, 'change_authgrouppermissions'),
(35, 'Can delete auth group permissions', 9, 'delete_authgrouppermissions'),
(36, 'Can view auth group permissions', 9, 'view_authgrouppermissions'),
(37, 'Can add auth permission', 10, 'add_authpermission'),
(38, 'Can change auth permission', 10, 'change_authpermission'),
(39, 'Can delete auth permission', 10, 'delete_authpermission'),
(40, 'Can view auth permission', 10, 'view_authpermission'),
(41, 'Can add auth user', 11, 'add_authuser'),
(42, 'Can change auth user', 11, 'change_authuser'),
(43, 'Can delete auth user', 11, 'delete_authuser'),
(44, 'Can view auth user', 11, 'view_authuser'),
(45, 'Can add auth user groups', 12, 'add_authusergroups'),
(46, 'Can change auth user groups', 12, 'change_authusergroups'),
(47, 'Can delete auth user groups', 12, 'delete_authusergroups'),
(48, 'Can view auth user groups', 12, 'view_authusergroups'),
(49, 'Can add auth user user permissions', 13, 'add_authuseruserpermissions'),
(50, 'Can change auth user user permissions', 13, 'change_authuseruserpermissions'),
(51, 'Can delete auth user user permissions', 13, 'delete_authuseruserpermissions'),
(52, 'Can view auth user user permissions', 13, 'view_authuseruserpermissions'),
(53, 'Can add bank', 14, 'add_bank'),
(54, 'Can change bank', 14, 'change_bank'),
(55, 'Can delete bank', 14, 'delete_bank'),
(56, 'Can view bank', 14, 'view_bank'),
(57, 'Can add booking', 15, 'add_booking'),
(58, 'Can change booking', 15, 'change_booking'),
(59, 'Can delete booking', 15, 'delete_booking'),
(60, 'Can view booking', 15, 'view_booking'),
(61, 'Can add django admin log', 16, 'add_djangoadminlog'),
(62, 'Can change django admin log', 16, 'change_djangoadminlog'),
(63, 'Can delete django admin log', 16, 'delete_djangoadminlog'),
(64, 'Can view django admin log', 16, 'view_djangoadminlog'),
(65, 'Can add django content type', 17, 'add_djangocontenttype'),
(66, 'Can change django content type', 17, 'change_djangocontenttype'),
(67, 'Can delete django content type', 17, 'delete_djangocontenttype'),
(68, 'Can view django content type', 17, 'view_djangocontenttype'),
(69, 'Can add django migrations', 18, 'add_djangomigrations'),
(70, 'Can change django migrations', 18, 'change_djangomigrations'),
(71, 'Can delete django migrations', 18, 'delete_djangomigrations'),
(72, 'Can view django migrations', 18, 'view_djangomigrations'),
(73, 'Can add django session', 19, 'add_djangosession'),
(74, 'Can change django session', 19, 'change_djangosession'),
(75, 'Can delete django session', 19, 'delete_djangosession'),
(76, 'Can view django session', 19, 'view_djangosession'),
(77, 'Can add feedback', 20, 'add_feedback'),
(78, 'Can change feedback', 20, 'change_feedback'),
(79, 'Can delete feedback', 20, 'delete_feedback'),
(80, 'Can view feedback', 20, 'view_feedback'),
(81, 'Can add login', 21, 'add_login'),
(82, 'Can change login', 21, 'change_login'),
(83, 'Can delete login', 21, 'delete_login'),
(84, 'Can view login', 21, 'view_login'),
(85, 'Can add master', 22, 'add_master'),
(86, 'Can change master', 22, 'change_master'),
(87, 'Can delete master', 22, 'delete_master'),
(88, 'Can view master', 22, 'view_master'),
(89, 'Can add package', 23, 'add_package'),
(90, 'Can change package', 23, 'change_package'),
(91, 'Can delete package', 23, 'delete_package'),
(92, 'Can view package', 23, 'view_package'),
(93, 'Can add reg', 24, 'add_reg'),
(94, 'Can change reg', 24, 'change_reg'),
(95, 'Can delete reg', 24, 'delete_reg'),
(96, 'Can view reg', 24, 'view_reg'),
(97, 'Can add scheduling', 25, 'add_scheduling'),
(98, 'Can change scheduling', 25, 'change_scheduling'),
(99, 'Can delete scheduling', 25, 'delete_scheduling'),
(100, 'Can view scheduling', 25, 'view_scheduling'),
(101, 'Can add studentfee', 26, 'add_studentfee'),
(102, 'Can change studentfee', 26, 'change_studentfee'),
(103, 'Can delete studentfee', 26, 'delete_studentfee'),
(104, 'Can view studentfee', 26, 'view_studentfee'),
(105, 'Can add video tips', 27, 'add_videotips'),
(106, 'Can change video tips', 27, 'change_videotips'),
(107, 'Can delete video tips', 27, 'delete_videotips'),
(108, 'Can view video tips', 27, 'view_videotips');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `bank`
--

CREATE TABLE `bank` (
  `bank_id` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `card_number` varchar(200) NOT NULL,
  `expiry` varchar(200) NOT NULL,
  `cvv` int(11) NOT NULL,
  `amount` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `bank`
--

INSERT INTO `bank` (`bank_id`, `name`, `card_number`, `expiry`, `cvv`, `amount`) VALUES
(1, 'vipin', '12345', '12/2024', 123, 6000);

-- --------------------------------------------------------

--
-- Table structure for table `booking`
--

CREATE TABLE `booking` (
  `bookid` int(50) NOT NULL,
  `fk_reg_id` int(11) NOT NULL,
  `fk_master_id` int(11) NOT NULL,
  `fk_package_id` int(11) NOT NULL,
  `booking_date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `booking`
--

INSERT INTO `booking` (`bookid`, `fk_reg_id`, `fk_master_id`, `fk_package_id`, `booking_date`) VALUES
(29, 32, 37, 28, '2024-01-16'),
(30, 33, 38, 30, '2024-01-17');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(7, 'martial_arts', 'arts'),
(8, 'martial_arts', 'authgroup'),
(9, 'martial_arts', 'authgrouppermissions'),
(10, 'martial_arts', 'authpermission'),
(11, 'martial_arts', 'authuser'),
(12, 'martial_arts', 'authusergroups'),
(13, 'martial_arts', 'authuseruserpermissions'),
(14, 'martial_arts', 'bank'),
(15, 'martial_arts', 'booking'),
(16, 'martial_arts', 'djangoadminlog'),
(17, 'martial_arts', 'djangocontenttype'),
(18, 'martial_arts', 'djangomigrations'),
(19, 'martial_arts', 'djangosession'),
(20, 'martial_arts', 'feedback'),
(21, 'martial_arts', 'login'),
(22, 'martial_arts', 'master'),
(23, 'martial_arts', 'package'),
(24, 'martial_arts', 'reg'),
(25, 'martial_arts', 'scheduling'),
(26, 'martial_arts', 'studentfee'),
(27, 'martial_arts', 'videotips'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2023-12-05 08:43:01.499408'),
(2, 'auth', '0001_initial', '2023-12-05 08:43:31.294552'),
(3, 'admin', '0001_initial', '2023-12-05 08:44:21.028717'),
(4, 'admin', '0002_logentry_remove_auto_add', '2023-12-05 08:44:32.256836'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2023-12-05 08:44:32.636837'),
(6, 'contenttypes', '0002_remove_content_type_name', '2023-12-05 08:44:38.489845'),
(7, 'auth', '0002_alter_permission_name_max_length', '2023-12-05 08:44:45.241855'),
(8, 'auth', '0003_alter_user_email_max_length', '2023-12-05 08:44:45.951856'),
(9, 'auth', '0004_alter_user_username_opts', '2023-12-05 08:44:46.141856'),
(10, 'auth', '0005_alter_user_last_login_null', '2023-12-05 08:44:49.603863'),
(11, 'auth', '0006_require_contenttypes_0002', '2023-12-05 08:44:49.793864'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2023-12-05 08:44:50.043864'),
(13, 'auth', '0008_alter_user_username_max_length', '2023-12-05 08:44:51.213866'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2023-12-05 08:44:52.743868'),
(15, 'auth', '0010_alter_group_name_max_length', '2023-12-05 08:44:53.891872'),
(16, 'auth', '0011_update_proxy_permissions', '2023-12-05 08:44:54.391873'),
(17, 'sessions', '0001_initial', '2023-12-05 08:45:00.099886');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

CREATE TABLE `feedback` (
  `feedid` int(50) NOT NULL,
  `subject` varchar(200) NOT NULL,
  `message` text NOT NULL,
  `sender` varchar(200) NOT NULL,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `feedback`
--

INSERT INTO `feedback` (`feedid`, `subject`, `message`, `sender`, `date`) VALUES
(11, 'czxc', 'czcs', 'ambadi@gmail.com', '2024-01-16'),
(12, 'sdfsf', 'sddfgdg', 'd@gmail.com', '2024-01-20');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `username` varchar(200) NOT NULL,
  `password` varchar(200) NOT NULL,
  `usertype` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`username`, `password`, `usertype`) VALUES
('aa@gmail.com', 'aaa', 'master'),
('admin@gmail.com', 'admin', 'admin'),
('ambadi@gmail.com', 'ambadi123', 'student'),
('appu@gmail.com', 'appu1234', 'master'),
('d@gmail.com', 'ddd', 'student');

-- --------------------------------------------------------

--
-- Table structure for table `master`
--

CREATE TABLE `master` (
  `master_id` int(20) NOT NULL,
  `fk_art_id` int(11) NOT NULL,
  `full_name` varchar(200) NOT NULL,
  `profile` text NOT NULL,
  `phone` varchar(200) NOT NULL,
  `email` varchar(200) NOT NULL,
  `gender` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `master`
--

INSERT INTO `master` (`master_id`, `fk_art_id`, `full_name`, `profile`, `phone`, `email`, `gender`) VALUES
(37, 34, 'Appu s', 'dferr', '7890987657', 'appu@gmail.com', 'Male'),
(38, 35, 'aaaa', 'ffg', '9876545657', 'aa@gmail.com', 'Male');

-- --------------------------------------------------------

--
-- Table structure for table `package`
--

CREATE TABLE `package` (
  `packgeid` int(20) NOT NULL,
  `package_title` varchar(200) NOT NULL,
  `fk_arts_id` int(11) NOT NULL,
  `duration` varchar(30) NOT NULL,
  `cost` decimal(18,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `package`
--

INSERT INTO `package` (`packgeid`, `package_title`, `fk_arts_id`, `duration`, `cost`) VALUES
(28, 'sadas', 34, '3 months', '3000.00'),
(30, 'hh', 35, '4 months', '25000.00');

-- --------------------------------------------------------

--
-- Table structure for table `reg`
--

CREATE TABLE `reg` (
  `reg_id` int(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `address` varchar(200) NOT NULL,
  `phoneno` varchar(50) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `emailid` varchar(50) NOT NULL,
  `dob` date NOT NULL,
  `usertype` varchar(50) NOT NULL,
  `doj` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `reg`
--

INSERT INTO `reg` (`reg_id`, `name`, `address`, `phoneno`, `gender`, `emailid`, `dob`, `usertype`, `doj`) VALUES
(32, 'Ambadi', 'ddd', '8989898989', 'male', 'ambadi@gmail.com', '2012-02-12', 'student', '2023-12-12'),
(33, 'ddd', 'b bgf', '8909876543', 'Female', 'd@gmail.com', '2015-01-01', 'student', '2024-01-03');

-- --------------------------------------------------------

--
-- Table structure for table `scheduling`
--

CREATE TABLE `scheduling` (
  `scheduleid` int(50) NOT NULL,
  `time_from` varchar(50) NOT NULL,
  `time_to` varchar(50) NOT NULL,
  `date` date NOT NULL,
  `fk_package_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `scheduling`
--

INSERT INTO `scheduling` (`scheduleid`, `time_from`, `time_to`, `date`, `fk_package_id`) VALUES
(51, '15:30', '17:30', '2024-01-12', 28);

-- --------------------------------------------------------

--
-- Table structure for table `studentfee`
--

CREATE TABLE `studentfee` (
  `feeid` int(11) NOT NULL,
  `fk_book_id` int(11) NOT NULL,
  `amount` decimal(18,2) NOT NULL,
  `due_date` date NOT NULL,
  `pay_date` date DEFAULT NULL,
  `status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `studentfee`
--

INSERT INTO `studentfee` (`feeid`, `fk_book_id`, `amount`, `due_date`, `pay_date`, `status`) VALUES
(17, 29, '3000.00', '2024-01-23', '2024-01-22', 'paid');

-- --------------------------------------------------------

--
-- Table structure for table `video_tips`
--

CREATE TABLE `video_tips` (
  `tips_id` int(11) NOT NULL,
  `title` varchar(200) NOT NULL,
  `description` text NOT NULL,
  `video_url` text NOT NULL,
  `fk_arts_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `video_tips`
--

INSERT INTO `video_tips` (`tips_id`, `title`, `description`, `video_url`, `fk_arts_id`) VALUES
(15, 'karatte', 'This vedio contains complete workout for Karate for kids. Do practice while watching the vedio.', 'https://www.youtube.com/embed/PQ6w7hSl-TM?si=aI2WJQ99bVR6V9By', 34);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `arts`
--
ALTER TABLE `arts`
  ADD PRIMARY KEY (`artsid`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `bank`
--
ALTER TABLE `bank`
  ADD PRIMARY KEY (`bank_id`);

--
-- Indexes for table `booking`
--
ALTER TABLE `booking`
  ADD PRIMARY KEY (`bookid`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `feedback`
--
ALTER TABLE `feedback`
  ADD PRIMARY KEY (`feedid`);

--
-- Indexes for table `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`username`);

--
-- Indexes for table `master`
--
ALTER TABLE `master`
  ADD PRIMARY KEY (`master_id`);

--
-- Indexes for table `package`
--
ALTER TABLE `package`
  ADD PRIMARY KEY (`packgeid`);

--
-- Indexes for table `reg`
--
ALTER TABLE `reg`
  ADD PRIMARY KEY (`reg_id`);

--
-- Indexes for table `scheduling`
--
ALTER TABLE `scheduling`
  ADD PRIMARY KEY (`scheduleid`);

--
-- Indexes for table `studentfee`
--
ALTER TABLE `studentfee`
  ADD PRIMARY KEY (`feeid`);

--
-- Indexes for table `video_tips`
--
ALTER TABLE `video_tips`
  ADD PRIMARY KEY (`tips_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `arts`
--
ALTER TABLE `arts`
  MODIFY `artsid` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=109;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `booking`
--
ALTER TABLE `booking`
  MODIFY `bookid` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `feedback`
--
ALTER TABLE `feedback`
  MODIFY `feedid` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `master`
--
ALTER TABLE `master`
  MODIFY `master_id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=39;

--
-- AUTO_INCREMENT for table `package`
--
ALTER TABLE `package`
  MODIFY `packgeid` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT for table `reg`
--
ALTER TABLE `reg`
  MODIFY `reg_id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;

--
-- AUTO_INCREMENT for table `scheduling`
--
ALTER TABLE `scheduling`
  MODIFY `scheduleid` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=53;

--
-- AUTO_INCREMENT for table `studentfee`
--
ALTER TABLE `studentfee`
  MODIFY `feeid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `video_tips`
--
ALTER TABLE `video_tips`
  MODIFY `tips_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

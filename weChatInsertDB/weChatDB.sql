drop schema if exists wechatDB;
create schema wechatDB;
use wechatDB;
drop table if exists weChatinfo;
CREATE TABLE `wechatinfo` (
  `ID` varchar(250) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `nickName` varchar(250) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `remarkName` varchar(250) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `city` varchar(250) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `province` varchar(250) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `sex` varchar(25) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `userName` varchar(250) COLLATE utf8mb4_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
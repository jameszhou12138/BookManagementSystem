/*
 Navicat Premium Data Transfer

 Source Server         : test
 Source Server Type    : MySQL
 Source Server Version : 80028
 Source Host           : localhost:3306
 Source Schema         : books

 Target Server Type    : MySQL
 Target Server Version : 80028
 File Encoding         : 65001

 Date: 03/06/2022 00:07:24
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for 书籍信息
-- ----------------------------
DROP TABLE IF EXISTS `书籍信息`;
CREATE TABLE `书籍信息`  (
  `id` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '书籍序号',
  `name` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL COMMENT '书籍名称',
  `author` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL COMMENT '书籍作者',
  `press` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL COMMENT '书籍出版',
  `type` enum('专业书','工具书','报告','小说','其他') CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '书籍类别',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 书籍信息
-- ----------------------------
INSERT INTO `书籍信息` VALUES ('9781302023683', '数据结构（C语言版）', '严蔚敏', '清华大学出版社', '专业书');
INSERT INTO `书籍信息` VALUES ('9787020017799', '简爱', 'Charlotte Bronte', '人民文学出版社', '小说');
INSERT INTO `书籍信息` VALUES ('9787020019526', '格林童话全集', 'Wilhelm Grimm', '人民文学出版社', '其他');
INSERT INTO `书籍信息` VALUES ('9787020019533', '悲惨世界', 'Victor Hugo', '人民文学出版社', '小说');
INSERT INTO `书籍信息` VALUES ('9787020019915', '傲慢与偏见', 'Jane Austen', '人民文学出版社', '小说');
INSERT INTO `书籍信息` VALUES ('9787020125548', '西游记', '吴承恩', '人民文学出版社', '小说');
INSERT INTO `书籍信息` VALUES ('9787020125555', '三国演义', '罗贯中', '人民文学出版社', '小说');
INSERT INTO `书籍信息` VALUES ('9787020125562', '红楼梦', '曹雪芹', '人民文学出版社', '小说');
INSERT INTO `书籍信息` VALUES ('9787020125579', '水浒传', '施耐庵', '人民文学出版社', '小说');
INSERT INTO `书籍信息` VALUES ('9787040223903', '计算机组成原理', '唐朔飞', '高等教育出版社', '专业书');
INSERT INTO `书籍信息` VALUES ('9787100124508', '现代汉语词典', '吕叔湘', '商务印书馆', '工具书');
INSERT INTO `书籍信息` VALUES ('9787100158602', '牛津高阶英汉双解词典', 'Nick Hornby', '商务印书馆', '工具书');
INSERT INTO `书籍信息` VALUES ('9787100184465', '英国面孔', 'Simon Schama', '商务印书馆', '其他');
INSERT INTO `书籍信息` VALUES ('9787108006639', '笑傲江湖', '金庸', '生活·读书·新知三联书店', '小说');
INSERT INTO `书籍信息` VALUES ('9787108006660', '神雕侠侣', '金庸', '生活·读书·新知三联书店', '小说');
INSERT INTO `书籍信息` VALUES ('9787108006721', '天龙八部', '金庸', '生活·读书·新知三联书店', '小说');
INSERT INTO `书籍信息` VALUES ('9787108057037', '汉字王国', '林西莉', '生活·读书·新知三联书店', '其他');
INSERT INTO `书籍信息` VALUES ('9787111075752', '设计模式', 'Erich Gramma', '机械工业出版社', '专业书');
INSERT INTO `书籍信息` VALUES ('9787111190561', '数据挖掘技术', 'MichaelJ.A.B', '机械工业出版社', '专业书');
INSERT INTO `书籍信息` VALUES ('9787111213826', 'Java编程思想', 'Bruce Eckel', '机械工业出版社', '专业书');
INSERT INTO `书籍信息` VALUES ('9787111321330', '深入理解计算机系统', 'Randal E.Bryant', '机械工业出版社', '专业书');
INSERT INTO `书籍信息` VALUES ('9787111367291', '编程原本', 'Alexander Stepanov', '机械工业出版社', '专业书');
INSERT INTO `书籍信息` VALUES ('9787111375296', '数据库系统概念', 'Abraham Silberschatz', '机械工业出版社', '专业书');
INSERT INTO `书籍信息` VALUES ('9787111407010', '算法导论', 'Thomas H.Cormen', '机械工业出版社', '专业书');
INSERT INTO `书籍信息` VALUES ('9787111612728', 'Effective Java', 'Joshua Bloch', '机械工业出版社', '专业书');
INSERT INTO `书籍信息` VALUES ('9787115320100', '挑战程序设计竞赛', '秋叶拓哉', '人民邮电出版社', '工具书');
INSERT INTO `书籍信息` VALUES ('9787115328670', 'Linux/UNIX系统编程手册', 'Michael Kerrisk', '人民邮电出版社', '工具书');
INSERT INTO `书籍信息` VALUES ('9787115390592', 'C Primer Plus', 'Stephen Prada', '人民邮电出版社', '工具书');
INSERT INTO `书籍信息` VALUES ('9787121155352', 'C++ Primer', 'Stanley B. Lippman', '电子工业出版社', '工具书');
INSERT INTO `书籍信息` VALUES ('9787121411748', '计算机网络', '谢希仁', '电子工业出版社', '专业书');
INSERT INTO `书籍信息` VALUES ('9787300103563', '组织与管理', 'Chester I. Barnard', '中国人民大学出版社', '其他');
INSERT INTO `书籍信息` VALUES ('9787302206088', '算法竞赛入门经典', '刘汝佳', '清华大学出版社', '工具书');
INSERT INTO `书籍信息` VALUES ('9787302294139', 'ACM国际大学生程序设计竞赛', '俞勇', '清华大学出版社', '工具书');
INSERT INTO `书籍信息` VALUES ('9787302529156', '算法竞赛入门到进阶', '罗勇军', '清华大学出版社', '工具书');
INSERT INTO `书籍信息` VALUES ('9787500627098', '沉默的大多数', '王小波', '中国青年出版社', '其他');
INSERT INTO `书籍信息` VALUES ('9787500646716', '青铜时代', '王小波', '中国青年出版社', '其他');
INSERT INTO `书籍信息` VALUES ('9787500646723', '黑铁时代', '王小波', '中国青年出版社', '其他');
INSERT INTO `书籍信息` VALUES ('9787500646730', '黄金时代 白银时代', '王小波', '中国青年出版社', '其他');
INSERT INTO `书籍信息` VALUES ('9787508630069', '史蒂夫·乔布斯传', 'Walter Isaacson', '中信出版社', '其他');
INSERT INTO `书籍信息` VALUES ('9787520714907', '现代英国的形成', 'Andrew Marr', '东方出版社', '其他');
INSERT INTO `书籍信息` VALUES ('9787533964641', '安徒生童话全集', 'H. C. Andersen', '浙江文艺出版社', '其他');
INSERT INTO `书籍信息` VALUES ('9787544510813', '聊斋志异', '蒲松龄', '长春出版社', '小说');
INSERT INTO `书籍信息` VALUES ('9787547737897', '美国独立70年', 'Jonathan Israel', '北京日报出版社', '其他');
INSERT INTO `书籍信息` VALUES ('9787553811215', '菜根谭', '洪应明', '岳麓书社', '小说');
INSERT INTO `书籍信息` VALUES ('9787560633503', '计算机操作系统', '汤小丹', '西安电子科技大学出版社', '专业书');
INSERT INTO `书籍信息` VALUES ('9787570206131', '2018年中国报告文学精选', '中国作协创研部', '长江文艺出版社', '报告');
INSERT INTO `书籍信息` VALUES ('9787570213863', '2019年中国报告文学精选', '中国作协创研部', '长江文艺出版社', '报告');
INSERT INTO `书籍信息` VALUES ('9787570219438', '2020年中国报告文学精选', '中国作协创研部', '长江文艺出版社', '报告');
INSERT INTO `书籍信息` VALUES ('9787570222414', '2021年中国报告文学精选', '中国作协创研部', '长江文艺出版社', '报告');
INSERT INTO `书籍信息` VALUES ('9787893881985', '算法竞赛进阶指南', '李煜东', '河南电子音像出版社', '工具书');

SET FOREIGN_KEY_CHECKS = 1;
